
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace
from pyspark.ml.feature import Tokenizer, StopWordsRemover, CountVectorizer, IDF
from pyspark.ml.linalg import Vector

spark = SparkSession.builder.appName("TFIDFBookSimilarity").getOrCreate()

# Load books
books_df = (
    spark.read
    .option("wholetext", "true")
    .text("/path/to/gutenberg/*.txt")
    .withColumnRenamed("value", "text")
    .withColumn("file_name", col("input_file_name()"))
)

# Clean text
cleaned_df = books_df.withColumn(
    "clean_text",
    regexp_replace(lower(col("text")), "[^a-z\\s]", "")
)

# Tokenization
tokenizer = Tokenizer(inputCol="clean_text", outputCol="words")
tokenized_df = tokenizer.transform(cleaned_df)

# Stopword removal
remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")
filtered_df = remover.transform(tokenized_df)

# TF
cv = CountVectorizer(
    inputCol="filtered_words",
    outputCol="tf_features",
    vocabSize=500,
    minDF=1
)
cv_model = cv.fit(filtered_df)
tf_df = cv_model.transform(filtered_df)

# IDF
idf = IDF(inputCol="tf_features", outputCol="tfidf_features")
idf_model = idf.fit(tf_df)
tfidf_df = idf_model.transform(tf_df)

# Cosine similarity function
def cosine_similarity(v1: Vector, v2: Vector) -> float:
    dot = v1.dot(v2)
    norm = v1.norm(2) * v2.norm(2)
    return float(dot / norm) if norm != 0 else 0.0

# Compute similarity with target book
target_book = "200.txt"

target_vector = (
    tfidf_df
    .filter(col("file_name").endswith(target_book))
    .select("tfidf_features")
    .first()[0]
)

similarities = (
    tfidf_df
    .filter(~col("file_name").endswith(target_book))
    .select("file_name", "tfidf_features")
    .rdd
    .map(lambda row: (row[0], cosine_similarity(target_vector, row[1])))
    .sortBy(lambda x: x[1], ascending=False)
)

top5_similar = similarities.take(5)

spark.stop()

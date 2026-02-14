
rom pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, abs

spark = SparkSession.builder.appName("AuthorInfluenceNetwork").getOrCreate()

# Load books
books_df = (
    spark.read
    .option("wholetext", "true")
    .text("/path/to/gutenberg/*.txt")
    .withColumnRenamed("value", "text")
    .withColumn("file_name", col("input_file_name()"))
)

# Extract author and year
author_df = (
    books_df
    .withColumn("author", regexp_extract(col("text"), "(?i)author:\\s*(.*)", 1))
    .withColumn("year", regexp_extract(col("text"), "(\\d{4})", 1))
    .filter(col("author") != "")
    .filter(col("year") != "")
)

author_df = author_df.select("author", col("year").cast("int"))

# Influence window
X = 5

# Self-join to form influence edges
edges = (
    author_df.alias("a")
    .join(author_df.alias("b"), col("a.author") != col("b.author"))
    .filter(abs(col("a.year") - col("b.year")) <= X)
    .select(
        col("a.author").alias("author1"),
        col("b.author").alias("author2")
    )
)

# Out-degree
out_degree = edges.groupBy("author1").count().withColumnRenamed("count", "out_degree")

# In-degree
in_degree = edges.groupBy("author2").count().withColumnRenamed("count", "in_degree")

spark.stop()

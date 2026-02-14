

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract, length, desc

spark = SparkSession.builder.appName("BookMetadataExtraction").getOrCreate()

# Load Project Gutenberg books
books_df = (
    spark.read
    .option("wholetext", "true")
    .text("/path/to/gutenberg/*.txt")
    .withColumnRenamed("value", "text")
    .withColumn("file_name", col("input_file_name()"))
)

# Metadata extraction using regex
metadata_df = (
    books_df
    .withColumn("title", regexp_extract(col("text"), "(?i)title:\\s*(.*)", 1))
    .withColumn("release_date", regexp_extract(col("text"), "(?i)release date:\\s*(.*)", 1))
    .withColumn("language", regexp_extract(col("text"), "(?i)language:\\s*(.*)", 1))
    .withColumn("encoding", regexp_extract(col("text"), "(?i)character set encoding:\\s*(.*)", 1))
)

# Books released per year
books_per_year = (
    metadata_df
    .withColumn("year", regexp_extract(col("release_date"), "(\\d{4})", 1))
    .filter(col("year") != "")
    .groupBy("year")
    .count()
    .orderBy("year")
)

# Most common language
common_language = (
    metadata_df
    .filter(col("language") != "")
    .groupBy("language")
    .count()
    .orderBy(desc("count"))
)

# Average title length
avg_title_length = metadata_df.select(length(col("title")).alias("len")).groupBy().avg("len")

spark.stop()

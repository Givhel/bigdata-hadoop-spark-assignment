
# Hadoop WordCount Example

This folder contains the Java implementation of the WordCount program using
Apache Hadoop MapReduce.

## Description
The program reads text files from HDFS and counts the frequency of each word.

## Steps to Run
1. Compile the program:
   hadoop com.sun.tools.javac.Main WordCount.java

2. Create JAR file:
   jar cf wordcount.jar WordCount*.class

3. Run the job:
   hadoop jar wordcount.jar WordCount <input_path> <output_path>

## Output
The output is written to HDFS and contains word-frequency pairs.

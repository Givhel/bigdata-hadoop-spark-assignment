

---

## 📄 File Description

### 1. `WordCount.java`
- Java implementation of the WordCount MapReduce program.
- Contains:
  - **Mapper class**: Tokenizes input text and emits `(word, 1)` pairs.
  - **Reducer class**: Aggregates counts for each word.
  - **Main method**: Configures the job, input path, output path, mapper, reducer, and runs the job.

This code follows the structure discussed in class and referenced from the Apache Hadoop MapReduce Tutorial.

---

### 2. `README.md`
- Explains the purpose of the WordCount program.
- Describes how the code is organized and executed.
- Complements the execution screenshots provided in the PDF report.

---

## ▶️ Execution Overview
The WordCount program was executed on a **pseudo-distributed Hadoop setup** using HDFS.

High-level steps followed:
1. Start Hadoop services (HDFS and YARN).
2. Create input directory in HDFS.
3. Upload input text file to HDFS.
4. Run the WordCount MapReduce job using the Hadoop examples JAR.
5. Verify output stored in HDFS.

The successful execution and output verification are shown using screenshots in the submitted PDF report.

---

## ✅ Output Verification
- Output is generated in the HDFS output directory.
- Each line of output is of the form:

- This confirms correct execution of both the Map and Reduce phases.

---

## 📝 Notes
- Only execution outputs and observations are included in the report as instructed.
- The Project Gutenberg dataset and Hadoop installation files are not included in this repository.
- Screenshots of terminal execution and outputs are provided in the PDF submission.

---

## 👤 Author
**Kunal Mishra**  
CSL7110 – Big Data / Hadoop & Spark  
Assignment 1

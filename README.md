# 📘 Big Data Assignment – Apache Hadoop & Apache Spark

This repository contains the complete implementation for **Assignment 1** of the **CSL7110 – Big Data / Hadoop & Spark** course.  
The assignment focuses on applying **distributed data processing concepts** using **Apache Hadoop MapReduce** and **Apache Spark**.

All tasks were executed locally in **pseudo-distributed mode**, and results were verified through Hadoop CLI outputs and Spark shell execution.

---

## 👤 Student Details

- **Name:** Kunal Mishra  
- **Course:** CSL7110 – Big Data / Hadoop & Spark  
- **Assignment:** Assignment 1 – Hadoop MapReduce & Apache Spark  

---

## 📂 Repository Contents

### 🔹 Apache Hadoop & MapReduce
- Executed the standard **WordCount** example using Hadoop MapReduce.
- Verified correct execution through HDFS input/output and job completion logs.
- Demonstrated usage of HDFS commands and MapReduce workflow.

### 🔹 Apache Spark

The Spark section covers analytical tasks performed on the **Project Gutenberg dataset**:

#### 1. Book Metadata Extraction and Analysis
- Extracted metadata such as **title**, **release date**, **language**, and **encoding** using regular expressions.
- Performed analysis to determine:
  - Number of books released per year
  - Most common language
  - Average length of book titles

#### 2. TF-IDF Based Book Similarity (Cosine Similarity)
- Cleaned and preprocessed raw book text.
- Tokenized text, removed stop words, and generated term frequency vectors.
- Computed **TF-IDF scores** for each book.
- Calculated **cosine similarity** to identify the most similar books.

#### 3. Author Influence Network
- Extracted author names and release years from book text.
- Constructed a simplified **author influence network** based on temporal proximity of book releases.
- Computed **in-degree** and **out-degree** to identify influential authors.

---

## 📊 Dataset Information

- The **Project Gutenberg dataset** (≈184 MB, multiple `.txt` files) was used.
- Due to its large size, the dataset is **not uploaded** to this repository.
- Sample files such as `200.txt`, `10.txt`, and `5.txt` were used during execution.
- The same dataset was reused for both Hadoop and Spark tasks as instructed.

---

## 📝 Submission Notes

- All **results, observations, and explanations** are included in the submitted **PDF report**.
- Screenshots of Hadoop and Spark executions are attached in the report.
- This repository contains all **code implementations** required for evaluation.

---

## ✅ Declaration

This work is **original** and completed by me as part of the CSL7110 course assignment.  
No code has been copied from external online resources.

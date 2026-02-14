# Apache Spark – Assignment 1

This folder contains PySpark programs developed for Assignment 1 of CSL7110.
The tasks demonstrate large-scale text processing and analysis using Apache Spark
on the Project Gutenberg dataset.

## Implemented Tasks

1. **Book Metadata Extraction and Analysis**
   - Extracted title, release date, language, and encoding using regular expressions.
   - Analyzed book releases per year, most common language, and average title length.

2. **TF-IDF Based Book Similarity Using Cosine Similarity**
   - Performed text preprocessing (cleaning, tokenization, stopword removal).
   - Computed Term Frequency (TF) and Inverse Document Frequency (IDF).
   - Generated TF-IDF vectors for each book.
   - Measured similarity between books using **cosine similarity** to identify the most similar books.

3. **Author Influence Network Construction**
   - Extracted author names and release years from book text.
   - Constructed a directed influence network based on temporal proximity of releases.
   - Computed in-degree and out-degree for each author to identify influential authors.

## Notes

- Execution was performed using Spark Shell for interactive analysis.
- Screenshots of execution outputs are included in the submitted PDF report.
- Code is provided here for reproducibility and evaluation.

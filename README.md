# Python Indexer for CACM Corpus
## Overview
This repository contains a Python script for indexing the CACM (Communications of the ACM) corpus, a collection of academic papers, using an inverted index. The indexer processes the text documents in the corpus, tokenizes them into individual terms, and constructs an inverted index mapping terms to the documents in which they appear. This facilitates efficient text search and retrieval within the corpus.

## Usage
**Clone the Repository:** Clone this repository to your local machine using the following command:

git clone https://github.com/kepo402/PythonIndexer.git
**Download CACM Corpus:** Download the CACM corpus from source and extract the contents into the repository folder.

**Run the Indexer:** Execute the Python script Code_indexer.py to index the documents in the CACM corpus:

python Code_indexer.py
**View Output:** After running the indexer, you'll find two output files in the repository folder:

**documents.dat:** Contains statistics about the indexing process.
**index.dat:** Contains the inverted index mapping terms to documents.

## Requirements
Python 3.x

## Files Included
**Code_indexer.py:** Python script for indexing the CACM corpus.
**documents.dat:** Output file containing indexing statistics.
**index.dat:** Output file containing the inverted index.





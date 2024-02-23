import os
import re
import pickle
import math

# Define the regular expression for tokenization
tokenizer = re.compile(r'\W+')

# Initialize variables for statistics
num_documents_processed = 0
total_terms_parsed = 0
unique_terms_added = 0

# Define the list of stop words
stop_words = ["and", "the", "is", "in", "of", ...]  # Add more stop words as needed

# Initialize the inverted index
inverted_index = {}

# Function to tokenize a query
def tokenize_query(query):
    tokens = tokenizer.split(query.lower())
    filtered_tokens = [token for token in tokens if token not in stop_words]  # Filter out stop words
    return filtered_tokens

# Function to load index data from a file
def load_index(index_filename):
    global inverted_index
    with open(index_filename, 'rb') as f:
        inverted_index = pickle.load(f)

# Function to calculate TF-IDF weight
def calculate_tfidf(tf, df, N):
    return tf * math.log(N / df)

# Function to perform information retrieval with TF-IDF ranking
def search(query, index_filename):
    load_index(index_filename)  # Load the index data
    query_tokens = tokenize_query(query)
    relevant_documents = {}
    for token in query_tokens:
        if token in inverted_index:
            for doc_id, tf in inverted_index[token].items():
                df = len(inverted_index[token])
                tfidf = calculate_tfidf(tf, df, num_documents_processed)
                if doc_id not in relevant_documents:
                    relevant_documents[doc_id] = 0
                relevant_documents[doc_id] += tfidf
    return relevant_documents
import os
import re
import pickle
import math

# Define the regular expression for tokenization
tokenizer = re.compile(r'\W+')

# Function to load index data from a file
def load_index(index_filename):
    with open(index_filename, 'rb') as f:
        return pickle.load(f)

# Function to calculate TF-IDF weight
def calculate_tfidf(tf, df, N):
    return tf * math.log(N / df)

# Function to perform information retrieval with TF-IDF ranking
def search(query, index_filename):
    inverted_index = load_index(index_filename)  # Load the index data
    query_tokens = query.split()  # Split the query into tokens
    relevant_documents = {}
    for token in query_tokens:
        if token in inverted_index:
            for doc_id in inverted_index[token]:  # Iterate over the document IDs in the set
                tf = 1  # Assume binary term frequency
                df = len(inverted_index[token])
                tfidf = calculate_tfidf(tf, df, len(inverted_index))  # Use the total number of documents as N
                if doc_id not in relevant_documents:
                    relevant_documents[doc_id] = 0
                relevant_documents[doc_id] += tfidf
    return relevant_documents
if __name__ == "__main__":
    main()
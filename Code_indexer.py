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
stop_words_count = 0

# Define the list of stop words
stop_words = ["and", "the", "is", "in", "of", ...]  # Add more stop words as needed

# Initialize the inverted index
inverted_index = {}

# Function to tokenize a document
def tokenize_document(document):
    global total_terms_parsed
    tokens = tokenizer.split(document.lower())
    total_terms_parsed += len(tokens)
    filtered_tokens = [token for token in tokens if token not in stop_words]  # Filter out stop words
    return filtered_tokens

def build_index(documents_folder):
    global num_documents_processed, unique_terms_added, stop_words_count
    for root, dirs, files in os.walk(documents_folder):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                document = f.read()
                tokens = tokenize_document(document)
                for token in tokens:
                    if token not in inverted_index:
                        inverted_index[token] = {}
                        unique_terms_added += 1
                    # Increment term frequency for the document
                    if filepath not in inverted_index[token]:
                        inverted_index[token][filepath] = 0  # Initialize the term frequency if not exists
                    inverted_index[token][filepath] += 1  # Increment term frequency for the document
                num_documents_processed += 1
                stop_words_count += len([token for token in tokens if token in stop_words])  # Count stop words in document

# Function to save index and documents data to files
def save_data(index_filename, documents_filename):
    with open(index_filename, 'wb') as f:
        pickle.dump(inverted_index, f)
    # Save the statistics to documents file
    with open(documents_filename, 'w') as f:
        f.write(f"Number of documents processed: {num_documents_processed}\n")
        f.write(f"Total number of terms parsed: {total_terms_parsed}\n")
        f.write(f"Total number of unique terms added to the index: {unique_terms_added}\n")
        f.write(f"Total number of terms found that matched one of the stop words: {stop_words_count}\n")
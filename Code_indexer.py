import os
import re
import pickle
import time

# Define the regular expression for tokenization
tokenizer = re.compile(r'\W+')

# Initialize variables for statistics
num_documents_processed = 0
total_terms_parsed = 0
unique_terms_added = 0

# Initialize the inverted index
inverted_index = {}

# Function to tokenize a document
def tokenize_document(document):
    global total_terms_parsed
    tokens = tokenizer.split(document.lower())
    total_terms_parsed += len(tokens)
    return tokens

# Function to build the inverted index
def build_index(documents_folder):
    global num_documents_processed, unique_terms_added
    for root, dirs, files in os.walk(documents_folder):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                document = f.read()
                tokens = tokenize_document(document)
                for token in tokens:
                    if token not in inverted_index:
                        inverted_index[token] = set()
                        unique_terms_added += 1
                    inverted_index[token].add(filepath)
                num_documents_processed += 1

# Function to save index and documents data to files
def save_data(index_filename, documents_filename):
    with open(index_filename, 'wb') as f:
        pickle.dump(inverted_index, f)
    # Save the statistics to documents file
    with open(documents_filename, 'w') as f:
        f.write(f"Number of documents processed: {num_documents_processed}\n")
        f.write(f"Total number of terms parsed: {total_terms_parsed}\n")
        f.write(f"Total number of unique terms added to the index: {unique_terms_added}\n")

# Main function
def main():
    start_time = time.time()
    documents_folder = r"C:\Users\MOJISOLA EMMANUEL\Downloads\cacm"  # Update this with the path to your documents folder
    build_index(documents_folder)
    save_data("index.dat", "documents.dat")
    end_time = time.time()
    print(f"Indexing completed in {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()
import os
import Code_indexer
import search

# Main function
def main():
    # Step 1: Build the inverted index
    documents_folder = r"C:\Users\MOJISOLA EMMANUEL\Downloads\cacm"  # Update this with the path to your documents folder
    Code_indexer.build_index(documents_folder)  # Only pass the documents_folder
    print("Indexing completed.")

    # Step 2: Perform a search
    index_filename = "index.dat"  # Assuming the index file is available in the current directory
    query = input("Enter your search query: ")
    relevant_documents = search.search(query, index_filename)  # Pass both query and index_filename

    # Step 3: Display search results
    if relevant_documents:
        print("Relevant documents for the query:")
        for doc_id, score in relevant_documents.items():  # Iterate over items for dictionary
            print(f"Document ID: {doc_id}, TF-IDF Score: {score}")
    else:
        print("No relevant documents found for the query.")

if __name__ == "__main__":
    main()
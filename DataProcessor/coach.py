import os
from itertools import combinations
import random
from DataProcessor.files_handler import read_file

def create_labeled_chunks(file_path1, file_path2, chunk_size=10, batch_size=20):
    # Read the files and tokenize the text
    tokens1 = read_file(file_path1).split(' ')
    tokens2 = read_file(file_path2).split(' ')

    # Create chunks and labels
    chunks1 = [tokens1[i:i+chunk_size] for i in range(0, len(tokens1), chunk_size)]
    chunks2 = [tokens2[i:i+chunk_size] for i in range(0, len(tokens2), chunk_size)]
    
    labeled_chunks1 = [(chunk, 0) for chunk in chunks1]
    labeled_chunks2 = [(chunk, 1) for chunk in chunks2]

    labeled_chunks1 = [(chunk, label, i//batch_size) for i, (chunk, label) in enumerate(labeled_chunks1)]
    labeled_chunks2 = [(chunk, label, i//batch_size) for i, (chunk, label) in enumerate(labeled_chunks2)]

    # Combine and shuffle the labeled chunks
    labeled_chunks = labeled_chunks1 + labeled_chunks2
    random.shuffle(labeled_chunks)

    return labeled_chunks


def process_file_pairs(directory):
    # Get all files in the directory
    files = os.listdir(directory)

    # Iterate over all pairs of files
    for file1, file2 in combinations(files, 2):
        # Generate full file paths
        file_path1 = os.path.join(directory, file1)
        file_path2 = os.path.join(directory, file2)

        # Call your function on the file pair
        dataet = create_labeled_chunks(file_path1, file_path2)

# Call the function
tokens_directory = os.path.join(os.environ['HOME'], 'data', 'tokens')
process_file_pairs(tokens_directory)
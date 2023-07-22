import os


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print("File not found at the specified path.")
        print(f"Specified file path: {file_path}")
        print(f"Current file path: {os.getcwd()}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None




################################################################################################################################
################################################################################################################################



from pyarabic.araby import strip_tashkeel

def remove_diacritics(text):
    return strip_tashkeel(text)


################################################################################################################################
################################################################################################################################

from farasa.segmenter import FarasaSegmenter

segmenter = FarasaSegmenter(interactive=True)

def segment(text):
    return segmenter.segment(text)

################################################################################################################################
################################################################################################################################

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('aubmindlab/bert-base-arabertv02')

def tokenize(text):
    return tokenizer.tokenize(text)


################################################################################################################################
################################################################################################################################

def write_string_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(text))

################################################################################################################################
################################################################################################################################


def process_file(file_path, dis_path):

    # read text file content
    text = read_file(file_path)

    # Remove diacritics
    text = remove_diacritics(text)

    # Perform sub-word units segmentation
    text = segment(text)

    # Tokenize the text
    tokens = tokenize(text)

    write_string_to_file(tokens, dis_path)



def process_all_files():
    src_directory = os.path.join(os.environ['HOME'], 'data', 'original_data')
    dis_directory = os.path.join(os.environ['HOME'], 'data', 'tokens')

    for filename in os.listdir(src_directory):
        file_path = os.path.join(src_directory, filename)
        dis_path = os.path.join(dis_directory, filename)
        process_file(file_path, dis_path)
        os.path.dirname
        


os.environ['HOME'] = os.path.dirname(os.path.dirname(__file__))
process_all_files()
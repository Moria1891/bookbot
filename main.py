

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content
    
def main():
    # Get the text
    text = get_book_text(sys.argv[1])
    
    # Get word count
    word_count = get_num_words(text)
    
    # Get character counts
    char_counts_dict = get_char_counts(text)
    
    # Get sorted character list
    sorted_chars = create_new_list(char_counts_dict)
    
    # Print the report (you'll need to format this)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Loop through sorted_chars and print each character (only if it's alphabetical)
    # You'll need to add this part
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")
from stats import get_num_words, get_char_counts, create_new_list

main()
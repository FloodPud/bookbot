from stats import word_count, char_count_dict, sorted_char_count_list
import sys

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]  # Path to the book text file
    book_text = get_book_text(book_path)
    book_word_count = word_count(book_text)
    book_char_dict = char_count_dict(book_text)
    book_sorted_char_list = sorted_char_count_list(book_char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("------- Character Count ---------")
    for item in book_sorted_char_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
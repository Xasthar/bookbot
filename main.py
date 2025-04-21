import sys
from stats import count_of_words, count_of_characters, make_report

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    char_count = count_of_characters(book_path)
    report = make_report(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words(book_path)} total words")
    print("--------- Character Count -------")
    
    for item in report:
        print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")

print(sys.argv)
main()

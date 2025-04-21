def get_book_text(book_path):
    
    with open(book_path) as book:
        book_string = book.read()

        return book_string

def count_of_words(book_path):
    list_of_words = get_book_text(book_path).split()
    word_count = len(list_of_words)

    return word_count

def count_of_characters(book_path):
    char_dictonary = {}
    list_of_words = get_book_text(book_path).lower()

    for letter in list_of_words:
        if letter not in char_dictonary:
            char_dictonary.update({letter: 1})
        else:
            char_dictonary[letter] += 1

    return char_dictonary

def make_report(book_path):
    char_list = []
    char_dictonary = count_of_characters(book_path)
    
    for char, count in char_dictonary.items():
        if char.isalpha():
            char_dict = {"char": char, "count": count}
            char_list.append(char_dict)
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
        
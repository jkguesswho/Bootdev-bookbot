def main():
    book_path = "books/frankenstein.txt"
    # storing the contents of 'book_path' file as a string to var 'text'
    text = read_book_text(book_path)
    # using __.split() to convert the 'text' string to a list
    word_count = get_num_words(text)
    # fn creating a dict of each unique character in string, values of instance count of character
    char_count = get_num_chars(text)
    # print(text)    # print entire contents string to console
    # print the value of word_count to console in a dymanic string
    print(f"{word_count} words found in the document.")
    # print the dictionary char_count
    print("These are all the unique characters in the document and how many times each one occurs:")
    print(char_count)

def read_book_text(path):
    # 'with' block closes files automatically when the block exits for any reason
    # open() opens the inputted file for manipulation and can be aliased like for loop
    with open(path) as f:
        # returned output is a string
        return f.read()
    
def get_num_words(text):
    # __.split() separates the targeted file by a chosen delimiter string (default is space/blank)
    words = text.split()
    # returned output is an integer
    return len(words)

def get_num_chars(text):
    # declaring an empty dictionary
    char_dict = {}
    # __.lower() converts all uppercase characters in the string to lowercase
    text = text.lower()
    # for loop iterating over each single character in the input string
    for char in text:
        # check if character exists as a key in the dictionary
        if char in char_dict:
            # if yes, increment counter by 1
            char_dict[char] += 1
        else:
            # if no, establish new key with value 1
            char_dict[char] = 1
    # debug print statement to check for errors within function
    # print("test1", list(char_dict.items())[:5])
    return char_dict

main()
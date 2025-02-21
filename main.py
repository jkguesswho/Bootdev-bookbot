def main():
    book_path = "books/frankenstein.txt"
    # storing the contents of 'book_path' file as a string to var 'text'
    text = read_book_text(book_path)
    # using __.split() to convert the 'text' string to a list
    word_count = get_num_words(text)
    # fn creating a dict of each unique character in string, values of instance count of character
    char_count = get_num_chars(text)
    # print(text)    # print entire contents string to console
    # print the value of word_count to console in a dymanic string (commented out)
    # print(f"{word_count} words found in the document.")
    # print the dictionary char_count (commented out)
    # print("These are all unique characters in the document and how many times each one occurs:")
    # print(char_count)
    # fn creating a detailed report containing filepath, word count, and alphabetic occurances
    gen_report(book_path, word_count, char_count)

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

def gen_report(path, words, chars):
    # establishing a whitelist of characters for later
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    # beginning report with the filepath
    print(f"--- Begin report of {path} ---")
    # printing the amount of words
    print(f"{words} words found in the document")
    # blank line for formatting
    print()
    # for loop iterating through the alphabet string
    for letter in alphabet:
        # printing iteration letter and value of corresponding key from input dictionary
        print(f"The '{letter}' character was found {chars[letter]} times")
    print("--- End report ---")

"""
# alternate method for creating report, with added frequency ordering!
def gen_report(path, words, chars):
    # converting dict to dict view object then to list for sorting as tuples
    # a dict view object cannot be iterated on, but a list of tuples can be!
    dict_view_obj = chars.items()
    tuple_list = list(dict_view_obj)
    tuple_list.sort(key = lambda item: item[1], reverse = True)
    # beginning with filepath display
    print(f"--- Begin report of {path} ---")
    # printing the amount of words
    print(f"{words} words in the document")
    # blank line for formatting
    print()
    # iterating the list of tuples, checking each key (index 0) if it is an alphabetical character
    for item in tuple_list:
        # if the key is an alphabetical character, print the key and value
        if item[0].isalpha() == True:
            print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")
"""

main()
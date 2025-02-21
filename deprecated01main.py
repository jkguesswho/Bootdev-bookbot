def main():
    # with block to guarantee close the file when the block exits not matter how it exits
    with open("books/frankenstein.txt") as f:
        """
        __.read() loads the contents of the targeted file into a string that is then stored in
        memory. Unlike the CLI 'cat' command, the data string is not inherently printed to console
        but is instead returned so as to be available for manipulation and processing by other
        parts of the program.
        """
        file_contents = f.read()
        # print the stored string to the console, containing the entire contents of the document.
        print(file_contents)
        # __.split() converts the targeted string into a list, default delimiter is space/whitespace
        word_count = file_contents.split()
    # print the number of items in the __.split() output list
    print(len(word_count))
    
main()
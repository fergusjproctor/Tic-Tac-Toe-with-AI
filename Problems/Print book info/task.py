def print_book_info(title, author=None, year=None):
    #  Write your code here
    printable_string = '"' + title + '"'
    if author is not None or year is not None:
        printable_string = printable_string + ' was written'
        if author is not None:
            printable_string = printable_string + ' by ' + author
        if year is not None:
            printable_string = printable_string + ' in ' + year
    print(printable_string)

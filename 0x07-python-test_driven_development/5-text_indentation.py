#!/usr/bin/python3
"""this is for the identation func."""


def text_indentation(text):
    """this func will add two lines --> question mark.

    Args:
        text: this is the string txt.

    Raises:
        TypeError: this error will raise in str input.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

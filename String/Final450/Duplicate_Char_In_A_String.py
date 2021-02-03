# Python program to count all duplicates from string using hashing

NO_OF_CHARS = 256  # 0 to 255


# Fills count array with  frequency of characters
def fill_char_counts(string, count):
    for i in string:
        count[ord(i)] += 1


# Print duplicates present in the passed string
def print_duplicates(string):
    # Create an array of size 256 and fill count of every character in it
    count = [0] * NO_OF_CHARS
    fill_char_counts(string, count)
    print_duplicate_chars(count)


def print_duplicate_chars(count):
    for index, num in enumerate(count):  # enumerate
        if num > 1:
            print(chr(index) + ", count = " + str(num))
    print()


if __name__ == "__main__":
    print_duplicates("test string")
    print_duplicates("prashant")

from Array.Final450.Reverse_Array_Or_String import reverse_pythonic, reverse_iterative, reverse_recursive

if __name__ == "__main__":
    string = "prashant"
    print(reverse_pythonic(string))

    char_arr = list(string)
    print(reverse_iterative(char_arr))
    print(reverse_recursive(char_arr))

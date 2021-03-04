"""
Inplace
"hi"  -> "ih"
"good" -> "doog"

"This is a Cat" -> "taCa si s ihT"
"This is a Cat" -> "taC asi s ihT"

"ab b c" --> "cb b a"   "c b ba"
"""


def reverse_inplace(string):
    n = len(string)
    char_array = [char for char in string]

    i = 0
    j = n - 1
    while i <= j:
        char_array[i], char_array[j] = char_array[j], char_array[i]
        i += 1
        j -= 1

    print("".join(char_array))


def reverse_with_spaces_intact(string):
    arr = [char for char in string]

    n = len(string)
    i = 0
    j = n - 1

    while i <= j:
        if arr[i] == ' ':
            i += 1

        if arr[j] == ' ':
            j -= 1

        if arr[i] != ' ' and arr[j] != ' ':
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    print("".join(arr))


if __name__ == '__main__':
    string = input()
    # reverse_inplace(string)
    reverse_with_spaces_intact(string)

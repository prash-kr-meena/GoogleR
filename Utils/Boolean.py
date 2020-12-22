def print_small_boolean(boolean: bool) -> None:
    if boolean is True:
        print("true")
    elif boolean is False:
        print("false")
    else:
        print("Not Boolean")


if __name__ == '__main__':
    print_small_boolean(True)
    print_small_boolean(False)
    print_small_boolean("False")

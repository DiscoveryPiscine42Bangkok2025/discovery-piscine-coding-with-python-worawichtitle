"""cell05/ex01"""
def main():
    """print array + 2"""
    array = [2, 8, 9, 48, 8, 22,-12, 2]
    new_array = [i + 2 for i in array]
    print("Original array: ", array)
    print("New array", new_array)
main()
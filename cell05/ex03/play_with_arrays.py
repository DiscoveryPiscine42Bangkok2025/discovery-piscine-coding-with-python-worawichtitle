"""cell05/ex03"""
def main():
    """print array + 2 when value > 5 no duplicate"""
    array = [2, 8, 9, 48, 8, 22,-12, 2]
    nodupe_array = list(set(array))
    new_array = [i + 2 for i in nodupe_array if i > 5]
    print("Original array: ", array)
    print("New array", new_array)
main()
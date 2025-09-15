"""cell04/ex03"""
def main(number):
    """check type float"""
    # if not number.is_integer():
    if number % 1 != 0:
        print("This number is a decimal.")
    else:
        print("This number is an integer.")
main(float(input("Give me a number: ")))
"""cell02/ex01"""
def main(number):
    """is it negative positive or both?"""
    if number == 0:
        print("This number is both positive and negative.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is positive.")
main(int(input()))
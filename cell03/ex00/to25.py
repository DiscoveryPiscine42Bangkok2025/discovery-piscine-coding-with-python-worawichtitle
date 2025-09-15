"""cell03/ex00"""
def main():
    """loop till 25"""
    print("Enter a number less than 25")
    number = int(input())
    if number > 25:
        print("Error")
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1
main()
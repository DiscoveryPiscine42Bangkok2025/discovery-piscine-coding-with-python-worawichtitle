"""cell03/ex01"""
def main():
    """loop multiplication table"""
    print("Enter a number")
    number = int(input())
    for i in range(0, 10):
        print(f"{i} x {number} = {number * i}")
main()
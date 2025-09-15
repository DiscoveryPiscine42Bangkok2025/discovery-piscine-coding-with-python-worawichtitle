"""cell04/ex01"""
def main(age):
    """age in 10, 20, 30 years"""
    print(f"You are currently {age} years old.")
    for year in [10, 20, 30]:
        print(f"In {year} years, you'll be {age + year} years old.")
main(int(input("Please tell me your age: ")))
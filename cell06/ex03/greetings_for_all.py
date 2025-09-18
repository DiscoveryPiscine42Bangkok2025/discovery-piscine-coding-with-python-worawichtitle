"""cell06/ex03"""
def greetings(name):
    """print greetings"""
    if not name:
        name = "noble stranger"
    if name.isnumeric():
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

def main():
    """call method greetings"""
    name = str(input())
    greetings(name)
main()
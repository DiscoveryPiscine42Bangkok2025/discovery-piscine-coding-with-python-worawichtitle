"""cell05/ex06"""
def main(word):
    """make word uppercase"""
    if word:
        print(word.upper())
    else:
        print("none")
main(str(input()))
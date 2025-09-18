"""cell06/ex01"""
def upcase_it(text):
    """turn text to uppercase"""
    return text.upper()

def main():
    """call method upcase_it"""
    input_text = str(input())
    print(upcase_it(input_text))
main()
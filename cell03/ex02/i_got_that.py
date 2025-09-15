"""cell03/ex02"""
def main():
    """say STOP or I don't stop"""
    word = str(input("What you gotta say? : "))
    while True:
        word = str(input("I got that! Anything else? : "))
        if word == "STOP":
            break
main()
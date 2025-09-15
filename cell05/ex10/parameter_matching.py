"""cell05/ex10"""
def main(para_input):
    """check if parameters match"""
    if not para_input:
        print("none")
    else:
        text_input = str(input("What was the parameter? "))
        if para_input == text_input:
            print("Good job!")
        else:
            print("Nope, sorry...")
main(str(input()))
"""cell01/ex03"""
def main():
    """print name but input"""
    first_name = str(input("Hey, what's your first name? : "))
    last_name = str(input("And your last name? : "))
    whole_name = first_name + " " + last_name
    print(f"Well, pleased to meet you, {whole_name}")
main()
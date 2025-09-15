"""cell05/ex08"""
def main(para_input):
    """print reverse parameters"""
    para = [str(i.strip('"')) for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"
    if len(para) >= 2:
        for i in reversed(para):
            print(i)
    else:
        print("none")
main(str(input()))
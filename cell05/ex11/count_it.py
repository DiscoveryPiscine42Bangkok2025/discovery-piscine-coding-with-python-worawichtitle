"""cell05/ex11"""
def main(para_input):
    """count parameters and lenght of parameters"""
    para = [str(i.strip('"')) for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"
    if para[0]:
        print("parameters:", len(para))
        for i in para:
            print(f"{i}: {len(i)}")
    else:
        print("none")
main(str(input()))
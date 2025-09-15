"""cell05/ex13"""
def main(para_input):
    """add 'ism' to parameters"""
    para = [str(i.strip('"')) for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"
    if para[0]:
        for i in para:
            if not i.endswith("ism"):
                print(f"{i}ism")
    else:
        print("none")
main(str(input()))
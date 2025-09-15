"""cell05/ex05"""
def main(para_input):
    """print first parameters"""
    para = [str(i.strip('"')) for i in para_input.split('" "')] # "Code Ninja" "Python" "Sad"
    if para[0]:
        print(para[0])
    else:
        print("none")
    # อีกวิธีเขียน # print(para[0] if para[0] else "none")
main(str(input()))
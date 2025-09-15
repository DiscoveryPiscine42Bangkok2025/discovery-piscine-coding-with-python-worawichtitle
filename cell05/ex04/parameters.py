"""cell05/ex04"""
def main(para_input):
    """count parameters"""
    para = [str(i.strip('"')) for i in para_input.split('" "')]
    print("Number of parameters: ", len(para) if para[0] else 0)
main(str(input()))
"""cell05/ex12"""
def main(para_input):
    """print z if parameters have it"""
    count_z = para_input.count('z')
    if count_z:
        print("z" * count_z)
    else:
        print("none")
main(str(input()))
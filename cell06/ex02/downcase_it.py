"""cell06/ex02"""
def downcase_it(text):
    """turn array to lowercase"""
    array = [i.lower().strip('"') for i in text.split('" "')]
    return array

def main():
    """call method downcase_it"""
    input_text = str(input())
    if input_text:
        for i in downcase_it(input_text):
            print(i)
    else:
        print("none")
main()
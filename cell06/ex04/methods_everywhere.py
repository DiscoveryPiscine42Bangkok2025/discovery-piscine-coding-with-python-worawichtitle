"""cell06/ex04"""
def shrink(text):
    """shrink text to 8 letters"""
    shrinked = text[:8]
    return shrinked

def enlarge(text):
    """enlarge text to 8 letters with 'Z' """
    enlarged = text.ljust(8, 'Z')

    return enlarged

def main(input_text):
    """print text with 8 letters call method shrink, enlarge"""
    if not input_text:
        print("none")
    else:
        array = [para.strip('"') for para in input_text.split('" "')]
        for text in array:
            if len(text) > 8:
                result = shrink(text)
            elif len(text) < 8:
                result = enlarge(text)
            else:
                result = text
            print(result)
main(str(input()))
"""cell05/ex07"""
def main(word):
    """make word downcase"""
    if word:
        print(word.lower())
    else:
        print("none")
main(str(input()))
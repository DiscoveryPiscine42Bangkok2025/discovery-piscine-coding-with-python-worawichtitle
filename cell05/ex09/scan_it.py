"""cell05/ex09"""
import re

def main(key, text):
    """find word in parameters"""
    found = len(re.findall(key, text))
    print(found)
    if found:
        print(found)
    else:
        print("none")
main(str(input()), str(input()))
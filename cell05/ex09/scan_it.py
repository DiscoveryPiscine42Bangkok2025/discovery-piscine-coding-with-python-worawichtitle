"""cell05/ex09"""
import re

def main(key, text):
    """find word in parameters"""
    found = len(re.findall(key, text))
    if found:
        print(found)
    else:
        print("none")
main(str(input()), str(input()))
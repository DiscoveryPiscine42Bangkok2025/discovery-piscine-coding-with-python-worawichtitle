"""cell07/ex01"""
def find_the_redheads(family):
    """find red hair"""
    array = [name for name, hair in family.items() if hair == "red"]
    return array

def main():
    """family dict"""
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    red_hair = find_the_redheads(dupont_family)
    print(red_hair)
main()
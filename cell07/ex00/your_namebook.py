"""cell07/ex00"""
def array_of_names(person):
    """Capitalize first and last name"""
    array = [f"{first.capitalize()} {last.capitalize()}" for first, last in person.items()]
    return array

def main():
    """person dict"""
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    cap_person = array_of_names(persons)
    print(cap_person)
main()
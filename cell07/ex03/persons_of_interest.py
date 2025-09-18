"""cell07/ex03"""
def famous_births(women_scientists):
    """sort by date of birth"""
    women = list(women_scientists.values())
    men = women[0]["name"]
    print(men)
    # sorted_scientists = sorted(women_scientists.values(), key=lambda x: int(x["date_of_birth"]))

    # Display the sorted list
    # for scientist in sorted_scientists:
        # print(f"{scientist['name']} is a great scientist born in {scientist['date_of_birth']}.")


def main():
    """women scientists dict"""
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)
main()
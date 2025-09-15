"""cell03/ex03"""
def main():
    """0 to 10 multiplication table"""
    for main_num in range(0, 11):
        print(f"Table de {main_num}:", end="")
        for sub_num in range(0, 11):
            print(f" {main_num * sub_num}", end="")
        print()
main()
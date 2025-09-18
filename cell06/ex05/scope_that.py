"""cell06/ex05"""
def add_one(value):
    """+1"""
    return value + 1

def main():
    """call before after add 1"""
    before = 10
    print("Before Add one:", before)
    after = add_one(before)
    print("After Add one:", after)
main()
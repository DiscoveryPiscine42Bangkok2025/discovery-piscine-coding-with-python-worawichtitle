"""cell02/ex02"""
def main(enter):
    """enter password"""
    password = "password123"
    if enter ==  password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
main(str(input()))
"""cell05/ex14"""
def main(startnum, endnum):
    """add value between parameters"""
    if startnum and endnum:
        startnum, endnum = int(startnum), int(endnum)
        step = 1 if startnum < endnum else -1
        print(list(range(startnum, endnum + step, step)))
    else:
        print("none")
main(input(), input())
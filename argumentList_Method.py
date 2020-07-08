def main():
    x = ('Rajeev', 'kumar', 'das')
    printArguments(*x)
def printArguments(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("couldn't find name")
if __name__=="__main__":
    main()

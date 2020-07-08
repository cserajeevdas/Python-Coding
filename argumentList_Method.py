def main():
    printArguments('Rajeev', 'kumar', 'das')
def printArguments(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("couldn't find name")
if __name__=="__main__":
    main()

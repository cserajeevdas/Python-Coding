def main():
    #file write
    #f = open("D:\MyWork\python_code\samplefile.txt", "w+")
    #file append
    
    # f = open("D:\MyWork\python_code\samplefile.txt", "a")
    # for i in range(10)    :
        # f.write("this is line"+ str(i)+ "\r\n")
        #print("this is line"+ str(i)+ "\r\n")
    # f.close()

    #file read
    f = open("D:\MyWork\python_code\samplefile.txt", "r")
    if f.mode == 'r':
        # contents = f.read()
        fl=f.readlines()
        for x in fl:
            print(x)
       # print(contents)
    f.close()
if __name__=="__main__":
    main()
    

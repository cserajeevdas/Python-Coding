#assigned a method to a variable and called the method
# def f1():
#     print("in f1")
# x = f1        
# x()

#calling f2 from the rturn value of f1
# def f1():
#     def f2():
#         print("in f2")
#     return f2

# x = f1()        
# x()

#calling the nested method through passed method
# def f1(f):
#     def f2():
#         print("before function call")
#         f()
#         print("after function call")
#     return f2

# def f3():
#     print("this is f3")

# x = f1(f3)
# x()

#creating the decorator function
def f1(f):
    def f2():
        print("before function call")
        f()
        print("after function call")
    return f2
@f1
def f3():
    print("this is f3")

f3()





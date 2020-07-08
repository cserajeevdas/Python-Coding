#####################################################################################################
#list contains comma separated values within square brackers [] .List is mutable i.e we can modify the list.
#sampleList = [1,2,3,4,5]

#Tuple contains comma separated values with parenthesis () . its immutable i.e we can't modify it
#sampleTuple = (14,5,6,7,8)

#Dictionaary contains key-value pairs within curly brackets {}.
# sampleDict ={"a":1, "b":2, "z":4}

#Set contains unique values within curly brackets {}.
#sampleSet = {4,5,6,1,4,8}
#####################################################################################################

#Dictionary program 
# key =""
# def main():
#     states  = {"Banaglore":"KA", "Pune": "MH", "Delhi": "DH", "Chennai":"TN" }
#     print_states(states)
#     global key
#     key=input("enter city name:")
#search in the entire dictionary
#     if key in states:
#         print(f"{key} exists in dictionary")
#     else:
#          print(f"{key} doesn't exist in dictionary")

# def print_states(obj):
#     for x in obj:
#         print(f"{x}: {obj[x]}")
# if __name__ == "__main__":
#     main()

#####################################################################################################

#The alternative of conventional dictionary is the dict keyword
def main():
    states  = dict(Bangalore="KA", Pune="MH", Delhi="DH", Chennai="TN")
    print_states(states)
    #can iterate thorugh keys using keys()
    print("=======Dict Keys=======")
    for k in states.keys(): print(k)
    #can iterate thorugh values using values()
    print("=======Dict values======")
    for v in states.values(): print(v)
    #you can use subscript operator to access a particular element in map.
    #if the key doesn't exist, it give key error, To avoid that use get method
    print("value is", states.get("Bangalore"))

#can use key, value and iterate in the dictionary items to print the values
def print_states(obj):
    for k, v  in obj.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
#####################################################################################################


#pause 2
# print(type("HELLO WORLD")) #string str
# print(type(123)) #integer int
# print(type(3.14)) #float
# print(type(True)) #boolean

#print("Number of letters in your name: " + str(len(input("Enter your name"))))

# TypeError: can only concatenate str (not "int") to str - IMPORTANT
name_answer = input(str("Enter your name"))
name_length = str(len(name_answer))
print("Number of letters in your name: " + name_length + "!!")



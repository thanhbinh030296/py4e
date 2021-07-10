def read_number():
    txt_input = input("\nEnter a number: ")
    return txt_input

#print("hihi ",get_right())
list_input = []
valid = 0
while valid == 0:
    try:
        txt_input = read_number()
        if (txt_input == "done"):
            valid = 1
        else:
            list_input.append(float(txt_input))
    except:
        print("\nInvalid input")
print("\nAll list: \n", list_input)
print("\ntotal ",sum(list_input))
print("\ncount: ",len(list_input), " avarage: ",sum(list_input)/len(list_input))
#Exercise 2 
print("\nmaximum: ",max(list_input), " min: ",min(list_input))
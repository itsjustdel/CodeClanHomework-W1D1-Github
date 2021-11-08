#declare a string
my_first_string = "Hello World"
# declare a second string
my_second_string = "Goodbye World"
# declare an integer
my_int = 1234
# declare a float
my_float = 1.234
# and a boolean
my_bool = True

# add/concatenate strings together and count how long they are
number_of_characters_in_both_strings = len(my_first_string) + len(my_second_string)
# show in terminal
print(number_of_characters_in_both_strings)

# add our character length variable to the integer created at the top
# and save in variable "new_addition"
new_addition = number_of_characters_in_both_strings + my_int

# show with descriptive text, note that we need to cast the integer to a string 
# if we are printing together with a string
print("Our new addition = " + str(new_addition))

# if we print new_addition on its own, python can handle it 
print(new_addition)

# adding ints and floats will default the class type to float
what_type = my_int + my_float
print(type(what_type)) # will output <class 'float'>



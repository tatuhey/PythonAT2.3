# Raihan Khalil Abdillah, 30065695
# AT2.3 Question 1
# If Else Statements

print("Enter a body temperature in Celsius: ", end="")      # receive input from user
temperature = float(input())        # converts input to float datatype

if 37 <= temperature < 38:
    print("Normal Body Temperature")
elif 38 <= temperature < 39:
    print("Is a fever")
elif 39 <= temperature < 40:
    print("Is a high fever")
elif 40 <= temperature < 41:
    print("Is a very high fever")
elif 41 <= temperature < 44:        # https://en.wikipedia.org/wiki/Human_body_temperature#:~:text=44%20%C2%B0C%20(111.2%20%C2%B0,%2C%20continuous%20convulsions%2C%20and%20shock.
    print("Is a serious emergency")
else:
    print("Invalid temperature")    # temperature less than 37c or higher than 44c will output invalid temp

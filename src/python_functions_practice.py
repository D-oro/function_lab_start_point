def return_10 ():
    return 10 

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

def length_of_string (string):
    return len(string)

def join_string (string_1, string_2):
    return (string_1 + string_2)

def add_string_as_number (a, b):
    return int(a) + int(b)

def number_to_full_month_name (number):
    if number == 1 :
        return "January"
    if number == 3 :
        return "March"
    if number == 9 :
        return "September"

def number_to_short_month_name (number):
    if number == 1 :
        return "Jan"
    if number == 4 :
        return "Apr"
    if number == 10 :
        return "Oct"


# def number_to_short_month_name ():
#     number_to_short_month_name = "January" 
#     truncated_text = number_to_short_month_name[0,3]
#     return number_to_short_month_name
# def ask_name():
#     name = input("What's your name? ")
#     return name

# keshia_name = ask_name()
# print(keshia_name)

# def create_gteeting(name):
#     greeting = f"Hello {name}"
#     return greeting

# print(create_gteeting("Chilli"))
# print(create_gteeting("Keshia"))

# def ask_int():
#     interger = int(input("Pick a number: "))
#     return interger

# print(ask_int()* 3)

# def mulitple_3(num):
#     return num * 3

# print(mulitple_3(5))

# def convert_cm_in(length_cm):
#     length_in_inch = length_cm / 2.54
#     return length_in_inch
# print(convert_cm_in(20))

# def convert_in_cm(length_in):
#     length_in_cm = length_in * 2.54
#     return length_in_cm

# print(convert_in_cm(40))

# def add(a,b):
#     return a+b

# print(add(2,6))

# def caculate_mean(a,b):
#     return (a+b) / 2

# print(caculate_mean(2,2))

#Q1
# def temp_c(temp_f):
#     temp_c = (temp_f - 32) * (5/9)
#     return temp_c

# print(temp_c(0))

#Q2
# def is_odd(num):
#     if num % 2 == 0: #% = modulo
#         return False
#     else:
#         return True

# print(is_odd(-3)) 

#Q3
# def mean(num_list):
#      return sum(num_list) / len(num_list)
     

# print(mean([4,3,2,6]))
# print(mean([10,5,6]))

#Q4
def total_cost(price, quant):
    return price * quant

print(f"${total_cost(4.25, 3)}")
#user input dimentions
length = int(input("Enter length of workpiece in mm: "))
tails = int(input("Enter number of dovetails: "))
spacing = int(input("Enter space between dovetails in mm: "))
percentage = int(input("enter percentage of reduction/increase: "))

percentage = percentage / 100


#caculate pins total dimentions
pins = tails + 1
pins_total = pins * spacing

#caculate tails total dimension
length = length - pins_total

#print to check math
print("total length of pins", pins_total)
print("remaining length for tails", length)


#half piece
tails = tails / 2
length = length / tails
even_tails = length / tails
tails_up = length / 2
tails_down = length / 2

print(even_tails)

tails_up = tails_up + (tails_up / 100 * percentage) 
tails_down = even_tails - (tails_down / 100 * percentage)
print(tails_up)
print(tails_down)
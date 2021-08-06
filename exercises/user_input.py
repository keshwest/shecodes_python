#user input dimentions
length = int(input("Enter length of workpiece in mm: "))
tails = int(input("Enter number of dovetails: "))
spacing = int(input("Enter space between dovetails in mm: "))
percentage = int(input("enter percentage of reduction/increase: "))

#caculate pins total dimentions
pins = tails + 1
pins_total = pins * spacing

#caculate tails total dimension
length = length - pins_total

#print to check math
print("total length of pins", pins_total)
print("remaining length for tails", length)

even_tails = length / tails
tails_up = even_tails
tails_down = even_tails

print(even_tails)
tails = tails - 2 

while tails > 2:
    tails = tails - 4
    tails_up = tails_up + ((tails_up / 100 * percentage) * 2)
    tails_down = tails_down - ((tails_down / 100 * percentage) * 2)
    print(tails_up)
    print(tails_down)
    
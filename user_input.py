length = input ("Enter length of workpiece in mm:")
tails = input ("Enter number of dovetails:")
spacing = input ("Enter space between dovetails in mm:")

pins = tails + 2

pins_total = pins * spacing

print(pins_total)
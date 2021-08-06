import csv

# with open("colours_20_simple.csv", mode="r") as csv_file:
#      csv_reader = csv.reader(csv_file, delimiter=",")
#      for line in csv_reader:
# #       print(f"{line[0]} {line[1]} {line[2]}") 

# list = []
# with open("colours_20_simple.csv", mode="r") as csv_file:
#      csv_reader = csv.reader(csv_file, delimiter=",")
#      for line in csv_reader:
#         list.append(line)
# list.pop(0)
# for line in list:
#     print(f"{line[2]} Hex: {line[1]} RGB: {line[0]}")
##        print(f"{line[2]} {line[0]} {line[1]}")

data = []
count = 0
with open("colours_20_simple.csv", mode="r") as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=",")
     for line in csv_reader:
         data.append(line)

for colour in data:
    if "yellow" in colour[2]:
        count += 1
print(f"Yellow:{count}") 
import csv

data = []
file = ""
# file = input("Enter file name: ")
if (file == ""):
    file = "HackUTD-2023-HomeBuyerInfo.csv"
with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    rowIndex = 0
    for row in spamreader:
        if (rowIndex != 0):
            data.append((row[0]).split(','))
        else:
            rowIndex += 1

print(data[0])
print(type(data[0][0]))
    
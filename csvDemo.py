import csv
with open('utilities\loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    #print(csvReader)
    #print(list(csvReader))
    name = []
    status = []
    for row in csvReader:
        name.append((row[0]))
        status.append(row[1])

print(name)
print(status)
index = name.index('Jim')
loanstatus = status[index]
print("loanstatus is "+loanstatus)

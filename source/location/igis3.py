import csv
x = 12.9058293
y = 77.5783209
ayoo = str(radius)
r=float(ayoo)
rad = float(r/111)
a = float(x + rad)
b = float(y + rad)
c = float(x - rad)
d = float(y - rad)

with open('findlocation\out.csv','w') as outputFile:

    with open('c_igis.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
           #c = 0
        for row in csv_reader:
            if row[1] == "" or row[1]=="Latitude": 
                continue
            i = float(row[1])
            j = float(row[2])
            if i <= a and i >= c:
                if j <= b and j >= d:
                    if j-i >= y-a and j-i <= y-c:
                        print(row)
                        outputFile.write(str(row[0])+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[13]+"\n")


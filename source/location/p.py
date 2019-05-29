# Python code to create a file
import csv
import sys
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors 
def geek(radius,curloc,r1,r2,r3,r4,r5,r6,r7,r8):
    file = open('geek.txt','w') 
    file.write("This is the write command") 
    file.write("It allows us to write in a particular file") 
    file.close()
    city=str(curloc)
    ayoo = str(radius)
    r=float(ayoo)
    rad = float(r/111) 
    with open('findlocation\out.csv','w') as outputFile:
	    with open('c_igis.csv') as csv_file:
		    csv_reader = csv.reader(csv_file, delimiter=',')
		    for xy in csv_reader:
			    if str(xy[0]).lower() == city.lower():
				    x= float(xy[1])
				    y= float(xy[2])

		    a = float(x + rad)
		    b = float(y + rad)
		    c = float(x - rad)
		    d = float(y - rad)
	    with open('c_igis.csv') as csv_file:
		    csv_reader = csv.reader(csv_file, delimiter=',')
		    for row in csv_reader:
			    if row[1] == "" or row[1]=="Latitude":
				    continue
			    i = float(row[1])
			    j = float(row[2])
			    print(i,j)
			    if i <= a and i >= c:
				    if j <= b and j >= d:
					    if j-i >= y-a and j-i <= y-c:
						    print(row)
						    outputFile.write(str(row[0])+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[13]+"\n")
	igis=pd.read_csv(r"findlocation\\out.csv")
	igis.columns=['City','Landmark','House of Worship','Pilgrimage','Archaeological Site','Shoreline','Waterside','Woods','Hill Station','Urban Area','State']
	igis.head()

	t=[ 3,  0,  0,  0,  0, 28,  0, 40]

	x=igis.ix[:,(2,3,4,5,6,7,8,9)].values
	x[0:10]

	nbrs=NearestNeighbors(n_neighbors=5).fit(x)

	print(nbrs.kneighbors([t]))
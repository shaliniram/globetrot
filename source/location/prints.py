# Python code to create a file
import csv
import sys
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors 
from . import knn
import matplotlib.pyplot as plt #apri
from apyori import apriori #apri
import numpy as np #apri
def geek(radius,curloc,r1,r2,r3,r4,r5,r6,r7,r8):
	file = open('geek.txt','w') 
	file.write("This is the write command") 
	file.write("It allows us to write in a particular file") 
	file.close() 
	city= str(curloc)
	ayoo = str(radius)
	r=float(ayoo)
	rad = float(r/111)
	
	with open('out.csv','w') as outputFile:

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
	
	#geek2(r1,r2,r3,r4,r5,r6,r7,r8)
	igis=pd.read_csv(r"out.csv")
	igis.columns=['City','Landmark','House of Worship','Pilgrimage','Archaeological Site','Shoreline','Waterside','Woods','Hill Station','Urban Area','State']
	igis.head()

	t=[ r1,  r2,  r3,  r4,  r5, r6,  r7, r8]

	x=igis.iloc[:,[2,3,4,5,6,7,8,9]].values
	x[0:10]

	nbrs=NearestNeighbors(n_neighbors=5).fit(x)
	
	print(nbrs.kneighbors([t])[1])
	val,res = nbrs.kneighbors([t])
	s = pd.Series(igis['City'])
	city_list =[]
	for item in res:
		city_list.append(str(s[item[0]]).lower())
		city_list.append(str(s[item[1]]).lower())
		city_list.append(str(s[item[2]]).lower())
		city_list.append(str(s[item[3]]).lower())
		city_list.append(str(s[item[4]]).lower())
	
	print(city_list)
	return city_list

def apr(location):
	city = location
	c=0
	with open('out1.csv','w') as outputFile:
		with open('c_igis_a.csv', 'r') as csvFile:
			reader = csv.reader(csvFile)
			for row in reader:
				for x in row:
					if x.lower()==city.lower():
						c+=1
						outputFile.write(str(row)+"\n")
						break
	print(c)
	csvFile.close()
	outputFile.close()    




	a_igis = pd.read_csv(r"C:\\Users\\chandha\\shallll\\final_ayoo\\source\\out1.csv", header = None)
	a_igis.head()


	x=c
	records = []
	for i in range(0,x):
		records.append([str(a_igis.values[i,j]) for j in range(0,11)])

	assoc_rules = apriori(records, min_support =(2/x), min_confidence = 0.2, min_lift = 1, min_length = 2)
	assoc_results = list(assoc_rules)
	list_=[]

	for item in assoc_results: 
		pair = item[0]
		items = [x for x in pair]
		print("Rule: " + str(items) )
		print("Support: " + str(item[1]))
		print("Confidence: " + str(item[2][0][2]))
		print("Lift: " + str(item[2][0][3]))
		print("==================================================")
	xx=[]
	for item in assoc_results:
		for x in item[0]:
			if x not in xx:
				xx.append(x)
				print(x)
	return xx
#   for item in assoc_results:
#       for x in item[0]:
#           if x.lower()!=location.lower():
#               print(x)

	#print(list_)

	#for m in list_:
	#   for n in m:
	#       if str(n)==str(location):
	#           print(n)
		


#json to csv  create by Tatsunobu!
import csv
import json
import sys 

def repalcestringwithspaces(str):
	before = [":" , "}" , "{" ,"'"]
	after  = ["," , ""  ,  "" , ""]
	for num in range(len(before)): 
		str = str.replace(before[num],after[num]) 
	return str
def getdata(listdata,finder):
	lists=[i for i, x in enumerate(listdata) if x == finder]
	for num in range(len(lists)):
		lists[num] += 1
	return lists

args = sys.argv

f = open(args[1], 'r')
json_dict = json.load(f) 
json_dict =	str(json_dict)
json_dict = repalcestringwithspaces(json_dict) 
l = json_dict.split(",")
f.close()

f = open(args[2], 'a')
writer = csv.writer(f, lineterminator='\n')
data  = getdata(l,' uupdatedAt')
data2 = getdata(l,' uaccX')
data3 = getdata(l,' uaccY')
data4 = getdata(l,' ulongitude')
data5 = getdata(l,' ulatitude')
title = ["updatedAt","accX","accY","longitude","latitude"] 
writer.writerow(title)
for num in range(len(data)):
	#print(l[data[num]])
	lists=list(l[data[num]])
   	lists2=list(l[data2[num]])
	lists3=list(l[data3[num]])
	lists4=list(l[data4[num]])
	lists5=list(l[data5[num]])
	del lists[0]
	del lists2[0]
	del lists3[0]
	del lists4[0]
	del lists5[0]
	lists = ''.join(lists).split(',')
	lists2 = ''.join(lists2).split(',')
	lists3 = ''.join(lists3).split(',')
	lists4 = ''.join(lists4).split(',')
	lists5 = ''.join(lists5).split(',')
	latlonlist = lists+lists2+lists3+lists4+lists5
	writer.writerow(latlonlist)
print("finish!")
f.close()
#lnglat to utm : create by Tatsunobu!
# -*- coding: utf-8 -*-

from pyproj import Proj
import sys
import csv

def main():
	args = sys.argv
	if(args[1]=="-help"):
		print "    python [filename] [readingdata] [zone]"
		print "ex) python lnglat_to_utm.py test.csv 52"
		print ""
		print "---csv file format---"
		print "lat,lng"
		print "  .   "
		print "  .   "
		print "  .   "
		sys.exit()

	print "------------------------------------------------------------------"
        #WGS84:アメリカで使用されている世界測地系→UTMのコンバータを生成
	convertor = Proj(proj='utm', zone=args[2], ellps='WGS84')
	with open(args[1], 'r') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',',quotechar='"') 
   		for row in csv_reader:
			row[0] = row[0].replace('\xef\xbb\xbf', '')
			print "lat:"+ row[0] + " lng:" + row[1] 
			x, y = convertor(float(row[1]),float(row[0]))
			print "zone:"+ args[2] 
			print "X = %f" % x
			print "Y = %f" % y
			print "------------------------------------------------------------------"

if __name__ == '__main__':
    main()

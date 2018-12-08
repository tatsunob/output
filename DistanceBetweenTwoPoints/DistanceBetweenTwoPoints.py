#DistanceBetweenTwoPoints : create by Tatsunobu!
# -*- coding: utf-8 -*-

#●二地点の緯度経度の距離を計算して表示するプログラム●
#----------------------------------------------------
#実行の仕方
#python DistanceBetweenTwoPoints.py filename.csv
#第一引数:このスクリプトの名前
#第二引数:読み込む緯度経度ファイル名を指定
#「filename.csv」には以下の形式のファイルを用意する
#緯度A,経度A,緯度B,経度B
#緯度C,経度C,緯度D,経度D
#          ・
#		   ・
#		　 ・
#----------------------------------------------------

import math
import sys
import csv


#球面三角法により、大円距離(メートル)を求める
def distance(lat1,lng1,lat2,lng2):

    #緯度経度をラジアンに変換
    rlat1 = lat1 * math.pi / 180
    rlng1 = lng1 * math.pi / 180
    rlat2 = lat2 * math.pi / 180
    rlng2 = lng2 * math.pi / 180

    #2点の中心角(ラジアン)を求める
    a = math.sin(rlat1) * math.sin(rlat2) + math.cos(rlat1) * math.cos(rlat2) * math.cos(rlng1 - rlng2)
    rr = math.acos(a)

    #地球赤道半径(メートル)
    earth_radius = 6378140

    #2点間の距離(メートル)
    distance = earth_radius * rr

    return distance;

def main():
	args = sys.argv
	print "------------------------------------------------------------------"
  	with open(args[1], 'r') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',',quotechar='"') 
   		for row in csv_reader:
			row[0] = row[0].replace('\xef\xbb\xbf', '')
			print "latA:"+ row[0] + " lngA:" + row[1]
			print "latB:"+ row[2] + " lngB:" + row[3]
			print ""
			print str(distance(float(row[0]),float(row[1]),float(row[2]),float(row[3])))+" m"
			print "------------------------------------------------------------------"
			

# main関数呼び出し
if __name__ == "__main__":
    main() 

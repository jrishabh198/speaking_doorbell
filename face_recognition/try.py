#!/usr/bin/env python
import sys
import os
import cv2
import mysql.connector
import argparse

# os.chdir('/home/rj/Downloads/openface-master')
# f = open('/home/rj/Downloads/openface-master/myfile3.txt', 'w')
# f.write("hello") 
# f.close()

# import argparse


# cap = cv2.VideoCapture(0)
# ret,frame = cap.read()
# cv2.imwrite('img.jpg',frame)
def inferit():
	os.chdir('/home/rj/Downloads/openface-master')



	var=os.system('./demos/classifier.py infer ./generated-embeddings/classifier.pkl img.png')
		

	

def savit(var):
	os.chdir('/home/rj/Downloads/openface-master')
	frame = cv2.imread('img.png')
	cnx = mysql.connector.connect(user='root', database='mytable', password = 'random1234')
	cursor = cnx.cursor()
	# query = "SELECT * FROM users"
	
	query = "SELECT name,noOfImages FROM users WHERE name = '"+ var+"'"
	
	cursor.execute(query)
	xx = cursor.fetchall()
	print(cursor.rowcount)
	if cursor.rowcount ==0 :
		query = "INSERT INTO users (name,noOfImages) VALUES ('" +var +"',1) "
		cursor.execute(query)
		cursor.execute('commit')
		os.system('mkdir ./training2/'+var)
		os.system('mkdir ./training1/'+var)
		cv2.imwrite('./training2/'+var +'/'+str(1)+'.jpg',frame)
		cv2.imwrite('./training1/'+var +'/'+str(1)+'.jpg',frame)


	else :
		query = "UPDATE users SET noOfImages = noOfImages+1 WHERE name = '"+ var+"'"
		cursor.execute(query)
		cursor.execute('commit')

		# print(xx[0][1])
		os.system('mkdir ./training2/'+var)
		os.system('mkdir ./training1/'+var)
		cv2.imwrite('./training2/'+var +'/'+str(xx[0][1]+1)+'.jpg',frame)
		cv2.imwrite('./training1/'+var +'/'+str(xx[0][1]+1)+'.jpg',frame)


	
	cursor.close()
	cnx.close()
	
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode', help="Mode")
    inferParser = subparsers.add_parser(
        'infer', help='Predict who an image contains from a trained classifier.')
    savitParser = subparsers.add_parser('savit',
                                        help="save the image.")
    
    # print(args)
    savitParser.add_argument('nam', type=str, 
                             help="Input image.")
    args = parser.parse_args()
    if args.mode == 'infer':
        inferit()
    elif args.mode == 'savit':
    	savit(args.nam)
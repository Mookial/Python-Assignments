##zero.python

def count_zero(lst):
	return [x for x in lst if x == 0]

##############################################################

##sphere.python

import math
def volume(r):
	print ("The volume of this sphere is: " ) 
	print (4/3 * math.pi * r**3)

##############################################################

##roots.python

import math
def real_roots(a, b, c):
	root = b**2-4*a*c
	if root == 0:
		print( "The root for this problem is: ", -b / (2 * a) )
	elif root < 0:
		print("There are no REAL roots.")
	elif root > 0:
		print( "The roots for this problem are:", (-b + math.sqrt(root)) / (2 * a), ",", (-b - math.sqrt(root)) / (2 * a) )

##############################################################

##pascal.python

def pascal(n):
	row = [1]
	k = [0]
	for x in range( max(n,0) ):
		print (row)
		row=[l+r for l,r in zip(row+k,k+row)]
	return n>=1

##############################################################

##minMax.python

def minMax(lst):
	list = []
	list.append( min(lst) )
	list.append( max(lst) )
	return list
	
##############################################################
	
##findnumb.python

import math
import re
def findNum():
	min = int(math.sqrt(102030405607080900))
	max = int(math.sqrt(1929394959697989990))
	pattern = re.compile("1\d2\d3\d4\d5\d6\d7\d8\d9\d0")
	for num in range(min, max):
		if pattern.match( str(num * num) ):
			return num
	#The answer is 1389019170 ** 2

# lyft coding challenge
# varun ved
# 9/21/15

from math import sqrt	

'''
Calculate the detour distance between two different rides. Given four latitude / longitude pairs, 
where driver one is traveling from point A to point B and driver two is traveling from point C to point D, 
write a function (in your language of choice) to calculate the shorter of the detour distances the drivers would need to take to pick-up and drop-off the other driver.

Assumptions:
	the path will always be a straight line (our car is an airplane)
	the path that driver 1 will take to get driver 2 is a -> c -> d -> b
	the path that driver 2 will take to get driver 1 is c -> a -> b -> d
	i'm going to assume that all distances traveled will not cross the equator or prime meridian 
'''

#parse the touples into a starting lat/long and ending lat/long for each driver
def calcRides(a,b,c,d):
	#driver one
	driverOneStartLat = a[0]
	driverOneStartLong = a[1]

	driverOneEndLat = b[0]
	driverOneEndLong = b[1]

	#driver two
	driverTwoStartLat = c[0]
	driverTwoStartLong = c[1]

	driverTwoEndLat = d[0]
	driverTwoEndLong = d[1]

	#driver one route
	d1dist = calcLength(driverOneStartLat,driverOneStartLong,driverTwoStartLat,driverTwoStartLong) + calcLength(driverTwoStartLat,driverTwoStartLong,driverTwoEndLat,driverTwoEndLong) + calcLength(driverTwoEndLat,driverTwoEndLong,driverOneEndLat,driverOneEndLong)
	d2dist = calcLength(driverTwoStartLat,driverTwoStartLong,driverOneStartLat,driverOneStartLong) + calcLength(driverOneStartLat,driverOneStartLong,driverOneEndLat,driverOneEndLong) + calcLength(driverOneEndLat,driverOneEndLong,driverTwoEndLat,driverTwoEndLong)


	print('Driver 1: ', d1dist)
	print('Driver 2: ', d2dist)
	if (d1dist < d2dist):

		print ("Driver 1 has a shorter distance")
	else:
		print("Driver 2 has a shorter distance")

def calcLength(startLat,startLong,endLat,endLong):
	#use absolute values for location, makes this easier
	sLat = abs(startLat)
	sLong = abs(startLong)

	eLat = abs(endLat)
	eLong = abs(endLong)

	#base and height calcs for pythagoreon theorem
	base = eLat - sLat
	height = eLong - sLong

	#find length of unkown side, hella math yo
	vectorLen = sqrt(base*base + height*height)
	return vectorLen

#some random values
a = (-31.323,128.34)
b = (-33.323,127.34)
c = (-35.323,119.34)
d = (-29.323,120.34)

calcRides(a,b,c,d)

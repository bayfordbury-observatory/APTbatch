import os
import math
from astropy.io import fits

##-------------------------------------------------------
##--- Variables to be customised

directory = r"C:\Users\David\Documents\apt tests\fortuna"

#The right ascension and declination of your target
RA_target_1 = 129.328754
DEC_target_1 = 16.082509

#Is the target moving? (True or False)
movingTarget = True

#If your target is moving:

#The right ascension and declination of your target at a second point
RA_target_2 = 129.360391
DEC_target_2 = 16.072311

#Julian date at the first and last point
JD_1 = 2458174.5500694443
JD_2 = 2458174.3645023149

#The right ascension and declination of the reference star
RA_reference = 129.439444
DEC_reference = 16.027707

#The right ascension and declination of the check star/s
RA_check_1 = 349.100001
DEC_check_1 = 31.437105

#Coordinates for a second check star (or 'None' if not used)
RA_check_2 = 348.874724
DEC_check_2 = 31.415189

#Maximum distance from expected coordinates for a source to be considered
maxDist = 2

#Name of the output file
listFile = "output_asteroid.csv"


##-------------------------------------------------------

def sortFirst(val): 
    return val[0]  

f= open(listFile,"w")
f.write("Julian Date,Target Intensity,Target Intensity Uncertainty,Target magnitude,target magnitude uncertainty,Reference Intensity,Reference Intensity Uncertainty,Reference magnitude,Reference magnitude uncertainty,Check1 Intensity,Check1 Intensity Uncertainty,Check1 magnitude,Check1 magnitude uncertainty")
if RA_check_2 is None:
	f.write("\n")
else:
	f.write(",Check2 Intensity,Check2 Intensity Uncertainty,Check2 magnitude,Check2 magnitude uncertainty\n")
f.close()

i = 0

list = []

if movingTarget == True:

	raMovement = RA_target_2-RA_target_1
	decMovement = DEC_target_2-DEC_target_1
	timeScale = JD_2-JD_1
	raRate = raMovement/timeScale
	decRate = decMovement/timeScale
	
	print "timeScale "+str(timeScale)+" raRate "+str(raRate)+" raRate "+str(decRate)


#loop through all files in directory
for filename in os.listdir(directory):
	##check it's a fits file
	if filename.endswith(".fit") or filename.endswith(".fits") or filename.endswith(".fts"): 
		
		#full path to file
		file = os.path.join(directory, filename)
		
		print file
		
		#path to source list
		sourceList = os.path.join(directory, os.path.splitext(filename)[0]+".tbl")

		#fits header data unit
		hdul = fits.open(file)

		#get the Julian date
		
		JD = float(hdul[0].header['JD'])	
		
		list.append([JD, 99,"0,0,0,0","0,0,0,0","0,0,0,0","0,0,0,0"])
			
		
		if movingTarget == True:
			#julian date interpolation
			
			timeScale = JD-JD_1
			
			RA_target = RA_target_1 + (raRate*timeScale)
			DEC_target = DEC_target_1 + (decRate*timeScale)
			
			print(str(timeScale)+" "+str(RA_target)+" "+str(DEC_target))
		else:
			RA_target = RA_target_1
			DEC_target = DEC_target_1
			
			
		#initialise some variables	
		lineNum=0

		closestTarget = 99
		closestRef = 99
		closestCheck1 = 99
		closestCheck2 = 99

		#open the source list for reading
		sourceList_in = open(sourceList, "r")
		
		#loop through all lines in the file
		for line in sourceList_in:
		
			#ignore the header lines
			if lineNum >2:
				
				#split the line by white spaces
				parts = line.split()
				
				#ignore the last line
				if parts[0]!="End":
				
					ra = float(parts[3])
					dec = float(parts[4])
					Intensity = parts[10]
					dIntensity = parts[12]
					mag = parts[14]
					dmag = parts[15]
					fwhm = parts[35]
					
					output_string =Intensity+","+dIntensity+","+mag+","+dmag
							
					ra1 = math.radians(RA_target)
					ra2 = math.radians(ra)
					d1 = math.radians(DEC_target)
					d2 = math.radians(dec)			
					
					#calculate the distance from this source to the target
					angSep = 3600*math.degrees(math.acos(math.sin(d1)*math.sin(d2)+math.cos(d1)*math.cos(d2)*math.cos(ra1-ra2)))
										
					if angSep < maxDist and angSep<closestTarget:
						closestTarget = angSep
						list[i][1]=closestTarget
						list[i][2]=output_string
						
					ra1 = math.radians(RA_reference)
					ra2 = math.radians(ra)
					d1 = math.radians(DEC_reference)
					d2 = math.radians(dec)			
					
					#calculate the distance from this source to the reference star
					angSep = 3600*math.degrees(math.acos(math.sin(d1)*math.sin(d2)+math.cos(d1)*math.cos(d2)*math.cos(ra1-ra2)))
										
					if angSep < maxDist and angSep<closestRef:
						closestRef = angSep
						list[i][1]=closestRef
						list[i][3]=output_string	
						
					ra1 = math.radians(RA_check_1)
					ra2 = math.radians(ra)
					d1 = math.radians(DEC_check_1)
					d2 = math.radians(dec)			
					
					#calculate the distance from this source to the check star
					angSep = 3600*math.degrees(math.acos(math.sin(d1)*math.sin(d2)+math.cos(d1)*math.cos(d2)*math.cos(ra1-ra2)))
										
					if angSep < maxDist and angSep<closestCheck1:
						closestCheck1 = angSep
						list[i][1]=closestCheck1
						list[i][4]=output_string	
					
					if RA_check_2 is not None:
						ra1 = math.radians(RA_check_2)
						ra2 = math.radians(ra)
						d1 = math.radians(DEC_check_2)
						d2 = math.radians(dec)			
						
						#calculate the distance from this source to the second check star
						angSep = 3600*math.degrees(math.acos(math.sin(d1)*math.sin(d2)+math.cos(d1)*math.cos(d2)*math.cos(ra1-ra2)))
											
						if angSep < maxDist and angSep<closestCheck2:
							closestCheck2 = angSep
							list[i][1]=closestCheck2
							list[i][5]=output_string	
						
					
						
					
			lineNum=lineNum+1


		sourceList_in.close()
		
		i=i+1
		
#sort by julian date
list.sort(key = sortFirst)  
		
f= open(listFile,"a")			
		
for n in range(i):

	f.write(str(list[n][0])+","+list[n][2]+","+list[n][3]+","+list[n][4])
	if RA_check_2 is None:
		f.write("\n")
	else:
		f.write(","+list[n][5]+"\n")


f.close() 
		
#print list
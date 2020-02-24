##### ----APTbatch.py---#############################################################################
#																									#
# Runs Aperture Photometry Tool (APT) to create a source list for every FITS file in a directory	#
#																									#
#####################################################################################################

import subprocess
import os

#-----------Variables to be customised before use-----------------------------------------------------


#Directory containing the FITS images you want processed
directory = r"C:\Users\David\Documents\apt tests\Transit 1"

#Location of the APT.jar file
aptJar = r"C:\Program Files (x86)\APT\APT.jar" #Uncomment this line and Comment the above line wPMB PCs

#Location of the exported APT preferences file (you must set up the photometry settings in APT first)
preferences = r"C:\Users\David\Documents\apt tests\Transit 1\APT.pref"


#---------------------------------------------------------------------------------------------------



#Loop through files in directory
for filename in os.listdir(directory):

	#Check it's a FITS file
	if filename.endswith(".fit") or filename.endswith(".fits") or filename.endswith(".fts"): 
		
		#Full path to the file
		file = os.path.join(directory, filename)
		
		print(file)
		
		#name of the output table file (source list)
		ofile = os.path.join(directory, os.path.splitext(filename)[0]+".tbl")
	
		#parameters to feed APT
		parameters = "-i \"" + file + "\" -s sourceListByAPT -o \"" + ofile + "\" "
		
		#Call APT
		subprocess.call(["C:/Program Files (x86)/Java/jre1.8.0/bin/java.exe", "-Duser.language=en", "-Duser.region=US", "-mx1024M", "-jar", aptJar, "-i", file, "-p", preferences, "-s", "sourceListByAPT", "-o", ofile])
		
		continue
	else:
		continue


print("Done!")
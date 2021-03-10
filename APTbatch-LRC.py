##### ----APTbatch.py---#############################################################################
#																									#
# Runs Aperture Photometry Tool (APT) to create a source list for every FITS file in a directory	#
# LRC March 2021 Version
#																									#
#####################################################################################################

import subprocess
import os

#-----------Variables to be customised before use-----------------------------------------------------


#Directory containing the FITS images you want processed
directory = r"C:\Users\Public\Documents\Practicals\Exoplanets\HAT-P-20\Transit 1"

#Location of the APT.jar file
aptJar = r"C:\ProgramData\APT_v2.8.3\APT_v2.8.3\APT.jar" #Specific location for APT on LRC machines in March 2021

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
		
		#remove any previous output files to write new data
		if os.path.exists(ofile):
			os.remove(ofile)
	
		#parameters to feed APT
		parameters = "-i \"" + file + "\" -s sourceListByAPT -o \"" + ofile + "\" "
		
		#Call APT (specific batch script on LRC PCs) 		
		subprocess.call(["APT-LRC.bat", "-i", file, "-p", preferences, "-s", "sourceListByAPT", "-o", ofile])
		
		continue
	else:
		continue


print("Done!")

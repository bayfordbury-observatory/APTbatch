import subprocess
import os

directory = r"C:\Users\David\Documents\apt tests\Transit 1"
aptJar = "C:/APT/APT.jar"
preferences = "APT.pref"

for filename in os.listdir(directory):
	if filename.endswith(".fit") or filename.endswith(".fits") or filename.endswith(".fts"): 
		
		file = os.path.join(directory, filename)
		ofile = os.path.join(directory, os.path.splitext(filename)[0]+".tbl")
		
		print(file)
		
		parameters = "-i \"" + file + "\" -s sourceListByAPT -o \"" + ofile + "\" "
		
		subprocess.call(["java", "-Duser.language=en", "-Duser.region=US", "-mx1024M", "-jar", aptJar, "-i", file, "-p", preferences, "-s", "sourceListByAPT", "-o", ofile])
		
		continue
	else:
		continue



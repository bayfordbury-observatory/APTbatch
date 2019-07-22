# APT Batch

APTbatch.py runs Aperture Photometry Tool (APT) automatically to create a source list for every FITS file in a directory

SourceLists.py then extracts specific sources from those APT source lists (a target, reference, and one or two check stars)

It can be used for quickly creating light curves of exoplanet transits, asteroid, variable stars... etc

## APTbatch.py

- You must first run APT on a single image to set up the photometry settings (photometry mode, aperture and sky annulus size)

- Next export these settings as a preference file (File > Preferences > Save Preferences)

Three variables must be edited in the script before use:

- The directory containing your FITS files to be processed

- The location of the APT.jar file (for PMB computers this will be "C:\Program Files (x86)\APT\APT.jar")

- The location of the preferences file you've saved from APT

Now run the script ("python APTbatch.py")

- APT will be run for each image and a corresponding .tbl source list will be created in the image directory

## SourceLists.py

You now have the magnitude of every single source (stars, asteroids..etc) in every image, but in most cases you are only interested in a few sources.
This script will extract only a few chosen sources (a target, reference, and one or two check stars), and output them into a single file with the Julian date.

Several variables must first be changed before running the script:

- The directory containing both the FITS files and .tbl source lists created by APTbatch.py

- The coordinates of the target (in decimal degrees)

- The coordinates of a reference star (pick a bright star nearby for maximum SNR, but ensure it does not saturate - peak pixel value should remain <40k)

- Coordinates of a check star, choose as in the same was as the reference.

- Coordinates of a second check star if desired.

- Maximum permissable distance for a source to be counted as the one you want (1-2 arcseconds is a good range)

- The filename of the output list

If your target is moving (a comet or asteroid) you must also specify 

- A second set of coordinates taken at a later time

- The Julian date of the first and second set of coordinates

Now run the script ("python SourceLists.py") and your photometry data will be extracted into a new file.
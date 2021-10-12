# PCX-Conversion-KAP-BSB
Tools to convert old PCX charts to new KAP/BSB files

for this we will need a few items: 

* something that can read/open/run PYTHON script 

* KONVERTOR (free tool for windows)

* GIMP (is free or other image manipulator) (https://www.gimp.org/)

* IMGKAP (free tool to convert image to KAP) (https://github.com/nohal/imgkap)

* EXEL (for making things simple)

.

for this project your files will probably look like

NAME.A01,
NAME.A02,
NAME.B01,
NAME.B02,
ect 

___

step 1 :

Open the python script 

Run step 1, follow the instructions in the script

___

Step 2 : 

Convert the PCX to PNG with KONVERTOR leaving the png in the original folder

___

Step 3 :

Open the python script 

Run step 3, follow the instructions in the script

___

step 4 :

Open the created image.png in GIMP

4.1(optional) goto > image > mode > indexed > set colors to 16 to 127 (if you want NIGHT colors for map max 64) but i recomend 24(makes file smaller)

4.2 if done 4.1 file > overwrite image.png

___

step 5 :

now move the image to the folder IMGKAP is located (if different)

___

step 6 :

open the EXEL sheet. 

fill in the BLUE tiles: 

* ZONE

* NAME

* SCALE

* Top right LAT, LON + coresponding PIXEL coordinates ( read in GIMP )

* Bottom left LAT, LON + coresponding PIXEL coordinates ( read in GIMP )

* Image size X,Y and DPI (DDI)

.

from the block "KAP FILE FORMAT "

select all the green tiles and CTR + C

___

Step 7 :
go to the folder IMGKAP is and create new .TXT file

open file and PASTE cpied text

DELETE LAST EMPTY ROW <<<<<<<<<<<<<<<<<<<<!!!!!!!

save

go to exel 

copy the text next to "KAP FILE FORMAT" that ends in ".kap"

rename the just made .TXT file with the copied text

___

step 8 (OPTIONAL):

follow steps in step 7 for the "BSB FILE FORMAT "

Programs such as OPENCPN dont need a BSB file, only the kap file 

___

step 9 :

OPEN IMGKAP 

go to exel and copy either one of the green tiles from "IMGKAP copy paste"  

and paste it in the IMGKAP 

automaticly a kap file is created in the same folder that can now be read in navigation program 

___

I am looking to create a DATABASE of old PCX charts and share them. if you have used this and can share the final charts that would be appreciated.
send a email to info@mari-caribbean.com

___

HAVING TROUBLE RUNNING IMGKAP?

open command prompt (start > cmd)

type > "cd URL/imgkapfolder" > enter

now you can paste the text from exel

___

ADVANCED:

For those that want to i find the "white" text on the map a bit dull
open the map KAP file with (https://notepad-plus-plus.org/downloads/) and look for :

RGB/X,0,0,0 see what number is at the X

scroll down to NGT/X  and change the numbers to  ,99,99,99 (the map glitches if more then 99 for some reason)

SAVE

now the white text should be more legible


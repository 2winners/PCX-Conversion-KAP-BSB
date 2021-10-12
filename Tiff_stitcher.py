import numpy as np
from imageio import imread, imwrite
import math
import os
import sys  
# change the PATH to the folder where all the chart folders are found 
path = r"C:\Users\Bastiaan Maijen\Desktop\Belgium and Holland 1"
Bpath = "Blank.png" #the file name of the blank block
chart_foldername = "M" #the common fisrt letter of the map folders


# Step 1:
# Renaming all the files in the folders to have an PCX extencion
# setstep 3 to "False" set step 1 to "True"
RENAME = False 
renameExt = ".PCX"

# Step 2:
# Use KONVERTOR to convert the ".PCX" files to ".png"

# Step 3:
# Stitching together the tiles
# setstep 1 to "False" set step 3 to "True"
STITCH = True
ext = ".png" # File extension
Reconizer = "final" # is used to create the output as "FOLDERNAME + Reconizer.png"

# The output files will appear in the folder this script exists
# If image fails please delete the Failed output image or it will skip when you restart

#_____________________________
#________ SCRIPT PART ________
#_____________________________



path2 = ""          #internal script path
directory_contents = []
Chart_Folders = []
alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M'] # Add more Letters if you find charts with more
numbr =['01','02','03','04','05','06','07','08','09','10','11','12'] #add more numbers if you find charts with more
imlist = []

#checks if Blank Exists
if os.path.isfile(Bpath) == False:
           print(Bpath + "Does not exist, Please place in folder this file exists")
else:           

    directory_contents = os.listdir(path)   # Grabs Folders in PATH
    if directory_contents == False:
        print("No folders found at " + path)
    else:
        for Name in directory_contents:     # Reads the names of the folders
   
            if Name[0] == chart_foldername:
               # print(Name)
                Chart_Folders.append(Name)

        #print(Chart_Folders)
        files = []                          #Temporary storage of the files in the current folder

        if Chart_Folders == False:
            print("No Mapfolders found that start with " + chart_foldername )

        for folder in Chart_Folders:
            path2 = path + '\\' + folder
            files = os.listdir(path + '\\' + folder)    # Fetches the files from the folder
            #print(files)
      
            if RENAME == True:              # Rename script part
                for file in files:
                    if renameExt in file:
                        print (renameExt)
                    else:
                        file = upper(file)
                        new_name = file + renameExt
                        src =  path + '\\' + folder + '\\' + file
                        print(src)
                        dst = path + '\\' + folder + '\\' + new_name
                        print(dst)
                        os.rename(src, dst)        
                files = []                  # clear Files
            if STITCH == True:              # Stitcher script
                if os.path.isfile(folder + Reconizer +".png") == True:        # Checks if the file was already created to not do double work
                    print("Exist " + folder + Reconizer + ".png")
                else:
                    files = os.listdir(path + '\\' + folder)
                    #print(files)
        
                    WIDTH = 0   
                    HEIGHT = 0
                    COUNTER = 0
                    n = 0 
                    for N in numbr:
                        l = 0
                        for L in alpa:
                            NA = folder + "." + alpa[l] + numbr[n] + ext
                            if NA in files:
                                imlist.append(path2 + '\\' + NA )
                                if "."+ L + "01" in NA:
                                    print( NA )
                                    WIDTH += 1
                                    print ("width:" + str(WIDTH))
                            else:
                                    COUNTER += 1
                                    print (NA + " ERROR")
                                    #print("BLANK:" + str(COUNTER))

                            l += 1
            
                        n += 1
                    print(imlist)
                    if imlist:
            
           
        
                        def tile_images(images, cols):
                            # tile images of same size to grid with given number of columns.
    
                            # Args:
                            #    images (collection of ndarrays)
                            #    cols (int): number of colums 
    
                            # Returns:
                            #    ndarray: stitched image
                            images = iter(images)
                            first = True
                            rows = []
                            i = 0
                            shape = imread(Bpath).shape
                            print(shape)
                            while True:
        
                                try:
                                    im = next(images)
                                    if im.shape != shape :              #if Image is not the same shape replace with a blank ( some "PAN ..." blocks have less layers and can not be stitched)
                                        print(f"not same {shape}")
                                        im = imread(Bpath)
                                    print(f"add image, shape: {im.shape}, type: {im.dtype}")
                                except StopIteration:
                                    if first:
                                        break
                                    else:
                                        im = np.zeros_like(im)  # black background
                
                                if first:
                                    row = im  # start next row
                                    dtyp = im.dtype
                                    first = False  
                                else:    
                                    row = np.concatenate((row, im), axis=1)  # append to row
            
                                i += 1
                                if not i % cols:
                                    print(f"row done, shape: {row.shape}")
                                    rows.append(row) # finished row
                                    first = True
            
                            tiled = np.concatenate(rows)   # stitch rows    
                            return tiled        

                        def main():
                            images = (imread(f) for f in imlist) 
                            new = tile_images(images, WIDTH)
                            imwrite(folder + Reconizer + ".png", new)


                        def test():
                            im1 = np.arange(65536).reshape(256,256)
                            im2 = np.arange(65536/2).reshape(128,256)
    
                            images = [im1,im1,im1,im2,im2,im2]
    
                            # works
                            new = tile_images(images, 3)
                            imwrite("new.png", new)
    
                            # failes
                            new = tile_images(images, 2)
                            imwrite("new2.png", new)
    
    
                        if __name__ == "__main__":
                            main()
                            # test()
                        images = []
                        imlist = []
                        files = [] 
        
                        print("________________")
                    else:
                        print("no PNG found")
                        #do something




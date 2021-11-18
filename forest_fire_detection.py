# Title: Forest fire detection
# Created by: Aaron Jutzi
# Date: November 1, 2021
# 
#
# This is a python script for running NDVI, NBR, BAI, and the image difference 
# process tool in ArcGIS Pro. These tools can useful for analyzing forest fires. 
#
# I created this script to practice, develop and demonstrate my python and arcpy skills
#
# Error handling is included although more can still be added (I plan on adding more
# error handling in the future)
#
##



import arcpy

# Set geoprocessing environments
arcpy.env.workspace = str(input("Enter your workspace path: "))
arcpy.env.overwriteOutput = True



# Printing out the rasters within the workspace
rasters = arcpy.ListRasters()

print("")
print("List of rasters in your workspace")
print("")
print("file name")
print("-----------")

for r in rasters:
    print(r)





# User is prompted to choose which raster process they want to use

print("What would you like to do?")
print("")

processes = {'1':"NDVI", '2':"NBR", '3':"BAI", '4':"Difference"}

print(processes)
print("")

# User inputs which process they want to use until they enter a valid number
while True:
    try:
        p = input("Enter the corresponding number: ")
        print("You chose", processes[p])
        break
    except:
        pass

    print("Invalid number, please try again")

print(processes[p])




# Option 1: User chooses NDVI
if p == '1':
    while True:
        try:

            # user enters file name
            r = input("Enter the file name (if within workspace)" + 
            "or full file path of the raster you want the NDVI of:\n")
            
        
            r = arcpy.Raster(r)
            
            
            x = 1

            # print out the raster's band names
            for n in r.bandNames:
                if x == 1:
                    print("Your rasters bands: ")
                    print("(" + str(x) + ")" + " " + n)
                    x += 1
                elif x > 1:
                    print("(" + str(x) + ")" + " " + n)
                    x += 1
                
                
        # Error exception for when user inputs invalid raster file path
        except:
            print("Error. Please enter a valid raster file path")
            continue

        else:
            break

        


            
    # User inputs NIR and Red band number id
    nir = int(input("Enter NIR band number: "))

    red = int(input("Enter Red band number: "))

    # NDVI raster is created
    NDVI_raster = arcpy.sa.NDVI(r, nir, red)
    
    
    name = input("What would you like to name your file?" + 
    "(just the name, no quotations or file extension)\n")



    print('"' + name + '.tif"')


    # NDVI raster is saved
    NDVI_raster.save(str(name) + '.tif')

            



# User chooses NBR
if p == '2':
    while True:
        try:

            # user enters file name
            r = input("Enter the file name (if within workspace)" + 
            "or full file path of the raster you want the NBR of:\n")
            
        
            r = arcpy.Raster(r)
            
            
            x = 1

            # print out the raster's band names
            for n in r.bandNames:
                if x == 1:
                    print("Your rasters bands: ")
                    print("(" + str(x) + ")" + " " + n)
                    x += 1
                elif x > 1:
                    print("(" + str(x) + ")" + " " + n)
                    x += 1
                
                
        # Error exception for when user inputs invalid raster file path
        except:
            print("Error. Please enter a valid raster file path")
            continue

        else:
            break
    
    # user enters swir and nir band numbers        
    swir = int(input("Enter SWIR band number: "))
    nir = int(input("Enter NIR band number: "))

    # nbr raster is created
    NBR_raster = arcpy.sa.NBR(r, swir, nir)
    
    name = input("What would you like to name your file?" + 
    "(just the name, no quotations or file extension)\n")

    # NBR raster is saved
    NBR_raster.save('"' + name + '.tif"')

    break


# User chooses BAI
if p == '3':
    while True:
        try:

            # user enters file name
            r = input("Enter the file name (if within workspace)" + 
            "or full file path of the raster you want the BAI of:\n")
            
        
            r = arcpy.Raster(r)
            
            
            x = 1

            # print out the raster's band names
            for n in r.bandNames:
                if x == 1:
                    print("Your rasters bands: ")
                    print("(" + str(x) + ")" + " " + n)
                    x += 1
                elif x > 1:
                    print("(" + str(x) + ")" + " " + n)
                    x += 1
                
                
        # Error exception for when user inputs invalid raster file path
        except:
            print("Error. Please enter a valid raster file path")
            continue

        else:
            break
        
    # user enters red and nir band numbers
    red = int(input("Enter red band number: "))
    nir = int(input("Enter NIR band number: "))

    # BAI raster is created
    BAI_raster = arcpy.ia.BAI(r, red, nir)
    
    name = input("What would you like to name your file?" + 
    "(just the name, no quotations or file extension)\n")

    # BAI raster is saved
    BAI_raster.save('"' + name + '.tif"')

    break

# User chooses difference
if p == '4':
    while True:

        r1 = input("Enter the file name (if within workspace)" + 
        "or full file path of the first raster to find the difference with:\n")
        
        r1 = arcpy.Raster(r1)

        r2 = input("Enter the file name (if within workspace)" + 
        "or full file path of the second raster to find the difference with:\n")

        r2 = arcpy.Raster(r2)

        diff = arcpy.sa.RasterCalculator([r1, r2], ["x","y"], "x-y")

        name = input("What would you like to name your file?" + 
        "(just the name, no quotations or file extension)\n")

        diff.save('"' + name + '.tif"')
        

        break

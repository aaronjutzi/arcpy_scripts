# Title: Find single and multiband rasters in a workspace
# Created by: Aaron Jutzi
# Date: April, 2021
#
# This script finds the rasters within a workspace and displays
# which rasters are single or multiband



import arcpy

# user inputs path to raster folder
arcpy.env.workspace = str(input("Please enter the file path to your raster folder: "))

rasters = arcpy.ListRasters()

# creating empty lists for one band and multi band rasters
oneBand = []
multiBand = []

# appending rasters accordingly to those lists
for raster in rasters:
    desc = arcpy.Describe(raster)
    if desc.bandCount == 1:
        oneBand.append(raster)
    elif desc.bandCount > 1:
        multiBand.append(raster)

print("The following rasters in the workspace are single band rasters: ")
for raster in oneBand:
    print(raster)

print("The following rasters in the workspace are multiband rasters: ")
for raster in multiBand:
    desc = arcpy.Describe(raster)
    print(raster, " has ", desc.bandCount, "bands")
        

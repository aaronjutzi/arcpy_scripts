# Title: Calculate length of line features
# Created by: Aaron Jutzi
# Date: November 20, 2021
#
# User inputs the file path to a line feature class and then choose
# which unit of measure they want to calculate the length of each feature
#
# This script uses tkinter for displaying a GUI


from tkinter import *
from tkinter.ttk import *

import arcpy


# C:\GIS\Data\digitize_scratch\lines.shp

# setting LENGTH as the geometry variable to be used for all functions 
l = "LENGTH"


def FEET_US():

        arcpy.management.AddGeometryAttributes(fc, l, "FEET_US")
        
        # The created field name here is "LENGTH".
        # This field name does not indicate the unit of measurement.
        # Therefore it is helpful to change the field name to something that indicates the unit
        # of measurement.
        # The alter field tool is one solution but it only works for feature classes in a FGDB.
        # We want a solution that works for files in folders as well.
        # The following solution copies the data from the LENGTH field into a field with a new name and
        # deletes the old "LENGTH" field.

        # The length of the field name cannot be larger than 10 (error 000313 otherwise)
        arcpy.management.AddField(fc, "len_FEET", "DOUBLE")
        arcpy.management.CalculateField(fc, "len_FEET", "!LENGTH!")
        arcpy.management.DeleteField(fc, "LENGTH")
        

        print("Length has been calculated for each feature in your feature class \U0001F642")

def METERS():

        arcpy.management.AddGeometryAttributes(fc, l, "METERS")

        # The created field name here is "LENGTH".
        # This field name does not indicate the unit of measurement.
        # Therefore it is helpful to change the field name to something that indicates the unit
        # of measurement.
        # The alter field tool is one solution but it only works for feature classes in a FGDB.
        # We want a solution that works for files in folders as well.
        # The following solution copies the data from the LENGTH field into a field with a new name and
        # deletes the old "LENGTH" field.

        # The length of the field name cannot be larger than 10 (error 000313 otherwise)
        arcpy.management.AddField(fc, "len_METERS", "DOUBLE")
        arcpy.management.CalculateField(fc, "len_METERS", "!LENGTH!")
        arcpy.management.DeleteField(fc, "LENGTH")
        

        print("Length has been calculated for each feature in your feature class \U0001F642")

def KILOMETERS():

        arcpy.management.AddGeometryAttributes(fc, l, "KILOMETERS")

        # The created field name here is "LENGTH".
        # This field name does not indicate the unit of measurement.
        # Therefore it is helpful to change the field name to something that indicates the unit
        # of measurement.
        # The alter field tool is one solution but it only works for feature classes in a FGDB.
        # We want a solution that works for files in folders as well.
        # The following solution copies the data from the LENGTH field into a field with a new name and
        # deletes the old "LENGTH" field.

        # The length of the field name cannot be larger than 10 (error 000313 otherwise)
        arcpy.management.AddField(fc, "len_KM", "DOUBLE")
        arcpy.management.CalculateField(fc, "len_KM", "!LENGTH!")
        arcpy.management.DeleteField(fc, "LENGTH")
        

        print("Length has been calculated for each feature in your feature class \U0001F642")

def MILES_US():

        arcpy.management.AddGeometryAttributes(fc, l, "MILES_US")

        # The created field name here is "LENGTH".
        # This field name does not indicate the unit of measurement.
        # Therefore it is helpful to change the field name to something that indicates the unit
        # of measurement.
        # The alter field tool is one solution but it only works for feature classes in a FGDB.
        # We want a solution that works for files in folders as well.
        # The following solution copies the data from the LENGTH field into a field with a new name and
        # deletes the old "LENGTH" field.

        # The length of the field name cannot be larger than 10 (error 000313 otherwise)
        arcpy.management.AddField(fc, "len_MILES", "DOUBLE")
        arcpy.management.CalculateField(fc, "len_MILES", "!LENGTH!")
        arcpy.management.DeleteField(fc, "LENGTH")
        

        print("Length has been calculated for each feature in your feature class \U0001F642")

def NAUTICAL_MILES():

        arcpy.management.AddGeometryAttributes(fc, l, "NAUTICAL_MILES")

        # The created field name here is "LENGTH".
        # This field name does not indicate the unit of measurement.
        # Therefore it is helpful to change the field name to something that indicates the unit
        # of measurement.
        # The alter field tool is one solution but it only works for feature classes in a FGDB.
        # We want a solution that works for files in folders as well.
        # The following solution copies the data from the LENGTH field into a field with a new name and
        # deletes the old "LENGTH" field.

        # The length of the field name cannot be larger than 10 (error 000313 otherwise)
        arcpy.management.AddField(fc, "len_NMiles", "DOUBLE")
        arcpy.management.CalculateField(fc, "len_NMILES", "!LENGTH!")
        arcpy.management.DeleteField(fc, "LENGTH")
        

        print("Length has been calculated for each feature in your feature class \U0001F642")


def YARDS():

        arcpy.management.AddGeometryAttributes(fc, l, "YARDS")

        # The created field name here is "LENGTH".
        # This field name does not indicate the unit of measurement.
        # Therefore it is helpful to change the field name to something that indicates the unit
        # of measurement.
        # The alter field tool is one solution but it only works for feature classes in a FGDB.
        # We want a solution that works for files in folders as well.
        # The following solution copies the data from the LENGTH field into a field with a new name and
        # deletes the old "LENGTH" field.

        # The length of the field name cannot be larger than 10 (error 000313 otherwise)
        arcpy.management.AddField(fc, "len_YARDS", "DOUBLE")
        arcpy.management.CalculateField(fc, "len_YARDS", "!LENGTH!")
        arcpy.management.DeleteField(fc, "LENGTH")
        

        print("Length has been calculated for each feature in your feature class \U0001F642")


# Program begins
fc = input("Enter the file path of your target line feature class: ")

print("Feature class fields:")
fields = arcpy.ListFields(fc)

for f in fields:
    print(f.name)


# setting up the Tkinter window
# functions are called whenever the user clicks one of these buttons
root= Tk()
root.title("Calculate length")
label = Label(root, text ="Choose your unit of measurement").pack()
canvas= Canvas(root, width=400, height=200)
button = Button(root, text="FEET_US", command=FEET_US)
button2 = Button(root, text="METERS", command=METERS)
button3 = Button(root, text="KILOMETERS", command=KILOMETERS)
button4 = Button(root, text="MILES_US", command=MILES_US)
button5 = Button(root, text="NAUTICAL_MILES", command=NAUTICAL_MILES)
button6 = Button(root, text="YARDS", command=YARDS)

canvas.pack()
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()

# Brings the root window to the front of other windows (needs to be before mainloop)
root.lift()
root.attributes("-topmost", True)

root.mainloop()
#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Emma Beyer (emma.beyer@duke.edu)
# Date:   Fall 2024
#--------------------------------------------------------------

#Ask user for a date
user_date = input("Enter a date: ")

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Initialize dictonaries
date_dict = {}
location_dict = {} 

#Pretend we read one line of data from the file
for lineString in line_list[17:]:
    # Check if line is a data line
    if lineString[0] in ("#","u"):
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Determine if location class criterion is met
    if obs_lc in ("1","2","3"):
        #Add items to dictonaries
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
    
#Initialze key list
keys = []

#Loop through all key, value pairs in the date_dictionary
for key, value in date_dict.items():
    if value == user_date:
        keys.append(key)

#Loop through keys and report locations
for key in keys:
    location = location_dict[key]
    lat = location[0]
    lng = location[1]
    print(f"On {user_date}, Sara the turtle was seen at {lat}d Lat, {lng}d Lng.")
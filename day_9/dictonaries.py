info = {
    "Name" : "Sakshi",
    "City" : "Kolhapur",
    "Age" : 20
} # here LHS is 'Key' and RHS is 'Value'

#to print key and value
print(info)

#to print value
print(info["Name"])

#to add new entry in dictonary
info["Collage"] = "IIT Bombay"
print(info)

#to edit any key
info["Age"] = 21
print(info)

#loop through dict
for key in info:
    print(key)  #while looping it just prints key 

#to wipe an existing dict
info = {}
print(info)




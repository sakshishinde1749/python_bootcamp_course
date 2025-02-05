# we can nest list as well as dictnory inside any dictnory


# Nested list in dictionary
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Berlin", "Stuttgart"]
# }

# to print any value inside list
# print(travel_log["France"][1])


# Nested dictionary in dictionary
travel = {
    "France" : {
        "num_time_visited" : 8,
        "cities_visited" : ["Paris", "Lille"]
    },
    "Germany" : ["Berlin", "Stuttgart"]
}

print(travel["France"])
print(travel["France"]["cities_visited"][0])
print(travel["Germany"][0])

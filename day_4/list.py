# List is a data structure

import random

countries = ["India", "America", "Germany", "Canada", "korea", "Japan"]

#to print any element of list
print(countries[0])

#to change the value of any element in the list
countries[1] = "USA"

#to add new element
countries.append("Chaina")

#to add no of element
countries.extend(["thailand", "North korea"])

#to print list
print(countries)


#to print any random element from list in 2 ways
print(countries[random.randint(0, 5)])
print(random.choice(countries))



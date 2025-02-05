fruits = ["Apple", "Pear", "Orange", "banana"]
student_scores = [132, 233, 133, 412, 342, 242, 232, 590]

#for loop
for fruit in fruits:
    print(fruit)                # when it loops through entire list, it will assign values to the fruit variable
    print(fruit + " Pie")
print(fruits)                   # identation matters


#sum of list elements
sum = 0
for score in student_scores:
    sum += score
print (sum)
#we can also use sum(student_scores) 


#find max num
max = -float('inf')
for score in student_scores:
    if(score > max):
        max = score
print(max)
#we can also use max(student_scores)



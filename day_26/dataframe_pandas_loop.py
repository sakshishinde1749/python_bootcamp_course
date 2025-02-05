import pandas

# looping through row of dataframe
student_scores = {
    "student" : ["ladu", "lili", "mina", "ladubai"],
    "score" : [89, 90, 98, 88]
}

data = pandas.DataFrame(student_scores)
print(data)

for (index, row) in data.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
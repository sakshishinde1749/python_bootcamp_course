height = float(input("height: "))
weight = int(input("weight: "))

# raising own error
if height > 3:
    raise ValueError("Human height should not be over 3")

bmi = weight / height ** 2
print(bmi)
# 2 ways to write directory of any file one is absolute path and another one is realtive path

# absolute path: path from root directory
with open("/Users/sakshi/Downloads/Apping Data.csv") as data:
    content = data.read()
    print(content)

# realtive path: path from our directory realatively
with open("./file.csv") as data:
    data.read()
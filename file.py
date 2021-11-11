import os
import timeit


path = "/Users/Dzhulai Anton/Documents/GitHub/Lab3/File"
with open("File", "w") as f:
    while  os.path.getsize(path) < 52428800:
        f.write(str(12746289462374623846234623487324783268468)+ "\n")

k = """s=0
s=0
with open("File", "r") as file:
    for i in file.readlines():
        if i.strip().isdigit():
            s+=int(i)
"""

print(timeit.timeit(k, number=50)/50)

k = """s=0
with open("File", "r") as file:
    for i in file:
        if i.strip().isdigit():
            s+=int(i)
"""

print(timeit.timeit(k, number=50)/50)
k = """s=0
with open("File", "r") as file:
    s = sum(int(i.strip()) for i in file if i.strip().isdigit()) 
"""

print(timeit.timeit(k, number=50)/50)
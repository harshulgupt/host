# read data from data.txt
with open("data.txt", "r") as f:
    data = f.read()

# write data to output.txt file
with open("output.txt", "w") as f:
    f.write(data)

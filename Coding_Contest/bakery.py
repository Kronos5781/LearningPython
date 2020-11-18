import numpy as np

input_file = open("input.txt", "r")

input = input_file.read()
input = np.array(input.split(" "))
input = input.reshape(len(input) // 3, 3)

wrong = []

for i in range(0, len(input) // 2):
    if input[i][2] != input[i + len(input) // 2][2]:
        wrong = np.append(wrong, input[i][1])

print("The Array is : ")
for i in range(0, len(wrong)):
    print(wrong[i], end = ' ')
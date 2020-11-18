# Genetic Drift
import numpy as np

# Define Input and Output File
input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

def read_input():
    input = input_file.read()
    input = np.array(input.split(" "), dtype=int)

    return input

def write_output(output, space):
    if space:
        output_file.write(str(output))
        output_file.write(" ")
    else:
        output_file.write(str(output))

def find_oriented_pairs(input):
    # Define Output Array
    output = []

    for i in range(len(input)):
        for j in range(len(input)):
            if j > i:  # Check if the numbers are consecutive
                if input[i] >= 0 and input[
                    j] < 0:  # Check if One of the two Numbers is Negative (0 wird als positive Zahl gewertet)
                    if input[i] - input[j] * -1 == -1 or input[i] - input[j] * -1 == 1:  # Check if |x| - |y| = +-1
                        output.append((input[i], input[j], i, j))  # Append the Value to the list and the index in the input

                elif input[i] < 0 and input[
                    j] >= 0:  # Check if One of the two Numbers is Negative (0 wird als positive Zahl gewertet)
                    if input[i] * -1 - input[j] == -1 or input[i] * -1 - input[j] == 1:  # Check if |x| - |y| = +-1
                        output.append((input[i], input[j], i, j))  # Append the Value to the list and the index in the input
    return output

def sort_oriented_paris(input):
    # Sort by x ascending
    for i in range(len(input)):
        for i in range(len(input) - 1):
            if input[i][0] > input[i + 1][0]:
                buffer_var = input[i]
                input[i] = input[i + 1]
                input[i + 1] = buffer_var
    return input

def write_oriented_pairs(input):
    # Write the number of Pairs
    write_output(len(input), True)

    # Write the Pairs itself
    for i in range(len(input)):
        if i == len(input) - 1:
            write_output(input[i][0], True)
            write_output(input[i][1], False) # If this is the last Output don't put a space behind it
        else:
            write_output(input[i][0], True)
            write_output(input[i][1], True)

def write_inverted_pairs(input):
    for i in range(len(input)):
        if i == len(input) - 1:
            write_output(input[i], False)
        else:
            write_output(input[i], True)




def inverse_oriented_pairs(input):
    output = []
    buffer = []
    front = []
    back = []

    if input[len(input) - 4] + input[len(input) - 2] == -1: # Check if the Sum of the oriented pair is -1 or +1
        for i in range(input[len(input) - 1] + 1, input[len(input) - 3] + 1, - 1): # Reverse the Part that needs to be reversed
            buffer.append(input[i] * -1)

        for i in range(1, input[len(input) - 3] + 2): # Put the part before the mutation in a seperate array because i don't know how to code
            front.append(input[i])

        for i in range(input[len(input) - 1] + 2, len(input) - 4): # Put the part after the mutation in a seperate array because i don't know how to code
            back.append(input[i])

    elif input[len(input) - 4] + input[len(input) - 2] == 1:
        for i in range(input[len(input) - 1], input[len(input) - 3], -1):
            buffer.append(input[i] * -1)

        for i in range(1, input[len(input) - 3] + 1):
            front.append(input[i])

        for i in range(input[len(input) - 1] + 1, len(input) - 4):
            back.append(input[i])

    # Put it all together and send it back
    for i in front:
        output.append(i)
    for i in buffer:
        output.append(i)
    for i in back:
        output.append(i)

    return output

if __name__ == '__main__':

    input = read_input()

    input = find_oriented_pairs(input)

    print(sort_oriented_paris(input))






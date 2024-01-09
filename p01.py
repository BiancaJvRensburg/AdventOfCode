import os

# Part 1
def elf_calories():
    dataFile = os.getcwd()+"\\p01-data.txt"
    elf_calories = []
    data = open(dataFile, "r")
    isNewElf = True     # Start counting calories for a new elf ?

    for calories in data:
        if calories == '\n':    # End of an elf, move on to the next
            isNewElf = True
            continue
        if isNewElf:            # Start the new elf
            elf_calories.append(int(calories))
            isNewElf = False
        else:                   # Add to the current elf's count
            elf_calories[-1] += int(calories)

    return elf_calories

# Basic max for a positive integer list
def max(numbers):
    max_number = 0

    for x in numbers:
        if x > max_number:
            max_number = x
    
    return max_number

# Part 2
def top_three(numbers):
    max_three = [0, 0, 0]

    for x in numbers:
        for i in range(3):
            if x > max_three[i]:        # If new top 3 elf, add it to the correct position
                max_three.insert(i, x)
                max_three.pop()         # Delete the last element (the smallest of the 4)
                break
    
    return max_three

# Basic sum of a list of integers
def add_list(numbers):
    sum = 0

    for x in numbers:
        sum += x
    
    return sum


if __name__ == "__main__":
    elf_cal = elf_calories()

    # Part 1
    """
    max_calories = max(elf_cal)
    print('Max calories:', max_calories)
    """

    # Part 2
    top_calories = top_three(elf_cal)
    print('Top 3 elves calories:', top_calories)
    total_top_calories = add_list(top_calories)
    print('Total calories of the top 3 elves: ', total_top_calories)


def readInput():
    # list of (summed food calories) carried by all elf
    calorie_list = list()
    sum = 0
    # reading the file
    with open("input_d1.txt", "r") as file:
        for calorie in file:
            if(calorie == '\n'): # mean the end of i'th elf food 
                calorie_list.append(int(sum))
                sum=0 # reset sum to count the next elf's food
            else: 
                sum+=int(calorie)
    calorie_list.append(int(sum)) # this will append the last elf's food list

    return calorie_list 

# part 1 of the puzzle is to find the biggest calories in the list
def part1(calories):
    ans = calories[0]
    # iterate through list to find the max, and return it
    # default = return the first item on the list
    for x in calories:
        if x >= ans:
            ans = x
    return ans

# part 2 of the puzzle is to find sum of 3 biggest calories in the list
def part2(calories):
    ans = 0
    # sort from biggest to lowest
    calories.sort(reverse=True)
    for i in range(3):
        ans+=calories[i]
    return ans

def main():
    calories = readInput()
    print("you answer for:")
    print(f"part 1 = {part1(calories)}")
    print(f"part 2 = {part2(calories)}")

main()
# part 1 answer is: 70698 
# part 2 answer is: 206643
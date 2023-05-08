def part1(a,b):
    if(b==0):
        return (a + 2) % 3
    elif(b==1):
        return a
    else:
        return (a + 1) % 3

def part2(a,b):
    b=part1(a,b)
    if (a + 1) % 3 == b:
        return 6+b+1
    elif a == b:
        return 3+b+1
    else:
        return b+1

def main():
    a = 0
    b = 0
    ans1 = 0
    ans2 = 0
    with open("input_d2.txt", "r") as x:
        for i in x:
            a,b = i.split()
            ans1+=part1(ord(a)-ord('A'),ord(b)-ord('X'))
            ans2+=part2(ord(a)-ord('A'),ord(b)-ord('X'))
        print("you answer for:")
        print(f"part 1 = {ans1}")
        print(f"part 2 = {ans2}")


main()
# you answer for:
# part 1 = 2101
# part 2 = 10274
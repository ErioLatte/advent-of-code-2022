def part2(p1):
    print("hello")

"""
explanation:
ROCK  --  PAPER  --  SCISSOR
front beat back
scissor beat paper,
paper beat rock,
rock beat scissor

for it to be looping, we need to use modulo
0           1           2         0(3%3)    1(4%3)
ROCK  --  PAPER  --  SCISSOR  --  ROCK  --  PAPER

see the pattern?
"""
def calculate1(p1, p2):
    if (p1 + 1) % 3 == p2: # lose
        return p1
    elif p1 == p2: # tie
        return 3 + p1
    else: # win
        return 6 + p1

def calculate(p2, p1):
    matrices = [
        [3, 0, 6],
        [6, 3, 0],
        [0, 6, 3],
    ]
    value = matrices[p1][p2]+p1+1
    # print(value)
    return value

def main():
    a = 0
    b = 0
    ans = 0
    with open("input_d2.txt", "r") as f:
        for line in f:
            a = line.split()
            ans += calculate(ord(a[0]) - ord('A'), ord(a[1])-ord('X'))
        print(ans)



main()
# you answer for:
# part 1 = 2101
# part 2 = 10274
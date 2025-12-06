from pathlib import Path

rolls = set()

with open(Path(__file__).parent / "input" / "day04.txt") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char != "@":
                continue
            rolls.add((x, y))


def removable_rolls():
    for x, y in rolls:
        roll = (x, y)
        neighbours = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                neighbour = (i, j)
                if neighbour != roll and neighbour in rolls:
                    neighbours += 1
        if neighbours < 4:
            yield roll


part1 = sum(1 for roll in removable_rolls())
print(part1)

count = 0
any_removed = True
while any_removed:
    any_removed = False
    for roll in list(removable_rolls()):
        rolls.remove(roll)
        any_removed = True
        count += 1

print(count)

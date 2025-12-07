from collections.abc import Iterator, Sequence
from pathlib import Path


def removable_rolls() -> Iterator[tuple[int, int]]:
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


if __name__ == "__main__":
    rolls = set()

    with open(Path(__file__).parent / "input" / "day04.txt") as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char != "@":
                    continue
                rolls.add((x, y))

    part1 = sum(1 for roll in removable_rolls())
    print(f"Part 1: {part1}")

    part2 = 0
    any_removed = True
    while any_removed:
        any_removed = False
        for roll in list(removable_rolls()):
            rolls.remove(roll)
            any_removed = True
            part2 += 1

    print(f"Part 2: {part2}")

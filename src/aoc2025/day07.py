from collections.abc import Sequence
from pathlib import Path


def part1(lines: Sequence[str]) -> int:
    count = 0
    it = iter(lines)
    beams = {i for i, c in enumerate(next(it)) if c == "S"}
    for line in it:
        splitters = {i for i, c in enumerate(line) if c == "^"}
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                count += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    return count


def part2(lines: Sequence[str]) -> int:
    count = 0
    it = iter(lines)
    beams = {i: 1 for i, c in enumerate(next(it)) if c == "S"}
    for line in it:
        splitters = {i for i, c in enumerate(line) if c == "^"}
        new_beams: dict[int, int] = {}
        for beam, paths in beams.items():
            if beam in splitters:
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + paths
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + paths
            else:
                new_beams[beam] = new_beams.get(beam, 0) + paths
        beams = new_beams
    return sum(beams.values())


if __name__ == "__main__":
    with open(Path(__file__).parent / "input" / "day07.txt") as file:
        manifold = list(file)
    result1 = part1(manifold)
    print(f"Part 1: {result1}")
    result2 = part2(manifold)
    print(f"Part 2: {result2}")

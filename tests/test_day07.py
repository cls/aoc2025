from pytest import fixture

from aoc2025.day07 import part1, part2


@fixture
def example1() -> list[str]:
    return [
        ".......S.......\n",
        "...............\n",
        ".......^.......\n",
        "...............\n",
        "......^.^......\n",
        "...............\n",
        ".....^.^.^.....\n",
        "...............\n",
        "....^.^...^....\n",
        "...............\n",
        "...^.^...^.^...\n",
        "...............\n",
        "..^...^.....^..\n",
        "...............\n",
        ".^.^.^.^.^...^.\n",
        "...............\n",
    ]


def test_part1_example(example1: list[str]) -> None:
    count = part1(example1)
    assert count == 21


def test_part2_example(example1: list[str]) -> None:
    count = part2(example1)
    assert count == 40

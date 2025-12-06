from pytest import fixture

from aoc2025.day03 import part1, part2


@fixture
def example1():
    return [
        "987654321111111\n",
        "811111111111119\n",
        "234234234234278\n",
        "818181911112111\n",
    ]


def test_part1_example(example1):
    total = part1(example1)
    assert total == 357


def test_part2_example(example1):
    total = part2(example1)
    assert total == 3121910778619

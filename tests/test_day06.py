from pytest import fixture

from aoc2025.day06 import part1, part2


@fixture
def example1() -> list[str]:
    return [
        "123 328  51 64\n",
        " 45 64  387 23\n",
        "  6 98  215 314\n",
        "*   +   *   +\n",
    ]


def test_part1_example(example1: list[str]) -> None:
    result = part1(example1)
    assert result == 4277556


def test_part2_example(example1: list[str]) -> None:
    result = part2(example1)
    assert result == 3263827

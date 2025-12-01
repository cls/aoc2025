from pytest import fixture

from aoc2025.day01 import Dial, Direction, Rotation, part1, part2


def test_dial_rotates() -> None:
    dial = Dial(position=11)
    dial.rotate(Rotation(Direction.R, 8))
    assert dial.position == 19
    dial.rotate(Rotation(Direction.L, 19))
    assert dial.position == 0


def test_dial_is_a_circle() -> None:
    dial = Dial(position=0)
    dial.rotate(Rotation(Direction.L, 1))
    assert dial.position == 99
    dial.rotate(Rotation(Direction.R, 1))
    assert dial.position == 0


@fixture
def example1() -> list[str]:
    return [
        "L68\n",
        "L30\n",
        "R48\n",
        "L5\n",
        "R60\n",
        "L55\n",
        "L1\n",
        "L99\n",
        "R14\n",
        "L82\n",
    ]


def test_part1_example(example1: list[str]) -> None:
    password = part1(example1)
    assert password == 3


def test_part2_example(example1: list[str]) -> None:
    password = part2(example1)
    assert password == 6


def test_count_zeros() -> None:
    dial = Dial(position=50)
    count = dial.count_zeros(Rotation(Direction.R, 1000))
    assert count == 10

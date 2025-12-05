import logging

from pytest import fixture

from aoc2025.day05 import Database, part1, part2


@fixture
def example1():
    return [
        "3-5\n",
        "10-14\n",
        "16-20\n",
        "12-18\n",
        "\n",
        "1\n",
        "5\n",
        "8\n",
        "11\n",
        "17\n",
        "32\n",
    ]


def test_part1_example(example1):
    database = Database.parse(example1)
    count = part1(database)
    assert count == 3


def test_part2_example(example1):
    database = Database.parse(example1)
    count = part2(database)
    assert count == 14

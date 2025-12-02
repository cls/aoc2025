import re

from pytest import fixture

from aoc2025.day02 import ProductIdRange, part1


def id_is_invalid(id: int) -> bool:
    id_str = str(id)
    matchobj = re.fullmatch(r"(\d+)\1", id_str)
    return matchobj is not None


def test_invalid_ids() -> None:
    assert id_is_invalid(55)
    assert id_is_invalid(6464)
    assert id_is_invalid(123123)
    assert not id_is_invalid(101)


@fixture
def example1() -> str:
    return (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
        "824824821-824824827,2121212118-2121212124\n"
    )


def test_example_invalid_ids(example1: str) -> None:
    id_ranges = ProductIdRange.parse_list(example1)
    invalid_ids = [list(id_range.invalid_ids()) for id_range in id_ranges]
    assert invalid_ids == [
        [11, 22],
        [99],
        [1010],
        [1188511885],
        [222222],
        [],
        [446446],
        [38593859],
        [],
        [],
        [],
    ]


def test_part1_example(example1: str) -> None:
    total = part1(example1)
    assert total == 1227775554

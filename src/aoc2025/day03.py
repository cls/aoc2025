import logging
from collections.abc import Sequence
from pathlib import Path

logger = logging.getLogger(__name__)


def part1(battery_banks: Sequence[str]):
    total = 0
    for battery_bank in battery_banks:
        battery_bank = battery_bank.strip()
        batteries = [int(battery) for battery in battery_bank]
        fst, j = sorted((-battery, i) for i, battery in enumerate(batteries[:-1]))[0]
        snd, k = sorted((-battery, i) for i, battery in enumerate(batteries[j + 1 :]))[
            0
        ]
        joltage = (-fst * 10) - snd
        logger.debug(
            f"In {battery_bank}, you can make the largest joltage possible, {joltage}, "
            f"by turning on batteries {j} and {j + k + 1}"
        )
        total += joltage
    return total


def part2(battery_banks: Sequence[str]):
    total = 0
    for battery_bank in battery_banks:
        battery_bank = battery_bank.strip()
        batteries = [int(battery) for battery in battery_bank]
        end_battery_idx = len(batteries) - 12
        assert end_battery_idx >= 0
        joltage = 0
        on_battery_idx = -1
        on_batteries = []
        for batteries_left in range(12):
            max_battery = 0
            max_battery_idx = -1
            for battery_idx, battery in enumerate(batteries):
                if (
                    on_battery_idx < battery_idx <= end_battery_idx + batteries_left
                    and max_battery < battery
                ):
                    max_battery = battery
                    max_battery_idx = battery_idx
            on_battery_idx = max_battery_idx
            on_batteries.append(on_battery_idx)
            joltage = joltage * 10 + max_battery
        logger.debug(
            f"In {battery_bank}, you can make the largest joltage possible, {joltage}, "
            f"by turning on batteries {on_batteries}"
        )
        total += joltage
    return total


if __name__ == "__main__":
    with open(Path(__file__).parent / "input" / "day03.txt") as file:
        battery_banks = list(file)
    total1 = part1(battery_banks)
    print(f"Part 1: {total1}")
    total2 = part2(battery_banks)
    print(f"Part 2: {total2}")

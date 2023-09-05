from enum import Enum

class Difficulty(Enum):
    VERY_EASY = 1
    EASY = 2
    MEDIUM = 3
    HARD = 4

class Result:
    QUALIFIED = "qualified"
    DISQUALIFIED = "disqualified"

q_difficulties = (d := Difficulty) and [
    d.VERY_EASY, d.VERY_EASY, d.EASY, d.EASY, d.MEDIUM, d.MEDIUM, d.HARD, d.HARD
]

max_time_by_difficulty = {
    d.VERY_EASY: 5,
    d.EASY: 10,
    d.MEDIUM: 15,
    d.HARD: 20
}

def interview(lst: list[int], tot: int) -> str:
    all_qs_completed = len(lst) == len(q_difficulties)
    if not all_qs_completed:
        return Result.DISQUALIFIED
    qs_completed_in_time = all(
        t <= max_time_by_difficulty[mt]
        for t, mt in zip(lst, q_difficulties)
    ) and tot <= 120
    return Result.QUALIFIED if qs_completed_in_time else Result.DISQUALIFIED

assert interview([5, 5, 10, 10, 15, 15, 20, 20], 120) == "qualified"
assert interview([2, 3, 8, 6, 5, 12, 10, 18], 120) == "qualified"
assert interview([2, 3, 8, 6, 5, 12, 10, 18], 64) == "qualified"
assert interview([5, 5, 10, 10, 25, 15, 20, 20], 120) == "disqualified"
assert interview([5, 5, 10, 10, 15, 15, 20], 120) == "disqualified"
assert interview([5, 5, 10, 10, 15, 15, 20, 20], 130) == "disqualified"
assert interview([5, 5, 10, 10, 15, 20, 50], 160) == "disqualified"
assert interview([5, 5, 10, 10, 15, 15, 40], 120) == "disqualified"
assert interview([10, 10, 15, 15, 20, 20], 150) == "disqualified"
assert interview([5, 5, 10, 20, 15, 15, 20, 20], 140) == "disqualified"
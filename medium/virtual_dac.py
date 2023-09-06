def virtual_dac(value: float) -> float:
    return round(value / 1023 * 5, 2)

assert virtual_dac(0) == 0
assert virtual_dac(1023) == 5
assert virtual_dac(400) == 1.96
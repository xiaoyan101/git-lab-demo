from add import add, mul

cases = [(1, 2, 3), (-1, 1, 0), (0, 0, 0), (2.5, 3.5, 6.0)]

for a, b, expected in cases:
    assert add(a, b) == expected, f"{a}+{b} 结果错误"

mul_cases = [(2, 3, 6), (-1, 2, -2), (0, 5, 0), (1.5, 2, 3.0)]

for a, b, expected in mul_cases:
    assert mul(a, b) == expected, f"{a}*{b} 结果错误"

print("全部用例通过")

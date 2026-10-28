from add import add

cases = [(1, 2, 3), (-1, 1, 0), (0, 0, 0), (2.5, 3.5, 6.0)]

for a, b, expected in cases:
    assert add(a, b) == expected, f"{a}+{b} 结果错误"

print("全部用例通过")

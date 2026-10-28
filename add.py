def add(a, b):
    return a + b
if __name__ == "__main__":
    x = float(input("第一个数："))
    y = float(input("第二个数："))
    print(f"{x} + {y} = {add(x, y)}")

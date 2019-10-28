from exp import Val, Add

def parse(s: str):
    num = int(s)
    return Val(num)

e = parse("123")
print(e)

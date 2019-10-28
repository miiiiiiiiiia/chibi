from exp import Val, Add

'''
def parse(s: str):
    num = int(s)
    return Val(num)

e = parse("123")
print(e)

s = "1+2"
pos = s.find('+')
print('pos',pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s, s1, s2)
'''

def parse(s: str):
    pos = s.find('+')
    if pos == -1:
        num = int(s)
        return Val(int(s))
    else:
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(parse(s1),parse(s2))

e = parse("1+2+3")
print(e, e.eval())

import pegpy
peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value (^{ '*' Value #Mul })*
Value = { [0-9]+ #Int }
''')
parser = pegpy.generate(peg)

t = parser('1+2*3')
print(repr(t))

def clac(t):
    if t == 'Int':
        return int(str(t))
    if t == 'Add':
        return clac(t[0]) + clac(t[1])
    if t == 'Mul':
        return clac(t[0]) * clac(t[1])
    print(f'TODO {t.tag}')
    return 0

t = parser('1+2*3+4*5')
print(repr(t))
print(clac(t))
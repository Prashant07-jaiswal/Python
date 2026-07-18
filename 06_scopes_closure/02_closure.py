def chaicoder(num):
    def actual(x):
        return x**num
    return actual(3)

f = chaicoder(2)
g = chaicoder(3)
print(chaicoder(2))
print(f)
print(g)

print(f(3))
print(g(3))

def chaicoder(num):
    def actual(x):
        return x**num
    print(actual(3))

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))

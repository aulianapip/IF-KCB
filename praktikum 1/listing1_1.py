from kanren.core import var, eq, run
x = var()
output = run(1, x, eq(5, x))
print(output)
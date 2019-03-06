from kanren.core import var, eq, run
x = var()
y = var()
output = run(1, x, eq((x, y), (y, 3)))
print(output)
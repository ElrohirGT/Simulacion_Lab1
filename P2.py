#!/usr/bin/env python3
import pulp as p

problem = p.LpProblem(name="Problema_de_horarios", sense=p.LpMinimize)


x1 = p.LpVariable("x1", 0, 225)
x2 = p.LpVariable("x2", 0, 225)
x3 = p.LpVariable("x3", 0, 225)
x4 = p.LpVariable("x4", 0, 225)
x5 = p.LpVariable("x5", 0, 225)
x6 = p.LpVariable("x6", 0, 225)

# x1 = p.LpVariable("x1", 0, 225, p.LpInteger)
# x2 = p.LpVariable("x2", 0, 225, p.LpInteger)
# x3 = p.LpVariable("x3", 0, 225, p.LpInteger)
# x4 = p.LpVariable("x4", 0, 225, p.LpInteger)
# x5 = p.LpVariable("x5", 0, 225, p.LpInteger)
# x6 = p.LpVariable("x6", 0, 225, p.LpInteger)

I1 = p.LpVariable("I1", 0)
I2 = p.LpVariable("I2", 0)
I3 = p.LpVariable("I3", 0)
I4 = p.LpVariable("I4", 0)
I5 = p.LpVariable("I5", 0)
I6 = p.LpVariable("I6", 0)

problem += 50*x1 + 45*x2 + 55*x3 + 52*x4 + 48*x5 + 50*x6 + 8*I1 + 10*I2 + 10*I3 + 10*I4 + 8*I5 + 8*I6

problem += x1 - I1 == 180
problem += I1 + x2 - I2 == 250
problem += I2 + x3 - I3 == 190
problem += I3 + x4 - I4 == 140
problem += I4 + x5 - I5 == 220
problem += I5 + x6 - I6== 250

status = problem.solve()

print("M1 :", p.value(x1), "ventanas.", p.value(I1), "bodega.","Total:", 50*p.value(x1) + 8*p.value(I1))
print("M2:", p.value(x2), "ventanas.", p.value(I2), "bodega.","Total:", 50*p.value(x2) + 10*p.value(I2))
print("M3:", p.value(x3), "ventanas.", p.value(I3), "bodega.","Total:", 50*p.value(x3) + 10*p.value(I3))
print("M4:", p.value(x4), "ventanas.", p.value(I4), "bodega.","Total:", 50*p.value(x4) + 10*p.value(I4))
print("M5:", p.value(x5), "ventanas.", p.value(I5), "bodega.","Total:", 50*p.value(x5) + 8*p.value(I5))
print("M6:", p.value(x6), "ventanas.", p.value(I6), "bodega.","Total:", 50*p.value(x6) + 8*p.value(I6))


#!/usr/bin/env python3
import pulp as p

problem = p.LpProblem(name="Problema_de_horarios", sense=p.LpMinimize)

x1 = p.LpVariable("x1", 0)
x2 = p.LpVariable("x2", 0)
x3 = p.LpVariable("x3", 0)
x4 = p.LpVariable("x4", 0)
x5 = p.LpVariable("x5", 0)
x6 = p.LpVariable("x6", 0)

problem += x1 + x6 >= 4
problem += x1 + x2 >= 8
problem += x2 + x3 >= 10
problem += x3 + x4 >= 7
problem += x4 + x5 >= 12
problem += x5 + x6 >= 4

problem += x1 >= 0
problem += x2 >= 0
problem += x3 >= 0
problem += x4 >= 0
problem += x5 >= 0
problem += x6 >= 0

status = problem.solve()
# print(status)

print("El turno 1 tiene:", p.value(x1), "buses.")
print("El turno 2 tiene:", p.value(x2), "buses.")
print("El turno 3 tiene:", p.value(x3), "buses.")
print("El turno 4 tiene:", p.value(x4), "buses.")
print("El turno 5 tiene:", p.value(x5), "buses.")
print("El turno 6 tiene:", p.value(x6), "buses.")

print(
    "Dando un total de:", sum([p.value(x) for x in [x1, x2, x3, x4, x5, x6]]), "buses"
)

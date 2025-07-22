import pulp as p

# Crear el problema de maximización
problem = p.LpProblem(name="Parte 1 Programación Lineal", sense=p.LpMaximize)

x1 = p.LpVariable("x1", lowBound=0)
x2 = p.LpVariable("x2", lowBound=0)
x3 = p.LpVariable("x3", lowBound=0)
x4 = p.LpVariable("x4", lowBound=0)

problem += x1 + x2 + 3 * x3 + 2 * x4, "Z"

problem += x1 + 2 * x2 - 3 * x3 + 5 * x4 <= 4 #  "Restriccion 1"
problem += 5 * x1 - 2 * x2 + 6 * x4 <= 8 # "Restriccion 2"
problem += 2 * x1 + 3 * x2 - 2 * x3 + 3 * x4 <= 3 # "Restriccion 3"
problem += -x1 + x3 + 2 * x4 <= 0 # "Restriccion 4"

status = problem.solve()

print(f"Estado: {p.LpStatus[status]}")
print("Solución óptima encontrada:")
print(f"x1 = {p.value(x1)}")
print(f"x2 = {p.value(x2)}")
print(f"x3 = {p.value(x3)}")
print(f"x4 = {p.value(x4)}")
print(f"Valor máximo de Z = {p.value(problem.objective)}")

from pulp import *
import sys
# Crear el problema
model = LpProblem("Renovacion_Urbana", LpMaximize)

arg = 0
if len(sys.argv) < 2:
        print("Usage: python P4.py <argument>")
        
        arg = int(sys.argv[1])


if len(sys.argv) < 2:
    print("Usage: python P4.py <argument>")

arg = sys.argv[1]
print(f"Received argument: {arg}")

try:
    number = int(arg)
    
    
    if arg == "1":
        x1 = LpVariable("Sencillas", lowBound=0, cat='Integer')
        x2 = LpVariable("Dobles", lowBound=0, cat='Integer')
        x3 = LpVariable("Triples", lowBound=0, cat='Integer')
        x4 = LpVariable("Cuadruples", lowBound=0, cat='Integer')
    else:
        # Variables continuas
        x1 = LpVariable("Sencillas", lowBound=0)
        x2 = LpVariable("Dobles", lowBound=0)
        x3 = LpVariable("Triples", lowBound=0)
        x4 = LpVariable("Cuadruples", lowBound=0)

    # Función objetivo
    model += 1000*x1 + 1900*x2 + 2700*x3 + 3400*x4

    # Restricciones
    model += 0.18*x1 + 0.28*x2 + 0.4*x3 + 0.5*x4 <= 63.75  # Área
    model += 50000*x1 + 70000*x2 + 130000*x3 + 160000*x4 <= 15000000  # Costo

    model += 0.75*x3 + 0.75*x4 - 0.25*x1 - 0.25*x2 >= 0
    model += 0.8*x1 - 0.2*x2 - 0.2*x3 - 0.2*x4 >= 0
    model += 0.9*x2 - 0.1*x1 - 0.1*x3 - 0.1*x4 >= 0

    model.solve()

    # Resultados
    print("Estado:", LpStatus[model.status])
    print("Recaudación total:", value(model.objective))
    for var in [x1, x2, x3, x4]:
        print(f"{var.name}: {var.varValue:.2f}")



except ValueError:
    print("Argument is not a valid integer.")

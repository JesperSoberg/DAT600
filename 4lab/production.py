from pulp import LpMaximize, LpProblem, LpVariable


if __name__ == "__main__":
    model = LpProblem(sense=LpMaximize)
    
    X = LpVariable(name="X", lowBound=10, cat="Integer")
    Y = LpVariable(name="Y", lowBound=0, cat="Integer")

    model += (15*X + 20*Y <= 2400)
    model += (20*X + 30*Y <= 2100)

    model += 200*X + 300*Y - 100/4*X - 100/3*Y - 20/3*X - 20/2*Y

    model.solve()

    print(f"objective: {model.objective.value()}")
    for var in model.variables():
        print(f"{var.name}: {var.value()}")

    
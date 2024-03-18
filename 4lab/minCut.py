from pulp import LpProblem, LpVariable

# 0 = i S-settet
# 1 = i T-settet

if __name__ == "__main__":

    model = LpProblem()

    V1 = LpVariable(name="V1", cat="Binary")
    V13 = LpVariable(name="V13", cat="Binary")
    V14 = LpVariable(name="V14", cat="Binary")

    V2 = LpVariable(name="V2", cat="Binary")
    V23 = LpVariable(name="V23", cat="Binary")
    V25 = LpVariable(name="V25", cat="Binary")

    V3 = LpVariable(name="V3", cat="Binary")
    V34 = LpVariable(name="V43", cat="Binary")
    V35 = LpVariable(name="V35", cat="Binary")

    V4 = LpVariable(name="V4", cat="Binary")
    V45 = LpVariable(name="V54", cat="Binary")

    V5 = LpVariable(name="V5", cat="Binary")

    v1_edges = 14*V1 + 3*(V3 - V13) + 21*(V4 - V14)
    v2_edges = 25*V2 + 13*(V3 - V23) + 7*(V5 - V25)
    v3_edges = 6*(V1 - V13) + 15*(V5 - V35)
    v4_edges = 10*(V3 - V34) + 20*(1-V4)
    v5_edges = 5*(V4 - V45) + 10*(1-V5)

    obj = v1_edges + v2_edges + v3_edges + v4_edges + v5_edges

    model += obj

    model += V13 <= V1
    model += V13 <= V3
    model += V13 >= V1 + V3 - 1

    model += V14 <= V1
    model += V14 <= V4
    model += V14 >= V1 + V4 - 1

    model += V23 <= V2
    model += V23 <= V3
    model += V23 >= V2 + V3 - 1

    model += V25 <= V2
    model += V25 <= V5
    model += V25 >= V2 + V5 - 1

    model += V34 <= V3
    model += V34 <= V4
    model += V34 >= V3 + V4 - 1

    model += V35 <= V3
    model += V35 <= V5
    model += V35 >= V3 + V5 - 1

    model += V45 <= V4
    model += V45 <= V5
    model += V45 >= V4 + V5 - 1

    model.solve()

    print(f"objective: {model.objective.value()}")

    for var in model.variables():
        print(f"{var.name}: {var.value()}")

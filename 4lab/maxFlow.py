from pulp import LpProblem, LpVariable, LpMaximize

if __name__ == "__main__":

	model = LpProblem(sense=LpMaximize)

	SV1 = LpVariable(name="SV1", cat="Integer", lowBound=0)
	SV2 = LpVariable(name="SV2", cat="Integer", lowBound=0)
	V1V3 = LpVariable(name="V1V3", cat="Integer", lowBound=0)
	V1V4 = LpVariable(name="V1V4", cat="Integer", lowBound=0)

	V2V3 = LpVariable(name="V2V3", cat="Integer", lowBound=0)
	V2V5 = LpVariable(name="V2V5", cat="Integer", lowBound=0)

	V3V1 = LpVariable(name="V3V1", cat="Integer", lowBound=0)
	V3V5 = LpVariable(name="V3V5", cat="Integer", lowBound=0)

	V4V3 = LpVariable(name="V4V3", cat="Integer", lowBound=0)
	V4T = LpVariable(name="V4T", cat="Integer", lowBound=0)

	V5V4 = LpVariable(name="V5V4", cat="Integer", lowBound=0)
	V5T = LpVariable(name="V5T", cat="Integer", lowBound=0)

	#obj = SV1 + SV2 + V1V3 + V1V4 + V2V3 + V2V5 + V3V1 + V3V5 +V4V3 + V4T + V5V4 + V5T
	obj = V4T + V5T

	model += obj
	
	model += SV1 <= 14
	model += SV2 <= 25
	model += V1V3 <= 3
	model += V1V4 <= 21
	model += V2V3 <= 13
	model += V2V5 <= 7
	model += V3V1 <= 6
	model += V3V5 <= 15
	model += V4V3 <= 10
	model += V4T <= 20
	model += V5V4 <= 5
	model += V5T <= 10

	model += SV1 + V3V1 == V1V3 + V1V4
	model += SV2 == V2V3 + V2V5
	model += V1V3 + V2V3 + V4V3  == V3V1 +V3V5
	model += V1V4 + V5V4 == V4V3 + V4T
	model += V2V5 + V3V5 == V5V4 + V5T
	

	

	model.solve()
        
	print(f"objective: {model.objective.value()}")

	for var in model.variables():
		print(f"{var.name}: {var.value()}")
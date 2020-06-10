import pulp

prob = pulp.LpProblem("myProblem", pulp.LpMaximize)

r = pulp.LpVariable('r', lowBound=0)
g = pulp.LpVariable('g', lowBound=0)
b = pulp.LpVariable('b', lowBound=0)
k = pulp.LpVariable('k', lowBound=0)


#obj fnc
prob += 10 * r + 15 * g + 25 * b + 25 * k, "Z"

# constraints
prob += (1/2) * r + (1/2) * g + (1/3) * k  <= 11
prob += (1/2) * r + (1/2) * b + (1/3) * k  <= 5
prob += (1/2) * g + (1/2) * b + (1/3)* k  <= 10

prob.solve()

print(pulp.LpStatus[prob.status])
for variable in prob.variables():
    print ("{} = {}".format(variable.name, variable.varValue))

print (pulp.value(prob.objective))


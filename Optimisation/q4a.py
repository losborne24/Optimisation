import pulp

prob = pulp.LpProblem("myProblem", pulp.LpMaximize)

x1 = pulp.LpVariable('x1', lowBound=0, upBound=1, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, upBound=1,cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, upBound=1,cat='Integer')
x4 = pulp.LpVariable('x4', lowBound=0, upBound=1,cat='Integer')
x5 = pulp.LpVariable('x5', lowBound=0, upBound=1,cat='Integer')
x6 = pulp.LpVariable('x6', lowBound=0, upBound=1,cat='Integer')

#obj fnc
prob += 60 * x1 + 70 * x2 + 40 * x3 + 70 * x4 + 16 * x5 + 100 * x6, "Z"

# constraints
prob += 6 * x1 + 7 * x2 + 4*x3 + 9*x4 + 5*x5 + 8*x6 <= 20

prob.solve()

print(pulp.LpStatus[prob.status])

for variable in prob.variables():
    print ("{} = {}".format(variable.name, variable.varValue))

print(pulp.value(prob.objective))


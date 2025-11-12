import gurobipy as gp
from gurobipy import GRB

def aircraft_assignment(availability, demand, capabilities, costs):
    """
    Args:
        availability: list, availability of each aircraft
        demand: list, demand for each route
        capabilities: 2D list, capabilities of each aircraft for each route
        costs: 2D list, costs of assigning each aircraft to each route

    Returns:
        min_total_cost: float, the minimum total cost of the assignment
    """
    num_aircraft = len(availability)
    num_routes = len(demand)

    # Create a new model
    model = gp.Model("AircraftAssignment")

    # Create decision variables
    x = {}
    for i in range(num_aircraft):
        for j in range(num_routes):
            x[i, j] = model.addVar(vtype=GRB.INTEGER, name=f"x_{i}_{j}")

    # Set objective function
    model.setObjective(gp.quicksum(costs[i][j] * x[i, j] for i in range(num_aircraft) for j in range(num_routes)), GRB.MINIMIZE)

    # Add constraints
    for j in range(num_routes):
        model.addConstr(gp.quicksum(x[i, j] for i in range(num_aircraft)) == demand[j])

    for i in range(num_aircraft):
        model.addConstr(gp.quicksum(x[i, j] for j in range(num_routes)) <= availability[i])

    for i in range(num_aircraft):
        for j in range(num_routes):
            model.addConstr(x[i, j] <= capabilities[i][j])

    # Optimize the model
    model.optimize()

    # Get the minimum total cost
    min_total_cost = model.objVal

    return min_total_cost

# Example input data
availability = [5, 3]
demand = [4, 5, 6]
capabilities = [[2, 3, 4], [3, 4, 5]]
costs = [[10, 15, 20], [12, 18, 24]]

# Call the aircraft_assignment function with the example input data
min_total_cost = aircraft_assignment(availability, demand, capabilities, costs)
print("Minimum Total Cost:", min_total_cost)
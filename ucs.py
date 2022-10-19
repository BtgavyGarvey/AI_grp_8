graph = [['SportsComplex', 'Siwaka', 450],
         ['Siwaka', 'Ph.1A', 10],
         ['Siwaka', 'Ph.1B', 230],
         ['Ph.1A', 'Mada', 112],
         ['Ph.1A', 'Ph.1B', 100],
         ['Ph.1B', 'Phase2', 50],
         ['Ph.1B', 'ParkingLot', 250],
         ['Phase2', 'J1', 600],
         ['Phase2', 'Phase3', 500],
         ['Phase2', 'STC', 50],
         ['STC', 'Phase2', 50],
         ['STC', 'ParkingLot', 250],
         ['J1', 'Mada', 200],
         ['Phase3', 'ParkingLot', 350],
         ['Mada', 'ParkingLot', 700]

         ]

temp = []
temp1 = []
for i in graph:
    temp.append(i[0])
    temp1.append(i[1])
nodes = set(temp).union(set(temp1))


def Uniform_Cost_Search(graph, costs, open, closed, cur_node):
    if cur_node in open:
        open.remove(cur_node)
    closed.add(cur_node)
    for i in graph:
        if i[0] == cur_node and costs[i[0]] + i[2] < costs[i[1]]:
            open.add(i[1])
            costs[i[1]] = costs[i[0]] + i[2]
            path[i[1]] = path[i[0]] + ' -> ' + i[1]
    costs[cur_node] = 999999
    small = min(costs, key=costs.get)
    if small not in closed:
        Uniform_Cost_Search(graph, costs, open, closed, small)


costs = dict()
temp_cost = dict()
path = dict()
open = set()
closed = set()
for i in nodes:
    costs[i] = 999999
    path[i] = ' '


def main():
    start_node = 'SportsComplex'
    goal_node = 'ParkingLot'
    open.add(start_node)
    open.add(start_node)
    path[start_node] = start_node
    costs[start_node] = 0
    Uniform_Cost_Search(graph, costs, open, closed, start_node)
    print('Solution is', path[goal_node])

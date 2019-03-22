from ai_pkg.search import Graph, Problem, Node
from ai_pkg.utils import random, argmax_random_tie


start = 'NewYork'
goal = 'LosAngeles'


city_map = Graph(dict(
    NewYork=dict(Chicago=1000, Toronto=800, Denver=1900),
       Chicago=dict(Denver=1000),
       Denver=dict(LosAngeles=1000, Houston=1500, Urbana=1000),
       Houston=dict(LosAngeles=1500),
       Toronto=dict(LosAngeles=1800, Chicago=500, Calgary=1500)), directed=True)

class CityProblem(Problem):
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

    def path_cost(self, cost, A, action, B):
        return cost + (self.graph.get(A, B) or infinity)

def breadth_first_search(problem):
    global track_path
    frontier = [(Node(problem.initial))]
    explored = set()
    track_path = [problem.initial]
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        expanded = node.expand(problem)
        for child in expanded:
            track_path.append(child.state)
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

if __name__=='__main__':
    track_path = []
    romania_problem = CityProblem(start, goal , city_map)
    node = breadth_first_search(romania_problem)
    if node is not None:
        final_path = node.solution()
        final_path.insert(0, start)
        print('TRACKING PATH: ', ' -> '.join(track_path))
        print('SOLUTION PATH: ', ' -> '.join(final_path))

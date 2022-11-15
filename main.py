import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import erdos_renyi_graph
import math


def valid(solution, graph):
    for i1 in range(len(solution)):
        for i2 in range(i1, len(solution)):
            if graph.has_edge(solution[i1], solution[i2]):
                return False
    return True


def independent_set(k, graph):
    global step
    if n == 0:
        return

    current_vertex = 0
    solution = []

    while len(solution) != 0 or current_vertex != -1:
        step += 1
        if len(solution) == k:
            if valid(solution, graph):
                return solution
            else:
                current_vertex = solution.pop()
        elif current_vertex != -1:
            solution.append(current_vertex)
        else:
            current_vertex = solution.pop()

        if current_vertex == n-1:
            current_vertex = -1
        else:
            current_vertex += 1


def max_independent_set(graph):
    k = 1
    s = True
    last_s = None
    while s:
        last_s = s
        s = independent_set(k, graph)
        k += 1
    return last_s


def max_independent_set_worstcase(graph):
    for k in range(1, n):
        independent_set(k, graph)


def visualize(graph, marked, n):
    color_map = ['blue' for _ in range(n)]
    for node in marked:
        color_map[node] = 'yellow'

    nx.draw(graph, node_color=color_map, with_labels=True)
    plt.savefig("graph.png")


p = 0.5

ns = []
steps = []
worstcase_steps = []

for n in range(1, 10, 1):
    ns.append(n)
    g = erdos_renyi_graph(n, p)
    step = 0
    k = len(max_independent_set(g))
    worstcase_steps.append(k*2*sum([math.comb(n, i) for i in range(n)]))
    steps.append(step)

plt.plot(ns, steps)
plt.plot(ns, worstcase_steps)
plt.legend(["Steps", "Worstcase"], loc="upper left")
plt.savefig("graph.png")

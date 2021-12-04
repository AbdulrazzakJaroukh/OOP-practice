from collections import Counter
from collections import OrderedDict

f = open("input.txt", "r")
problem_lines = f.read().splitlines()

input_as_tuples = [tuple(e.split(" ")) for e in problem_lines]

problem_dict = {}
for tup in input_as_tuples:
    problem_dict[tup[1]] = []

for worker, task, verdict in input_as_tuples:
    problem_dict[task].append(verdict)

sorted_problem_dict = OrderedDict(sorted(problem_dict.items()))

for task in sorted_problem_dict:
    c = Counter(problem_dict[task])
    list_here = c.most_common()
    higher_list = list(filter(lambda e: e if e[1] == list_here[0][1] else None, list_here))
    print(task, min(higher_list)[0])

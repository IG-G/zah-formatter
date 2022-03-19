from typing import List, Tuple


def prepare_list_of_tasks_assigned_to_processors(input_lines: List) -> List:
    elements = []
    for i in range(0, len(input_lines), 4):
        elements.append([input_lines[i], input_lines[i + 1], input_lines[i + 2], input_lines[i + 3]])
    time_q = [int(i[2][4:-1]) for i in elements]
    proc_name = [i[0][4:-1] for i in elements]
    task_number = [i[1][4:-1] for i in elements]
    for count, el in enumerate(elements):
        el[2] = time_q[count]
        el[0] = proc_name[count]
        el[1] = task_number[count]
    elements.sort(key=lambda row: (row[0], row[2]))
    return elements


def split_list_to_processors(elements) -> Tuple:
    # Split list to lists of processors
    procs = {"ProcA": [], "ProcB": [], "ProcC": []}
    for el in elements:
        procs[el[0]].append([el[1], el[2]])
    return procs["ProcA"], procs["ProcB"], procs["ProcC"]


def add_missing_values(a: List, max: int) -> List:
    tmp = []
    for i in range(max):
        if i + 1 not in [i[1] for i in a]:
            tmp.append(["  ", i + 1])
    return sorted(a + tmp)


def print_table(procA: List, procB: List, procC: List) -> None:
    print("      A   B   C")
    for i in range(len(procA)):
        space_flag = ""
        if procA[i][1] < 10:
            space_flag = " "
        print(f"{procA[i][1]}{space_flag} |  {procA[i][0]}  {procB[i][0]}  {procC[i][0]}")


with open("input.txt") as f:
    input_lines_from_file = []
    for count, line in enumerate(f):
        input_lines_from_file.append(line)
assigned_list = prepare_list_of_tasks_assigned_to_processors(input_lines_from_file)
procA, procB, procC = split_list_to_processors(assigned_list)
max_element = max(len(procA), len(procB), len(procC))
procA = add_missing_values(procA, max_element)
procB = add_missing_values(procB, max_element)
procC = add_missing_values(procC, max_element)
print_table(procA, procB, procC)

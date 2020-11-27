import operator

def arithmetic_arranger(problems, result_flag=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    header = ''
    bottom = ''
    result = ''
    dashes = list()
    result_list = list()
    ops = { "+": operator.add, "-": operator.sub }
    arranged = list()
    problems_list = map(lambda x: x.split(" "), problems)
    for problem in problems_list:
        if  problem[0].isdigit() is False or problem[2].isdigit() is False:
            return "Error: Numbers must only contain digits."

        if problem[1] != '+' and problem[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        for align, p in zip('<', problem):
            if len(problem[0]) < len(problem [2]):

                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[2]) + 1), fill='', align=align, width= 2 + len(problem[2]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="", align=align, width= 2 + len(problem[2]) + 4)
                result = str(ops[problem[1]](int(problem[0]), int(problem[2])))
                result = '{0:{fill}{align}{width}}'.format(result.rjust(len(problem[1]) + len(problem[2]) + 1), fill="", align=align, width= 2 + len(problem[2]) + 4)
                result_list.append(result)
                dashes.append((2 + len(problem[2])) * '-')
                
            if len(problem[0]) == len(problem [2]):
                
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill='', align=align, width= 2 + len(problem[0]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="", align=align, width= 2 + len(problem[0]) + 4)
                result = str(ops[problem[1]](int(problem[0]), int(problem[2])))
                result = '{0:{fill}{align}{width}}'.format(result.rjust(len(problem[1]) + len(problem[0]) + 1), fill='', align=align, width= 2 + len(problem[0]) + 4)
                result_list.append(result)
                dashes.append((2 + len(problem[0])) * '-')
            
            if len(problem[0]) > len(problem[2]):
                
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill="", align=align, width= 2 + len(problem[0]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2].rjust(len(problem[0])), fill="", align=align, width= 2 + len(problem[0]) + 4)
                result = str(ops[problem[1]](int(problem[0]), int(problem[2])))
                result = '{0:{fill}{align}{width}}'.format(result.rjust(len(problem[1]) + len(problem[0]) + 1), fill="", align=align, width= 2 + len(problem[0]) + 4)
                result_list.append(result)
                dashes.append((2 + len(problem[0])) * '-')
            

    header = header.rstrip()
    header += header.join("\n")
    bottom = bottom.rstrip()
    bottom += bottom.join("\n")
    dashes = map(lambda x: x.ljust(len(x) + 4), dashes)
    f_dashes = "".join(list(dashes))
    f_dashes = f_dashes.rstrip()
    result = map(lambda x: str(x), result_list)
    f_result = "".join(list(result))
    f_result = f_result.rstrip()
    if result_flag:
        f_dashes += f_dashes.join("\n")
        arranged.append(header + bottom + f_dashes + f_result)
    arranged.append(header + bottom + f_dashes)
    return arranged[0]


print(arithmetic_arranger(["3 + 8553", "4801 - 2", "45 + 43", "123 + 49"]))

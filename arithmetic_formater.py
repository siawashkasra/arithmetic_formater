import operator


def arithmetic_arranger(problems):
    header = ''
    bottom = ''
    result = ''
    dashes = list()
    result_list = list()
    ops = { "+": operator.add, "-": operator.sub }
    arranged = list()
    problems_list = map(lambda x: x.split(" "), problems)
    for problem in problems_list:
        if len(problem[0]) < len(problem [2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[2]) + 1), fill='', align=align, width= 2 + len(problem[2]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="", align=align, width= 2 + len(problem[2]) + 4)
                result = str(ops[problem[1]](int(problem[0]), int(problem[2])))
                result = '{0:{fill}{align}{width}}'.format(result.rjust(len(problem[1]) + len(problem[2]) + 1), fill="", align=align, width= 2 + len(problem[2]) + 4)
            result_list.append(result)
            dashes.append((2 + len(problem[2])) * '-')
                
        if len(problem[0]) == len(problem [2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill='', align=align, width= 2 + len(problem[0]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="", align=align, width= 2 + len(problem[0]) + 4)
                result = str(ops[problem[1]](int(problem[0]), int(problem[2])))
                result = '{0:{fill}{align}{width}}'.format(result.rjust(len(problem[1]) + len(problem[0]) + 1), fill='', align=align, width= 2 + len(problem[0]) + 4)
            result_list.append(result)
            dashes.append((2 + len(problem[0])) * '-')
            
        if len(problem[0]) > len(problem[2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill="", align=align, width= 2 + len(problem[0]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2].rjust(len(problem[0])), fill="", align=align, width= 2 + len(problem[0]) + 4)
                result = str(ops[problem[1]](int(problem[0]), int(problem[2])))
                result = '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill="", align=align, width= 2 + len(problem[0]) + 4)
            result_list.append(result)
            dashes.append((2 + len(problem[0])) * '-')
            

    header += header.join("\n")
    bottom += bottom.join("\n")
    dashes = map(lambda x: x.ljust(len(x) + 4), dashes)
    f_dashes = "".join(list(dashes))
    f_dashes += f_dashes.join("\n")
    result = map(lambda x: str(x), result_list)
    f_result = "".join(list(result))
    arranged.append(header + bottom + f_dashes + f_result)
    return arranged[0]
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
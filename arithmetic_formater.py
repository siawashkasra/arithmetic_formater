def arithmetic_arranger(problems):
    header = ''
    bottom = ''
    dashes = ''
    arranged = list()
    problems_list = map(lambda x: x.split(" "), problems)
    for problem in problems_list:
        if len(problem[0]) < len(problem [2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[2]) + 1), fill='', align=align, width= 2 + len(problem[2]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="", align=align, width= 2 + len(problem[2]) + 4)
                dashes = (2 + len(problem[2])) * '-'
        if len(problem[0]) == len(problem [2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill='', align=align, width= 2 + len(problem[0]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="", align=align, width= 2 + len(problem[0]) + 4)
                dashes = (2 + len(problem[0])) * '-'
        if len(problem[0]) > len(problem[2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill="", align=align, width= 2 + len(problem[0]) + 4)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2].rjust(len(problem[0])), fill="", align=align, width= 2 + len(problem[0]) + 4)
                dashes = (2 + len(problem[2])) * '-'

    header += header.join("\n")
    bottom += bottom.join("\n")
    arranged.append(header + bottom + dashes)
    return arranged[0]
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
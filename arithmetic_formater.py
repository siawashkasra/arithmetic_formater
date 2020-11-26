def arithmetic_arranger(problems):
    header = ''
    bottom = ''
    dashes = ''
    arranged = list()
    problems_list = map(lambda x: x.split(" "), problems)
    for problem in problems_list:
        # if len(problem[0]) < len(problem [2]):
        #     for align, p in zip('<', problem):
        #         header += '{0:{fill}{align}{width}}'.format('{0:{fill}{align}{width}}'.format(p, fill='*', align='>', width=len(problem[2]) + len(p)), fill=align, align=align, width=(len(p) + 4 + len(problem[2])))
        #         bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill=align, align=align, width=(len(problem[2]) + 4 + len(problem[1]) + 1))
        if len(problem[0]) == len(problem [2]):
            for align, p in zip('<', problem):
                header += '{0:{fill}{align}{width}}'.format(problem[0].rjust(len(problem[1]) + len(problem[0]) + 1), fill='*', align=align, width= 2 + len(problem[0]) + 2)
                bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + problem[2], fill="*", align=align, width= 2 + len(problem[0]) + 2)
                dashes = len(bottom) * '-'
        # if len(problem[0]) > len(problem[2]):
        #     for align, p in zip('<', problem):
        #         header += '{0:{fill}{align}{width}}'.format('{0:{fill}{align}{width}}'.format(p, fill='*', align='>', width=len(problem[0]) + 1), fill=align, align=align, width=(len(p) + 4 + len(problem[1])))
        #         bottom += '{0:{fill}{align}{width}}'.format(problem[1].ljust(len(problem[1]) + 1) + '{0:{fill}{align}{width}}'.format(problem[2], fill='*', align='>', width=len(problem[0]) - len(problem[2])), fill=align, align=align, width=(len(problem[2]) + 4 + len(problem[1]) + 1))
                
    header += header.join("\n")
    bottom += bottom.join("\n")
    arranged.append(header + bottom + dashes)
    return arranged[0]
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
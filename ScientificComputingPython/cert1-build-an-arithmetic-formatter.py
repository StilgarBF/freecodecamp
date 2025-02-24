def calculate(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b

def arithmetic_arranger(problems, show_answers=False):
    if(len(problems) > 5):
        return 'Error: Too many problems.'

    exploding_problems = []

    for problem in problems:
        split = problem.split(' ')

        if len(split) != 3:
            return "Error: Problem not properly formated."
        elif split[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        elif not split[0].isdigit() or not split[2].isdigit():
            return "Error: Numbers must only contain digits."
        elif max(len(split[0]), len(split[2])) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        exploding_problems.append({
            'first': split[0],
            'second': split[2],
            'operator': split[1],
            'width': max(len(split[0]),len(split[2])),
            'result': calculate(split[1], int(split[0]), int(split[2]))
        })

    lines = ["", "", "", ""]
    spacer = "    ";

    for problem in exploding_problems:
        lines[0] += f"{problem['first']:>{(problem['width']+2)}}" + spacer
        lines[1] += f"{problem['operator']} {problem['second']:>{(problem['width'])}}" + spacer
        lines[2] += "-" * (int(problem['width']) + 2) + spacer
        lines[3] += f"{problem['result']:>{(problem['width']+2)}}" + spacer
    
    result_str = "\n".join(line.rstrip() for line in lines[:3])

    if show_answers:
        result_str = result_str + "\n" + lines[3].rstrip()
    return result_str

print(f'\n{arithmetic_arranger(["3801 - 2", "8123 + 9049", "123 + 49", "423 - 49"],True)}')
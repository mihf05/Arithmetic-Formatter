def arithmetic_arranger(problems, show_answers=False):
  if (len(problems) > 5):
    return 'Error: Too many problems.'
  
  for problem in problems:
    operand1, operator, operand2 = problem.split(' ')
    for operand in (operand1, operand2):
      if (len(operand) > 4):
        return 'Error: Numbers cannot be more than four digits.'
      for char in operand:
        if (char not in '0123456789'):
          return "Error: Numbers must only contain digits."
    if (operator not in '+-'):
      return "Error: Operator must be '+' or '-'."

  prepared_problems = [arrange_problem(problem, show_answers) for problem in problems]
  line_elements = list(zip(*prepared_problems))
  lines = list(map(lambda elements: (' ' * 4).join(elements), line_elements))
  arranged_problems = '\n'.join(lines)
  return arranged_problems

def arrange_problem(problem, show_answer):
  operand1, operator, operand2 = problem.split(' ')
  width = max(len(operand1), len(operand2)) + 2
  arranged_problem = []
  arranged_problem.append(operand1.rjust(width))
  arranged_problem.append(f'{operator} {operand2.rjust(width-2)}')
  arranged_problem.append('-' * width)
  if (show_answer):
    answer = int(operand1) + int(operand2) if operator == '+' else int(operand1) - int(operand2)
    arranged_problem.append(str(answer).rjust(width))
  return arranged_problem
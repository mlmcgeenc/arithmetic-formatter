testdata = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
import re
def arithmetic_arranger(problems):
  library = []
  # Split each equation string in the list 'problems'
  # Determine the length of the longer operand
  # Solve the equation and add the solution to the dictionary
  # Add whitespace to the operands so they are the same length
  for equation in problems:
    splitEq = equation.split()
    longestOperand = len(max(splitEq, key=len))
    mathResult = 0
    if splitEq[1] == '+':
      mathResult = int(splitEq[0]) + int(splitEq[2])
    else:
      mathResult = int(splitEq[0]) - int(splitEq[2])
    for index, entry in enumerate(splitEq):
      if re.match("^[+-]$", entry) == None:
        splitEq[index] = entry.rjust(longestOperand)
    # !!!!! Before sending to the dictionary we need to build the result and line
    eqDict = ({'line1' : splitEq[0], 'line2' : splitEq[1] + ' ' + splitEq[2], 'line3' :  '----', 'line4' : mathResult})
    library.append(eqDict)
  for dict in library:
    print(dict)

  """  
  multiline = [line1, line2, line3, line4]
  arranged_problems = '\n'.join(multiline)
  """
  arranged_problems = 'In testing'
  return arranged_problems
print(arithmetic_arranger(testdata))
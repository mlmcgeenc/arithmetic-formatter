testdata = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
import re
def arithmetic_arranger(problems):
  library = []
  # Split each equation string in the list 'problems' into it's own list
  for equation in problems:
    # Determine the length of the longer operand
    splitEq = equation.split()
    longestOperand = len(max(splitEq, key=len))
    # Solve the equation
    mathResult = 0
    if splitEq[1] == '+':
      mathResult = int(splitEq[0]) + int(splitEq[2])
    else:
      mathResult = int(splitEq[0]) - int(splitEq[2])
    # Add whitespace to the operands so they are the same length
    for index, entry in enumerate(splitEq):
      if re.match("^[+-]$", entry) == None:
        splitEq[index] = entry.rjust(longestOperand)
    # Build the dividing line
    divider = '-'
    while len(divider) < (longestOperand + 2):
      divider = '-' + divider
      continue
    # Add the operands, divider line, and solution to the library
    eqDict = ({'line1' : '  ' + splitEq[0], 'line2' : splitEq[1] + ' ' + splitEq[2], 'line3' :  divider, 'line4' : str(mathResult).rjust(longestOperand + 2)})
    library.append(eqDict)
  print(str(library[0].get('line1'))+'  '+str(library[1].get('line1'))+'  '+str(library[2].get('line1')))
  print(str(library[0].get('line2'))+'  '+str(library[1].get('line2'))+'  '+str(library[2].get('line2')))
  print(str(library[0].get('line3'))+'  '+str(library[1].get('line3'))+'  '+str(library[2].get('line3')))
  print(str(library[0].get('line4'))+'  '+str(library[1].get('line4'))+'  '+str(library[2].get('line4')))
  #return arranged_problems
print(arithmetic_arranger(testdata))
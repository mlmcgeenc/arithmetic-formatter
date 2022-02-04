#testdata = [["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True]
#testdata = ['3801 - 2', '123 + 49']
#testdata = ['1 + 2', '1 - 9380']
#testdata = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']
#testdata = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
#testdata = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']
#testdata = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']
#testdata = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']
#testdata = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
#testdata = [['3 + 855', '988 + 40'], True]
testdata = [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True]

import re
def arithmetic_arranger(problems, printSol=False):
  newprobs = problems
  if True in problems:
    myprobs = newprobs[0]
    printsolutions = newprobs[1]
  else:
    myprobs = problems
    printsolutions = False

  # Check to make sure there are no more than 5 equations
  if len(myprobs) > 5:
    return "Error: Too many problems."
  library = []

  # Split each equation string in the list 'problems' into it's own list
  for equation in myprobs:
    if re.findall('[a-zA-Z]', str(equation)) != []:
      return 'Error: Numbers must only contain digits.'
    splitEq = equation.split()

    # Determine the length of the longer operand
    longestOperand = len(max(splitEq, key=len))
    if longestOperand > 4:
      return "Error: Numbers cannot be more than four digits."

    # Solve the equation
    mathResult = 0
    if re.findall('[*/]', splitEq[1]) != []:
      return "Error: Operator must be '+' or '-'." 
    if splitEq[1] == '+':
      mathResult = int(splitEq[0]) + int(splitEq[2])
    else:
      mathResult = int(splitEq[0]) - int(splitEq[2])

    # Add whitespace to the shorter operand so the two are the same length
    for index, entry in enumerate(splitEq):
      if re.match("^[+-]$", entry) == None:
        splitEq[index] = entry.rjust(longestOperand)

    # Build the dividing line
    divider = '-'
    while len(divider) < (longestOperand + 2):
      divider = '-' + divider
      continue

    # Add the first operand, operator and operand, dividing line, and solution to a dictionary,
    # and add the dictionary to the library
    eqDict = ({'line0' : '  ' + splitEq[0], 'line1' : splitEq[1] + ' ' + splitEq[2], 'line2' :  divider, 'line3' : str(mathResult).rjust(longestOperand + 2)})
    library.append(eqDict)

  # Create an array that will hold the formatted strings before printing to the screen
  if printsolutions == True:
    multiLine = ['', '', '', '']
  else:
    multiLine = ['', '', '']
  
  # Create strings from dictionary values contained in the library list
  count = 0
  for libDict in library:
    if count + 1 != len(library):
      multiLine[0] = multiLine[0] + libDict['line0'] + '    '
      multiLine[1] = multiLine[1] + libDict['line1'] + '    '
      multiLine[2] = multiLine[2] + libDict['line2'] + '    '
      if printsolutions == True:
        multiLine[3] = multiLine[3] + libDict['line3'] + '    '
      count += 1
    else:
      multiLine[0] = multiLine[0] + libDict['line0'] + "\n"
      multiLine[1] = multiLine[1] + libDict['line1'] + "\n"
      multiLine[2] = multiLine[2] + libDict['line2'] + "\n"
      if printsolutions == True:
        multiLine[3] = multiLine[3] + libDict['line3'] + "\n"
    continue
  # Join strings with breaks in the appropriate places and return for printing 
  arranged_problems = "".join(multiLine)
  print(multiLine)
  return arranged_problems
print(arithmetic_arranger(testdata))
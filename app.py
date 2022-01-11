testdata = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems):
  library = []
  # Split each equation string in the list 'problems' 
  # into it's own list and assign the operands and 
  # operator to keys in a dictionary, then add the
  # new dictionary to the list 'library'
  for equation in problems:
    splitEq = equation.split()
    longestOperand = len(max(splitEq, key=len))
    mathResult = 0
    if splitEq[1] == '+':
      mathResult = int(splitEq[0]) + int(splitEq[2])
    else:
      mathResult = int(splitEq[0]) - int(splitEq[2])
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
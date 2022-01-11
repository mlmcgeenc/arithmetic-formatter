testdata = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems):
  # Determine how many equations are in the input list
  problemsCount = len(problems)

  library = []
  # Split each equation string in the list 'problems' 
  # into it's own list and assign the operands and 
  # operator to keys in a dictionary, then add the
  # new dictionary to the list 'library'
  for equation in problems:
    splitEq = equation.split()
    if len(splitEq[0]) > len(splitEq[2]):
      print('Bypass for now')
    eqDict = ({'var1' : splitEq[0], 'operator' : splitEq[1], 'var2' :  splitEq[2]})
    library.append(eqDict)
  for dict in library:
    print(dict)







  """
  # Set maxLen to the length of the longer of the two operands
  maxLen = 0
  for value in myDict.values():
    if len(value) > maxLen:
      maxLen = len(value)
      continue
  # Apply that length to the shorter operand
  for key in myDict.keys():
    if len(myDict[key]) < maxLen:
      myDict.update({key : ' ' + myDict[key]})
  print(myDict)
  
  # Build a string from parallel indexes in each equation
  for problem in splitProblems:
    line1 = line1 + problem[0] + ' '
    line2 = line2 + problem[1] + ' ' + problem[2]
    line3 = line3 + '----' + ' '
    # Build a string of results by processing the equations
    if problem[1] == '+':
      line4 = line4 + str(int(problem[0]) + int(problem[2])) + ' '
    else:
      line4 = line4 + str(int(problem[0]) - int(problem[2])) + ' '
  
  multiline = [line1, line2, line3, line4]
  arranged_problems = '\n'.join(multiline)
  """
  arranged_problems = 'In testing'
  return arranged_problems
print(arithmetic_arranger(testdata))
testdata = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems):
  # Determine how many equations are in the input list
  problemsCount = len(problems)

  # Initialize the dictionary that will hold calues before printing
  library = {}

  # Initialize the 4 lines that will be displayed in the output
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''

  # Split each equation string in the 'problems' list into it's own list
  splitProblems = []
  for problem in problems:
    splitProblems.append(problem.split()) 

  library.update({'var1' : splitProblems[0][0],'operator' : splitProblems[0][1], 'var2' : splitProblems[0][2]})
  print(library)

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
  return arranged_problems
print(arithmetic_arranger(testdata))
testdata = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems):
  splitProblems = []
  for problem in problems:
    splitProblems.append(problem.split())
  
  line1 = ''
  line2 = ''
  line3 = ''
  for problem in splitProblems:
    line1 = line1 + problem[0] + ' '
    line2 = line2 + problem[1] + ' ' + problem[2]
    line3 = line3 + '----' + ' '
  
  multiline = [line1, line2, line3]
  arranged_problems = '\n'.join(multiline)
  return arranged_problems
print(arithmetic_arranger(testdata))
import re

def arithmetic_arranger(problems, solve = False):
  arranged_problems = ""

  if len(problems) > 5: return "Error: Too many problems."

  for i in range(len(problems)):
    arr = problems[i].split()
    if arr[1] != "+" and arr[1] != "-": return "Error: Operator must be '+' or '-'."
    elif re.search("[^\s0-9.+-]", problems[i]): return "Error: Numbers must only contain digits."
    elif len(arr[0]) > 4 or len(arr[2]) > 4: return "Error: Numbers cannot be more than four digits."
    if i != 0: arranged_problems += "    "

    if len(arr[0]) < len(arr[1]) + len(arr[2]):
      for k in range(len(arr[1]) + len(arr[2]) - len(arr[0])):
        arranged_problems += " "
    else: arranged_problems += " "
    
    arranged_problems += " " + arr[0]

  arranged_problems += "\n"

  for j in range(len(problems)):
    arr = problems[j].split()
    if j != 0: arranged_problems += "    "
    arranged_problems += arr[1] + " "

    if len(arr[0]) > len(arr[2]):
      for k in range(len(arr[0]) - len(arr[1]) - len(arr[2]) + 1):
        arranged_problems += " "

    arranged_problems += arr[2]

  arranged_problems += "\n"

  for l in range(len(problems)):
    arr = problems[l].split()
    if l != 0: arranged_problems += "    "
    if len(arr[0]) > len(arr[2]):
      for space in range(len(arr[0]) + 2):
        arranged_problems += "-"
    else:
      for space in range(len(arr[2]) + 2):
        arranged_problems += "-"

  if solve == True:
    arranged_problems += "\n"
    for m in range(len(problems)):
      arr = problems[m].split()
      if m != 0: arranged_problems += "    "
      if arr[1] == "+": result = str(int(arr[0]) + int(arr[2]))
      else: result = str(int(arr[0]) - int(arr[2]))

      if len(result) < len(arr[0]) + 2 and len(arr[0]) > len(arr[2]):
        for n in range(len(arr[0]) + 2 - len(result)):
          arranged_problems += " "
      elif len(result) < len(arr[2]) + 2:
        for space in range(len(arr[2]) + 2 - len(result)):
          arranged_problems += " "

      arranged_problems += result

  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
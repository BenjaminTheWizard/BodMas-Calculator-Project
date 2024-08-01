import os
answer = float()

def calculate(aithmetic):
  def format():
    delete_following = num_list.count('')
    for x in range(0,delete_following):
      num_list.remove('')
  num_list = aithmetic
  global answer
  x = 0
  while True:
    if num_list.count('*') == 0:
      break
      return 'Done'
    if num_list[x-1] == "*":
      num_list[x-2] = num_list[x-2] * num_list[x]
      num_list.remove(num_list[x-1])
      num_list.remove(num_list[x-1])
      for y in range(2):
        num_list.append('')
      x = 0
    x+=1
  format()

  while True:
    if num_list.count('**') == 0:
      break
      return 'Done'
    if num_list[x-1] == "**":
      num_list[x-2] = num_list[x-2] ** num_list[x]
      num_list.remove(num_list[x-1])
      num_list.remove(num_list[x-1])
      for y in range(2):
        num_list.append('')
      x = 0
    x+=1
  format()
    
  while True:
      if num_list.count('/') == 0:
        break
        return 'Done'
      if num_list[x-1] == "/":
        num_list[x-2] = num_list[x-2] / num_list[x]
        num_list.remove(num_list[x-1])
        num_list.remove(num_list[x-1])
        for y in range(2):
          num_list.append('')
        x = 0
      x+=1
  format()
    
  while True:
      if num_list.count('+') == 0:
        break
        return 'Done'
      if num_list[x-1] == "+":
        num_list[0] = num_list[0] + num_list[x]
        num_list.remove(num_list[x-1])
        num_list.remove(num_list[x-1])
        for y in range(2):
          num_list.append('')
        x = 0
      x+=1
  format()

  while True:
      if num_list.count('-') == 0:
        break
        return 'Done'
      if num_list[x-1] == "-":
        num_list[0] = num_list[0] - num_list[x]
        num_list.remove(num_list[x-1])
        num_list.remove(num_list[x-1])
        for y in range(2):
          num_list.append('')
        x = 0
      x+=1
  answer = num_list[0]
  format()

def menu():
  number_input = False
  number_just_inputted = False
  op_input = False
  equ = []
  problem = ""
  while True:
    print("_-_-_-_-_-_-_-_-_-_-_-_-\n|    My Calculator!    |\n_-_-_-_-_-_-_-_-_-_-_-_-")
    print("\nCurrent operations:\n+: to add\n-: to subtract\n*: to multiply\n**: to add powers to numbers\n/: to divide\n\nCommands:\nclr: to clear the math problem\n=: for the answer to be returned\n\nType a single number/operation/command into the console.")
    print(problem)
    choice = input(": ")
    if choice == "clr":
      number_input = False
      number_just_inputted = False
      op_input = False
      equ = []
      problem = ""
    elif choice == "=":
      if number_input == False:
        print()
      else:
        try:
          calculate(equ)
        except:
          print('\nAn error occurred.')
          input("\nPress enter: ")
        else:
          print(f"\n{answer}")
          input("\nPress enter: ")
    elif choice == "+":
      if number_input == False:
        print()
      else:
        if op_input == False:
          op_input = True
          problem = problem+'+'
          equ.append('+')
          number_just_inputted = False
    elif choice == "**":
      if number_input == False:
        print()
      else:
        if op_input == False:
          op_input = True
          problem = problem+'**'
          equ.append('**')
          number_just_inputted = False
    elif choice == "-":
      if number_input == False:
        print()
      else:
        if op_input == False:
          op_input = True
          problem = problem+'-'
          equ.append('-')
          number_just_inputted = False
    elif choice == "*":
      if number_input == False:
        print()
      else:
        if op_input == False:
          op_input = True
          problem = problem+'x'
          equ.append('*')
          number_just_inputted = False
    elif choice == "/":
      if number_input == False:
        print()
      else:
        if op_input == False:
          op_input = True
          problem = problem+'÷'
          equ.append('/')
          number_just_inputted = False
    else:
      if number_just_inputted == False:
        number_just_inputted = True
        try:
          float(choice)
          number_input = True
          op_input = False
          problem = problem+choice
          equ.append(float(choice))
        except:
          print("That is not a operator or number.")
          input('Press enter: ')
        else:
          print("Number just has been inputted.")
          input('Press enter: ')
    os.system("clear")
menu()

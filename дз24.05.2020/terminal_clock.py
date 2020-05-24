
import time
import os
import datetime
import ctypes
import platform

opsys = platform.platform()
if opsys  == 'MacOS':
     ctypes.windll.kernel32.SetConsoleTitleA("Python Clock")
     os.system("mode con: cols=90 lines=11")

list = [
'''
██████
██  ██
██  ██
██  ██
██████''',
'''
  ██
████
  ██
  ██
██████''',
'''
██████
    ██
██████
██
██████''',
'''
██████
    ██
██████
    ██
██████''',
 '''
██  ██
██  ██
██████
    ██
    ██''',
'''
██████
██
██████
    ██
██████''',
'''
██████
██
██████
██  ██
██████''',
'''
██████
    ██
    ██
    ██
    ██''',
'''
██████
██  ██
██████
██  ██
██████''',
 '''
██████
██  ██
██████
    ██
██████'''
]
colon = '''

  ██

  ██
      '''

done = True
while(done):

    if opsys == 'MacOS':
         os.system('cls')
    else:
        print ("\n"*15)

    ti = str(datetime.datetime.now())
    ti = ti[11:19]

    lines = ["","","","","","","","",""]
    line = 0

    numbers = [[],[],[],[],[],[],[],[]]
    for x in range(8):
        if ti[x].isdigit():

            numbers[x] = list[int(ti[x])].splitlines()
        elif ti[x] == ":":
            numbers[x] = colon.splitlines()

    for x in range(9):
        temp = ""
        for i in range(9):

            try:
                if i != 8:
                    temp += str(numbers[i][line]).ljust(10)
                else:
                    temp += str(numbers[i][line])
            except:
                temp += "          "
        lines[x] += temp
        line += 1


    for x in range(9):
        print (lines[x])

    print
    time.sleep(.2)
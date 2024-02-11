[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/_qDY-9qJ)
# tPythonModule03
tPythonModule03

Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than an integer, detect their mistake using try and except and print an error message and skip to the next integers.

Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

Code up Worked Exercise 6.5 as viewed in the video. This program involves prompting the user for a list of numbers, storing these numbers in a list, and then calculating the maximum and minimum numbers after the user has finished entering their numbers. The user indicates they are done by entering "done". Here's how you could implement this in Python.

---

## Video 5 (Exercise 5.1)

`num = 0`
`tot = 0.0`
`while True :`
    `sval = input('Enter a number: ')`
    `if sval == 'done' :`
        `break`
    `try:`
        `fval = float(sval)`
    `except:`
        `print('Invalid input')`
        `continue`
   `# print(fval)`
    `num = num + 1`
    `tot = tot + fval`

`# print('ALL DONE')`
`print(tot,num,tot/num)`

### Windows PowerShell Terminal

(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
Five
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
1.0
Enter a number: 2
2.0
Enter a number: 3
3.0
Enter a number: bad
Traceback (most recent call last):
  File "C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python\iterationsModule3.py", line 5, in <module>
    fval = float(sval)
           ^^^^^^^^^^^
ValueError: could not convert string to float: 'bad'
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
1.0
Enter a number: 2
2.0
Enter a number: 3
3.0
Enter a number: done
Traceback (most recent call last):
  File "C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python\iterationsModule3.py", line 5, in <module>
    fval = float(sval)
           ^^^^^^^^^^^
ValueError: could not convert string to float: 'done'
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
Enter a number: 4
ALL DONE
4.0 1 4.0
Enter a number: 5
5.0
ALL DONE
9.0 2 4.5
Enter a number: 6
6.0
ALL DONE
Enter a number: done
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
Enter a number: 4
4.0
Enter a number: 5
5.0
Enter a number: 6
6.0
Enter a number: done
15.0 3 5.0
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
Enter a number: 4
Enter a number: 5
Enter a number: 6
Enter a number: sljddsjkl
Traceback (most recent call last):
  File "C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python\iterationsModule3.py", line 7, in <module>
    fval = float(sval)
           ^^^^^^^^^^^
ValueError: could not convert string to float: 'sljddsjkl'
(.venv) PS C:\Users\Brendan\PycharmProjects\CIT95SPRING2024\CIT95python> py iterationsModule3.py
Enter a number: sdjk
Invalid input
Enter a number: kjhsd
Invalid input
Enter a number: kshdj
Invalid input
Enter a number: sdkjh
Invalid input
Enter a number: 4
Enter a number: 5
Enter a number: 6
Enter a number: jdjds
Invalid input
Enter a number: dfjfdjk
Invalid input
Enter a number: done
15.0 3 5.0

---

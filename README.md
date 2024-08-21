# Lab 1 - CIST 1600

## Overview
- Look at different ways of creating/running a Python program.
- Create a GitHub account.
- Open GitHub Classroom and GitHub Code Spaces

---
### Text Editor
- How to configure Python on your home computers
  - Download Python
    - [python.org](https://www.python.org/)
  - Download a Text Editor
    - [Atom.io](https://atom.io/)
    - [Notepad++](https://notepad-plus-plus.org/downloads/)
    - [Sublime Text](https://www.sublimetext.com/)
  - In a command-line interface:
    - Navigate to the folder with your python file.
    - Use command **python file.py** where ***file*** is changed for the name of your file.
    - Depending on configuration, the command may be **python3 file.py**

### IDLE Editor
- IDE that comes with Python when you download
- Opens to an interactive shell
- You can run scripts by from the **Run** menu and choosing **Run Script**
  - Alternatively you can type **F5** on your keyboard

## Instructions
- Log into GitHub and Canvas
- Accept the assignment from GitHub Classroom in Canvas
- Open in GitHub Code Spaces

Now that we have the files in GitHub, we will start to work with the Python file.

## FirstProgram.py
The instructions for the program is in code. In python, a pound sign (#) is used to denote a comment. This is code that will not execute and is only there for the benefit of the programmer.

Please label all of your work. There is an area at the top of the code for the file name, your name, the purpose of the file, and the last revision date. Please update all of this info.
```
#FirstProgram.py
#Name:
#Date:
#Assignment: Lab 1
#Purpose: To ask a user for their name, and calculate their birth year.
```
- We are going to make a program that that says hello and asks for your name.  
- We have not yet used input, you will need the following code to make it work. Experiment to answer these questions.
  - Do I need a prompt or can I simply get input?
  - How do I use the value the user just gave me?
  - What is the data type of the value the user just gave me?
    - Can it be printed?
    - What happens if it is a number and we try to do math with it?
    - Can I convert data types if this one is not correct for my needs?

```
answer = input("This is a prompt for info: ")
print(answer)
```

## MadLib.py
Create a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) where the user supplies key adjectives, nouns, verbs, adverbs, or other types of speech then constructs a full story with those words.

Your Mad Lib must:
- Ask for at least 6 words
- Consider usability in design (be clear)
- Create a story with the user supplied words.

There are a few ways to join words in python:

```
noun1 = "Bicycle"
print("I like to ride my " + noun1)
print("I like to ride my", noun1)
```
Test which works best for you, note where the spaces fall using the different methods.

Please remember to fill in all of the info at the top of the document.


## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
Submit your work in GitHub Classroom

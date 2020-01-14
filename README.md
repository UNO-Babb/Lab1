# Lab 1 - CYBR 2890

## Overview
- Setup GitHub account
  - [GitHub.com](https://www.github.com)
- How to configure Python on your home computers
  - Download Python
    - [python.org](https://www.python.org/)
  - Download Atom
    - [Atom.io](https://atom.io/)
  - Install Script addon in Atom
    - File -> Settings
    - Install -> Search Script
    - Click Install on the top search hit (with 2.2 million downloads)

## Instructions
- Accept the Lab 1 assignment from GitHub classroom. You can find the assignment on Canvas.
- Once you've cloned the repository, get the link from GitHub
- Open Atom on your computer
  - Type Ctrl + Alt + P in Atom
  - Search for "GitHub: Clone" in Atom
  - Paste the link from GitHub in the popup

Now that we have the files on your computer, we will start to work with the Python file.

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

## Magic8Ball.py
Create a program that will allow the user to ask a question, then provide a random response like a Magic 8 Ball.

- A traditional Magic 8 Ball has 20 possible answers:
- As I see it, yes.
- Ask again later.
- Better not tell you now.
- Cannot predict now.
- Concentrate and ask again.
- Don’t count on it.
- It is certain.
- It is decidedly so.
- Most likely.
- My reply is no.
- My sources say no.
- Outlook not so good.
- Outlook good.
- Reply hazy, try again.
- Signs point to yes.
- Very doubtful.
- Without a doubt.
- Yes.
- Yes – definitely.
- You may rely on it.

You may select to use these or answers you have created. They key is that they are given a random answer to the question they ask.

How to create a list of possible answers:
```
answers = ["thing 1", "thing 2"] # Each item must be in quotes, separated by a comma.
```
Since we imported random at the top of our file, we can use the following code to select a random item from the list.
```
response = random.choice(answers)
```

## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
Use Atom Git window to stage changes and push. If you are not done, you will still want to push changes so you can continue to work on this later.

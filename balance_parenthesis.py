from node_stack import *
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""

# I have had a   time trying to import node_stack.py from my email; Please excuse any errors that pop up in those terms.
def balance_parenthesis(a_string):
    line_stack = Stack()
    last_open_bracket = None # Current index of a open bracket
    closed_bracket_num = 0 # Total closed bracket
    open_bracket_num = 0 # Total open Bracket
    
    for letter in a_string: #puts everything in the stack
        line_stack.push(letter)
    
    currrent_index = len(line_stack)-1 # Where we are in a_string logistically (reversed; first in - last out)
    
    while len(line_stack) > 0: #Takes everything off the stack one-by-one and works the data.
        work_letter = line_stack.pop()
        if work_letter != '-': #Ignores the letter if a dash (still iterates)
            if work_letter == ')':
                closed_bracket_num +=1
            elif work_letter == '(':
                last_open_bracket = currrent_index
                open_bracket_num +=1 
        currrent_index-=1
    
    if closed_bracket_num == open_bracket_num: return 0 #Everythings balanced
    elif closed_bracket_num > open_bracket_num: return -1 # 1+ extra closed brackets
    else: return last_open_bracket #The location of the  open bracket.




# Manual testing / debugging - Good news, it passes the examples!
def main():   
    result = balance_parenthesis("-----() -- ( () )")
    print(result)

if __name__ == "__main__":    main()
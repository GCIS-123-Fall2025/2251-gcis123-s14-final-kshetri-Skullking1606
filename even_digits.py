#import node_stack
from dict_queue import *
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #4 (25 points)
Filename: even_digits.py

Define a function named "even_digits" that declares a parameter for an 
    integer. The function should return a copy of the integer with the odd
    digits removed. You MUST NOT convert the integer to/from a string, but 
    instead may only use basic arithmetic operators (e.g. %, //, etc.).

    Given Input     Expected Output
    1               0
    2               2
    34              4
    1234567890      24680

For credit your function must use a stack or a queue in a significant way.
    You must not use any other data structures. For full credit, your 
    implementation must run in linear time.
"""

def even_digits(integer):
    digit_queue = Queue()
    mod_slot = 10 # Singling out each digit
    difference = 0 #Used to subtract numbers in lower places (ex: 17 - 7 = 10)
    while True:
        try:
            difference += digit_queue.back()
        except IndexError: # Throws an IndexError @ the ones place (queue MT)
            pass
        digit_queue.enqueue(((integer-difference)%mod_slot))
        mod_slot *= 10
        if integer % mod_slot == integer: break # Not the greatest case to break a loop but the next line of code ensures each numerical place is queued.
    digit_queue.enqueue(integer-(digit_queue.back()+difference))

    final_number = 0 # Return Variable
    tens_place = 1 #How it gets returned as a digit post-even check
    while len(digit_queue) > 0:
        current_num = digit_queue.dequeue()
        while current_num >= 10:
            current_num /= 10

        if int(current_num) % 2 == 0: 
            final_number += current_num * tens_place
            tens_place *= 10
        
    return(int(final_number))
        
    

# several test cases provided for even digits - 1, 2, 34, 1234567890
def test_even_digits_1():
    # setup
    integer = 1
    expected = 0
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_2():
    # setup
    integer = 2
    expected = 2
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_34():
    # setup
    integer = 34
    expected = 4
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_1234567890():
    # setup
    integer = 1234567890
    expected = 24680
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual
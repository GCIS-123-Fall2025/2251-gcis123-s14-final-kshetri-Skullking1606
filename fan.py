"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #2 (25 points)
Filename: fan.py

Complete the Fan class and functions below to keep track of the state of the fan.
Ensure that fields are limited to only the defined state and that a constructor
is provided.

State
    Brand (string) - the brand name of the fan
    Is On (boolean) - keeps track whether or not the fan is on
    Spped (integer) - the speed of the current fan

Constructor: 
    Accepts a brand name.  The fan should default to off and a speed of 0
"""
class Fan:
    pass # please replace with your solution
    

"""
Complete the turn_on function below to update the state of the fan.
Parameters:     
    fan - a fan object
    speed - the speed of the fan.  Must be between 1 and 10 (inclusive).  If outside
        of that range, do not change the state of the fan.
Returns:
    True - if the speed was valid and fan is on.
    False - otherwise

"""
def turn_on(fan,speed):
    pass # please replace with your solution
    

"""
Complete the turn_off function below to update the state of the fan.  When a fan is off,
the speed resets to 0.
Parameters:    fan - a fan object
Returns:    None
"""
def turn_off(fan):
    pass # please replace with your solution
    

"""
Complete the get_state function below.
Parameters:     fan - a fan object
Returns:    Tuple - in the form of (brand, is on, speed)
Example:
    fan = Fan("Holmes")
    get_state(fan) returns ("Holmes", False, 0)
    turn_on(fan,3)
    get_state(fan) returns ("Holmes", True, 3)
More test cases in main() method
"""
def get_state(fan):
    return (fan.brand, fan.is_on, fan.speed)


def main():
    fan = Fan("Holmes")
    assert get_state(fan) == ("Holmes", False, 0)
    assert turn_on(fan,3) == True
    assert get_state(fan) == ("Holmes", True, 3)
    turn_off(fan)
    assert get_state(fan) == ("Holmes", False, 0)
    assert turn_on(fan,5) == True
    assert get_state(fan) == ("Holmes", True, 5)
    assert turn_on(fan,11) == False
    assert get_state(fan) == ("Holmes", True, 5)

if __name__ == "__main__":    main()
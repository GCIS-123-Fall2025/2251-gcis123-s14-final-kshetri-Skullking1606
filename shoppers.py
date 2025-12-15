"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ['__item_code','__name','__price']

    def __init__(self,item_code,name,price):
        self.__item_code = item_code
        self.__name = name
        self.__price = price
        
    def get_item_code(self):
        return self.__item_code

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return "("+ self.__item_code +","+ self.__name +","+ str(self.__price) +")"

    def __eq__(self, value):
        if type(value) == type(self):
            if self.__item_code == value.get_item_code(): return True
        return False
    
    def __hash__(self):
        return hash(self) # Was not taught formally; Best Guess given.

# Missing sort Method - Unsure on that one. Partial working code :)


# manual test from main() method
def main():     
    my_item_one = Item('AEH-YU','R.A.M.',9999)
    print(my_item_one)
    my_item_two = Item('GEH-SUM','Lettuce', 27)
    print(my_item_two)
 

if __name__ == "__main__":    main()
class Queue:
    __slots__ = ['__elements', '__front', '__back']

    def __init__(self):
        self.__elements = {}
        self.__front = 0
        self.__back = 0

    def __repr__ (self):
        values = []
        for index in range(self.__front, self.__back):
            values.append(self.__elements[index])
        return str (values)
    
    def is_empty(self):
        return len(self.__elements) == 0
    
    def __len__(self):
        return len (self.__elements)

    def enqueue(self, value):
        self.__elements[self.__back] = value
        self.__back += 1

    def front (self):
        if not self.is_empty():
            return self.__elements[self.__front]
        else:
            raise IndexError("Queue is empty")

    def back(self):
        if not self.is_empty():
            return self.__elements[self.__back - 1]
        else:
            raise IndexError("Queue is empty")

    def dequeue(self):
        if not self.is_empty():
            value = self.__elements.pop(self.__front)
            self.__front += 1
            return value 
        else:
            raise IndexError("Queue is empty")

def main():
    queue = Queue()
    print(queue)

    print(queue.is_empty())
    print(len(queue))

    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')
    print(len(queue))
    print(queue)

    print(queue.front())
    print(queue.back())


    while not queue.is_empty():
        print("Removed", queue.dequeue())
        print(len(queue))
        print(queue)
        
        if not queue.is_empty():
            print(queue.front())
            print(queue.back())

if __name__ == "__main__":
    main ()
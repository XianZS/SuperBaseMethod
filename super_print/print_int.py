"""
    Interface Print Int
"""
from abc import ABC,abstractmethod

class Interface_print_int(ABC):
    @abstractmethod
    def enter(self,rdd:int)->tuple:
        """
            rdd type is int
            return value type is tuple
        """

class Base_print_int(Interface_print_int):
    def enter(self,rdd:int)->tuple:
        print("<---")
        print("<- type:int ->")
        print(f"\t{rdd}")
        print("--->")



if __name__=="__main__":
    bpi=Base_print_int()
    bpi.enter(1)



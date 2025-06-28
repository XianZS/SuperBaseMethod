"""
    Interface Print Bool
"""
from abc import ABC,abstractmethod

class Interface_print_bool(ABC):
    @abstractmethod
    def enter(self,rdd:bool)->tuple:
        """
            rdd type is bool
            return type is tuple
        """

class Base_print_bool(Interface_print_bool):
    def enter(self,rdd:bool)->tuple:
        print("<---")
        print("<- type:bool ->")
        print(f"\t{rdd}")
        print("--->")



if __name__=="__main__":
    bpb=Base_print_bool()
    bpb.enter(True)

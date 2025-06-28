"""
    Interface Print Float
"""
from abc import ABC,abstractmethod

class Interface_print_float(ABC):
    @abstractmethod
    def enter(self,rdd:float)->tuple:
        """
            rdd type is float
            return value type is tuple
        """

class Base_print_float(Interface_print_float):
    def enter(self,rdd:float)->tuple:
        print("<---")
        print("<- type:float ->")
        print(f"\t{rdd}")
        print("--->")



if __name__=="__main__":
    bpf=Base_print_float()
    bpf.enter(3.3)

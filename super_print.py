from abc import ABC, abstractmethod
from collections import deque
import itertools
import math
import typing


class IPublic(ABC):
    def sprint(self,rdd:typing.Any)->tuple:
        """
            rdd:typing.Any
        """

class IPrivate(ABC):
    @abstractmethod
    def __super_print_int(self, rdd: int) -> tuple:
        """
            rdd:int
        """

    @abstractmethod
    def __super_print_float(self,rdd:float)->tuple:
        """
            rdd:float
        """

    @abstractmethod
    def __super_print_bool(self,rdd:bool)->tuple:
        """
            rdd:bool
        """

    @abstractmethod
    def __super_print_list(self,rdd:list)->tuple:
        """
            rdd:list
        """

    @abstractmethod
    def __super_print_tuple(self,rdd:tuple)->tuple:
        """
            rdd:tuple
        """

    @abstractmethod
    def __super_print_set(self,rdd:set)->tuple:
        """
            rdd:set
        """

    @abstractmethod
    def __super_print_dict(self,rdd:dict)->tuple:
        """
            rdd:dict
        """

    @abstractmethod
    def __super_print_str(self,rdd:str)->tuple:
        """
            rdd:str
        """

    @abstractmethod
    def __judge_type(self,rdd:typing.Any,rdd_type:type)->tuple:
        """
            rdd:typing.Any
            rdd_type:type
        """


class Base(IPublic,IPrivate):
    def __judge_type(self,rdd:typing.Any,rdd_type:type)->tuple:
        try:
            if type(rdd)==rdd_type:
                return rdd,True
            else:
                return rdd,False
        except Exception as e:
            return e,False

    def __super_print_int(self,rdd:int)->tuple:
        rdd,ok=self.__judge_type(rdd,int)
        if ok:
            print(f"<- int: {rdd} ->")
            return rdd,True
        else:
            return rdd,False

    def __super_print_float(self,rdd:float)->tuple:
        rdd,ok=self.__judge_type(rdd,float)
        if ok:
            print(f"<- float: {rdd} ->")
            return rdd,True
        else:
            return rdd,False

    def __super_print_str(self,rdd:str)->tuple:
        rdd,ok=self.__judge_type(rdd,str)
        if ok:
            print(f"<- str: {rdd} ->")
            return rdd,True
        else:
            return rdd,False

    def __super_print_bool(self,rdd:bool)->tuple:
        rdd,ok=self.__judge_type(rdd,bool)
        if ok:
            print(f"<- bool: {rdd} ->")
            return rdd,True
        else:
            return rdd,False

    def __super_print_list(self,rdd:list)->tuple:
        rdd,ok=self.__judge_type(rdd,list)
        if ok

def test() -> tuple:
    return 1, True


if __name__ == "__main__":
    test()

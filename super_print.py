import typing
from abc import ABC,abstractmethod
from collections import deque

class IPublic(ABC):
    @abstractmethod
    def only_one_level_print(self,rdd:typing.Any)->tuple:
        """
            only_one_level_print function
            args:
                rdd:typing.Any
            childrens:
                int,float,bool,str,one_level_list,set,one_level_tuple
        """

    @abstractmethod
    def some_level_print(self,rdd:typing.Any)->tuple:
        """
            some_level_print function
            args:
                rdd:typing.Any4
            childrens:
                some_level_list,some_level_tuple
        """

    @abstractmethod
    def dict_print(self,rdd)->tuple:
        """
            dict_print function
            args:
                rdd:dict
            childrens:
                dict
        """

    @abstractmethod
    def sprint(self,rdd)->tuple:
        """
            sprint function
            args:
                rdd:typing.Any
        """



class Base_one(IPublic):
    def only_one_level_print(self,rdd)->tuple:
        try:
            print(f"<- rdd:{type(rdd)} ->")
            if type(rdd)==int or type(rdd)==float or type(rdd)==bool or type(rdd)==str:
                print("\t",f"{rdd}")
                return rdd,False
            if type(rdd)==list:
                print("\t"," ".join(str(cho) for cho in rdd))
                return rdd,True
            if type(rdd)==tuple:
                print("\t"," ".join(str(cho) for cho in rdd))
                return rdd,True
            if type(rdd)==set:
                print("\t"," ".join(str(cho) for cho in list(rdd)))
                return rdd,True
            return rdd,False
        except Exception as e:
            print(e)
            return e,False

    def some_level_print(self,rdd)->tuple:
        try:
            c=len(rdd)
            if c==1:
                return rdd,False
            print(f"<- rdd:{type(rdd)} ->")
            if type(rdd)==list or type(rdd)==tuple:
                for x in range(c):
                    print(" ".join(str(cho) for cho in rdd[x]))
                return rdd,True
            else:
                return rdd,False
        except Exception as e:
            print(e)
            return e,False

    def __dict_print(self,childs_dict:dict)->tuple:
        if type(childs_dict)!=dict:
            print(childs_dict)
            return childs_dict,True
        key_list=list(childs_dict)
        for key in key_list:
            print(f"{key}:")
            self.__dict_print(childs_dict[key])
        return childs_dict,True

    def dict_print(self,rdd)->tuple:
        try:
            print(f"<- rdd:{type(rdd)} ->")
            _,ok=self.__dict_print(rdd)
            if ok:
                return rdd,True
            else:
                return rdd,False
        except Exception as e:
            print(e)
            return e,False

    def __get_depth_list(self,rdd)->int:
        if isinstance(rdd,list):
            return 1+max(self.__get_depth_list(item) for item in rdd)
        else:
            return 0
    def __get_depth_tuple(self,rdd)->int:
        if isinstance(rdd,tuple):
            return 1+max(self.__get_depth_tuple(item) for item in rdd)
        else:
            return 0

    def sprint(self,rdd)->tuple:
        try:
            if (type(rdd)==int) or (type(rdd)==set) or (type(rdd)==float) or (type(rdd)==bool) or (type(rdd)==str) or (type(rdd)==list and self.__get_depth_list(rdd)==1) or (type(rdd)==tuple and self.__get_depth_tuple(rdd)==1):
                _,ok=self.only_one_level_print(rdd)
                if ok:
                    return rdd,True
                else:
                    return rdd,False
            if type(rdd)==list or type(rdd)==tuple:
                _,ok=self.some_level_print(rdd)
                if ok:
                    return rdd,True
                else:
                    return rdd,False
            if type(rdd)==dict:
                _,ok=self.dict_print(rdd)
                if ok:
                    return rdd,True
                else:
                    return rdd,False
        except Exception as e:
            return e,False

def test():
    base=Base_one()
    # 整数
    base.sprint(12001)
    print("---"*20)
    # 浮点数
    base.sprint(1.1)
    print("---"*20)
    # 布尔
    base.sprint(True)
    print("---"*20)
    # 字符串
    base.sprint("11-223")
    print("---"*20)
    # 列表
    base.sprint([1,2,3])
    print("---"*20)
    base.sprint([[1],[2,3],[4,5,6]])
    print("---"*20)
    # 元组
    base.sprint((1,2,3))
    print("---"*20)
    base.sprint(((1,1),(2,3),(4,5,6)))
    print("---"*20)
    # 集合
    base.sprint({1,2,3})
    print("---"*20)
    # 字典
    base.sprint({"name":["jom","kom","lom"],"age":[1,2,3],"address":{"ShangHai":1,"BeiJing":2}})

if __name__=="__main__":
    test()




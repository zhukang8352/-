"""自定义异常"""
class AgeError(Exception):
    def __init__(self,msg,code,age_value):
        super().__init__(msg)
        self.msg = msg
        self.code = code
        self.age_value = age_value
class Wife:
    def __init__(self,age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 15 <= value <=30:
            self.__age = value
        else:
            #raise ValueError("我不要")
            raise AgeError("我不要",16,value)

try:
    w01 = Wife(80)
except AgeError as e:
    print("错误信息：",e.msg,"错误代码行号:",e.code,"错误值：",e.age_value)


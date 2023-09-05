#student module
#提供變數，module提供的常數
#提供class
#提供function

class Student:
    def __init__(self, name:str, chinese:int, english:int, math:int):
        #實體的attribute
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math
    
    #實體的method
    def total(self) -> int:
        return self.chinese + self.english + self.math
    
    #建立property -> 類似method，沒有參數，一定要傳出一個值
    @property
    def average(self) -> float:
        return self.total() / 3.0
    
    def __repr__(self) -> str:
        return f"我是student實體，我的name：{self.name}"

import random 
def get_student(n:str) -> Student:
    c = random.randint(50, 100)
    e = random.randint(50, 100)
    m = random.randint(50, 100)
    return Student(name=n, chinese=c, english=e, math=m)
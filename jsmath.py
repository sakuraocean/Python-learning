# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:37:19 2020

@author: m1353
"""

import random

 
# 用来计算最终结果
def Calculation_Formula(a,b,c,c1,c2):
    num = 0
    if c2 == '*' and c1 != '*' and c1 != '/':
        if c1 == '-':
            num = (-b)*c
        else:
            num = b*c
        
    if c2 == '/' and c1 != '*' and c1 != '/':
        if c1 == '-':
            num = (-b)/c
        else:
            num = b/c
    if c1 ==  '+':
        num = num+a+b
    if c1 == '-':
        num = num+a-b
    if c1 == '*':
        num = num+a*b
    if c1 == '/':
        num = num+a/b
    if c2 == '+':
        num = num+c
    if c2 == '-':
        num = num-c
    if c2 == '*':
        num = num*c
    if c2 == '/':
        num = num/c
    return num
 
 
def Random_Formula():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    MathematicalSymbols = ['+', '-','/','*']
    MathematicalSymbols1 = random.choice(MathematicalSymbols)
    MathematicalSymbols2 = random.choice(MathematicalSymbols)
    # 生成式子
    if MathematicalSymbols1 == '-' and MathematicalSymbols2 != '*' and MathematicalSymbols2 != '/':
        if a-b < 0:
            Random_Formula()
    if MathematicalSymbols1 == '*' or MathematicalSymbols1 == '/':
        a = random.randint(1,10)
        b = random.randint(1,10)
    if MathematicalSymbols2 == '*' or MathematicalSymbols2 == '/':
        b = random.randint(1,10)
        c = random.randint(1,10)
    if a==b or b==c or a==c:
        Random_Formula()
    formula = str(a) + MathematicalSymbols1 + str(b) + MathematicalSymbols2 + str(c)
    re = Calculation_Formula(a,b,c,MathematicalSymbols1,MathematicalSymbols2)
    string = formula+'='+'      '+str(re)
    # 防止出现负数
    if re < 0 : 
        Random_Formula()
    else:
        # print(formula,'=',re)
        # 将生成的算式写到文件中去
        with open(r'D:\Py-test\04.txt','a',encoding='utf-8') as f:
            f.write(string)
            # 为了美观
            f.write('\n')
        pass
 
 
#生成25个小学加减乘除混合运算
if __name__ == '__main__':
    import profile
    for i in range(25):
        Random_Formula()
        pass
    profile.run("Random_Formula()")
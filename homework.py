__author__ = 'bzw'
"""
作业
1.简述普通参数、指定参数、默认参数、可变长参数的区别
2.写函数，计算传入字符串中单个【数字】、【字母】、【空格] 以及 【其他】的个数
3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5
4.写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有[],'',(),None或{}。
5.定义一个函数，输入不定个数的数字，返回所有数字的和
"""
#1.普通参数：与顺序有关，按顺序传参数
#  指定参数：与顺序无关，根据给定的值进行传参
#  默认参数：参数有默认值，如果不修改该参数，该参数就使用默认值
#  可变参数：变量前面带有*或者**，可以接收多个参数
#2.
# def statistics(c):
#     """
#     统计输入字符串中字母的个数，数字的个数，空格的个数和其他类型的个数
#     :param c: 一个字符串
#     :return:返回字母的个数，数字的个数，空格的个数和其他类型的个数
#     """
#     l = len(c)
#     en = 0
#     num = 0
#     sp = 0
#     other = 0
#     a = 0
#     for i in c:
#         x = ord(i)
#         if 65 <= x <= 90 or 97 <= x <= 122:
#             en = en + 1
#         elif 48 <= x <= 57:
#             num = num + 1
#         elif x == 32:
#             sp = sp + 1
#         else:
#             other = other + 1
#
#     return en, num, sp, other
#
#
# c = input("请输入一串字符串：")
# a, b, c, d = statistics(c)
# print("字母的个数为：{0}，数字的个数为：{1}，空格的个数为：{2}，其他类型的个数为：{3}".format(a, b, c, d))

#3.
# def is_len(s):
#     if len(s)>5:
#         return True
#     return False
# s=input("请输入参数：")
# d=eval(s)
# if is_len(d):
#     print("长度大于5")
# else:
#     print("长度不大于5")

#4
def is_none(s):
    '''
    判断传入可迭代对象中每一个元素是否含有空类型：[],(),{},'',None
    如果传入的是一个空对象，则返回None
    '''
    #if type(s)=='dict':
        #if [] in s.values():
           # print(s.values)
            #return True
        #else:
            #return False
    #else:
    if len(s)==0:
        return True
    for i in s:
        if i==[] or i=={} or i=='' or i==None or i==():
           return True
    else:
            return False
s=[]
a=(1,6,5)
c=input("请输入参数：")
#将字符串转化为列表或者元组，字典，如果输入的第一个字符为[则转化为列表，
# 如果第一个字符为（则转化为元组，如果第一个字符为{则转化为字典
try:
   b=eval(c)
except Exception as e:
    b=c
#print(b)
print(type(b))
print(is_none(b))

#5.
# def random_sum(num):
#     '''
#     输入不定个数的数字，返回所有数字的和
#     :param n: 输入的不定的数字
#     :return:返回所有数字的和
#     '''
#     for j in num:
#        x=ord(j)
#        if x<48 or x>57:
#           return -1
#     sum=0
#     for i in num:
#         b=int(i)
#         sum=sum+b
#     return sum
#
# num=input("请输入数字：")
# a=random_sum(num)
# if a==-1:
#     print("输入错误！")
# else:
#     print("您输入所有数字的和为：%s"%a)




# l=len(c)
# lists=[]
# if c[0]=="[" and c[l-1]=="]":
#     print("yes")
# #print(type(c))
# for i in range(1,l-1):
#     lists.append(c[i])
#     if ',' in lists:
#        lists.remove(',')
# print(lists)

c=input("请输入参数：")
b=eval(c)
print(type(b))
print(is_none(b))
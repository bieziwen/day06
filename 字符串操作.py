__author__ = 'bzw'
"""
使用字符串的find方法，把下面的字符串中的文本链接添加到一个list中。

"""

html = """"
<dl class=dl-list">

                    <dd><span class="classify">[古言]</span><span class="author">浅浅的心</span><a href="/info/471282.html" target="_blank">嫡女风华</a></dd>
                    <dd><span class="classify">[现言]</span><span class="author">月初姣姣</span><a href="/info/921936.html" target="_blank">名门隐婚：枭爷娇宠妻</a></dd>
                    <dd><span class="classify">[现言]</span><span class="author">秋囚囚</span><a href="/info/942135.html" target="_blank">重生之王牌军妻</a></dd>
                    <dd><span class="classify">[现言]</span><span class="author">唐家姑娘</span><a href="/info/850135.html" target="_blank">军少独爱闪婚萌妻</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">懒语</span><a href="/info/875887.html" target="_blank">枕上香之嫡女在上</a></dd>
                    <dd><span class="classify">[悬疑]</span><span class="author">涂山九尾</span><a href="/info/937235.html" target="_blank">大明女推官</a></dd>
                    <dd><span class="classify">[玄幻]</span><span class="author">处雨潇湘</span><a href="/info/701416.html" target="_blank">逆天魔妃太嚣张</a></dd>
                    <dd><span class="classify">[现言]</span><span class="author">恩很宅</span><a href="/info/888707.html" target="_blank">枭宠重生之盛妻凌人</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">福星儿</span><a href="/info/931207.html" target="_blank">穿越莽荒：王牌特工vs野人老公</a></dd>
                    <dd><span class="classify">[现言]</span><span class="author">陈小笑</span><a href="/info/890930.html" target="_blank">八块八：高冷总裁带回家 </a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">澄夏</span><a href="/info/830950.html" target="_blank">军王狂后之帝君有毒</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">宝贝鹿鹿</span><a href="/info/836613.html" target="_blank">重生之妖娆毒后</a></dd>
                    <dd><span class="classify">[青春]</span><span class="author">听听雨夜</span><a href="/info/830987.html" target="_blank">学霸你女朋友掉了</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">千山茶客</span><a href="/info/688238.html" target="_blank">重生之将门毒后</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">三木游游</span><a href="/info/872466.html" target="_blank">嫡女煞妃</a></dd>
            </dl>
"""
def find_all_href(html_doc):
    """
    查找文档中所有的超链接
    传入参数：一个HTML文档
    返回值：links列表
    """
    links=[]#创建一个空列表
    i=0
    l=len(html_doc)
    while i<l:
        index=html_doc.find("href",i)#查找第一个href的索引值并赋给index，i表示是从i开始索引

        if index==-1:#如果没找到href就返回-1
            break
        links.append(html_doc[index+7:index +23])#将找到后的链接添加到列表当中，index+7表示从“h”后的第7位开始添加一直到第23位
        i=index +4#每次查找时索引值都加4，因为index表示h的索引值，如果从index开始，也就是从h开始查找，找到的还是当前的href
    return links
l=find_all_href(html)
for i in l:
   print(i)


a=set((3,5,9))#类型为集合 集合可以直接用大括号例如{1,6,8,7}
b=set([1,5,9,6,8,7])
print(a&b)#并集


def is_zimu(c):
    """
    输入一个字符判断是否为字母
    :param c: 一个字符
    :return:True or False
    """
    if len(c)!=1:
        return -1
    y= ord(c)

    if 65<=y<=90 or 97<=y<=122:
        return True
    else:
        return False

while True:
    c=input("请输入字符：")
    if c==" ":
        break
    if is_zimu(c) is True:
        print("你输入的是字母！")
    elif is_zimu(c) is False:
        print("你输入的不为字母！")
    else:
        print("你输入有误！")





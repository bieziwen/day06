html="""
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
                    <dd><span class="classify">[青春]</span><span class="author>听"听雨夜</span><a href="/info/830987.html" target="_blank">学霸你女朋友掉了</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">千山茶客</span><a href="/info/688238.html" target="_blank">重生之将门毒后</a></dd>
                    <dd><span class="classify">[古言]</span><span class="author">三木游游</span><a href="/info/872466.html" target="_blank">嫡女煞妃</a></dd>
            </dl>
"""
def find(html_doc):
    link=[]
    i=0
    l=len(html_doc)
    while i<l:
        index=html_doc.find('href',i)
        if index==-1:
            break
        link.append(html_doc[index+7:index+23])
        i=index+4
    return link


#h=find(html)
#for i in h:
    #print(i)
a={'name':'赵','age':21,'sex':'男'}
b=set(a)
print(b)#b的值是a中所有的key值
print(type(b))




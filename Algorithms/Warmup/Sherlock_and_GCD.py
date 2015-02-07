# -*- coding: utf-8 -*-
#Question:
#福爾摩斯得到一個集合
#只要找到它的任一子集合其最大公因數為1
#則為正解
#---------------------
#Answer:
#1.(如正文)用雙迴圈列出所有組合可能性做XOR
#2.如果知道使用itertools的combinations的話，程式碼會更短
#----------------------
import itertools

def gcd(args):
    #物件只有一個，就不看了
    if len(args) == 1:
        return args[0]

    #物件兩個以上，進行GCD
    L = list(args)
    while len(L) > 1:
        a = L[len(L) - 2]
        b = L[len(L) - 1]
        L = L[:len(L) - 2]        
        while a:
            a, b = b%a, a
        L.append(b)
    return abs(b)


testcase = input()
while testcase > 0:
    a = input()
    b = ([ int(i) for i in raw_input().split() ])
    b = list(set(b))
    gcd_result = None
    satisfy = False
    
    #C(n,choose)，決定choose，1<=choose<=n
    for choose in range(len(b)):
        if satisfy :
            break
        if choose == 0:
            if min(b) == 1 :
                satisfy = True
            continue
        #列出所有組合可能性
        for i in itertools.combinations(b, choose+1):
            #print i
            #如果發現有子集的最大公因數為1，則停止運算
            if gcd(i) == 1:                        
                satisfy = True
                break

    if satisfy :
        print "YES"
    else :
        print "NO"
    testcase -= 1

"""
from itertools import chain, combinations


def gcd(args):
    L = list(args)
    #物件只有一個，就不看了
    if len(L) == 1:
        return L[0]
   
    #物件兩個以上，進行GCD
    
    while len(L) > 1:
        a = L[len(L) - 2]
        b = L[len(L) - 1]
        L = L[:len(L) - 2]        
        while a:
            a, b = b%a, a
        L.append(b)
    return abs(L[0])

#超級集合，但去除了空集合
def powerset(iterable):
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) if n > 0 )


testcase = input()
while testcase > 0:
    #輸入元素數量(但根本不到)
    a = input()
    #輸入集合
    b = [ int(i) for i in raw_input().split() ]
    #去除重複的元素
    b = list(set(b))
    #超級集合
    b = list(powerset(b))
    
    satisfy = False

    for i in b :
        if gcd(i) == 1 :
            satisfy = True
            break
   
    if satisfy :
        print "YES"
    else :
        print "NO"
    testcase -= 1

"""
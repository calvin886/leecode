# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一：用insert（)每次将原链表中的元素插入空链表的头部，从而实现头尾转换
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result=[]
        while listNode:
            result.insert(0,listNode.val)
            listNode = listNode.next
            
        return result
        
方法二：递归
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.result=[]
        
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode:
            self.printListFromTailToHead(listNode.next)
            self.result.append(listNode.val)
        return self.result 
 

！[image](https://github.com/calvin886/leecode/blob/main/1600257113-BMRLhV-image.png)
 
        

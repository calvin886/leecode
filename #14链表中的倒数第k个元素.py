# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
方法一：Linklist对于元素搜索比较麻烦，但是把链表中的元素输入到arraylist中就比较便于元素关于index的查询
      所以本方法直接将链表中的元素倒序输入到Arraylist中然后找第k个元素即可
class Solution:
    def FindKthToTail(self, head,k):
        # write code here
        array = []
        if head is None or k<1:
            return None 
        while head:
            array.insert(0,head)
            head = head.next
        if k<= len(array):
            return array[k-1]
           
方法二：

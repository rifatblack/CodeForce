# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')



# class Employee():
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def fun(self):
#         new = ()
#         if self.name == 'Alice':
#             new +=self.name
#         return self.name + new # 👈️ return a string
#
#     def __str__(self):
#         vals = []
#         node = self.name
#         while node is not None:
#             vals.append(node.val)
#             node = node.next
#         return f"[{','.join(str(val) for val in vals)}]"
#
#
# emp = Employee('Alice', 100)
# emp1 = Employee('Alice1', 100)
# emp2 = Employee('Alice2', 100)
# emp3 = Employee('Al1ice3', 100)
#
#
# print(emp.fun())
#

#
# class ListNode:
#     def __init__(self, val=0, next=None,pre=None):
#         self.pre = pre
#         self.val = val
#         self.next = next
# class Solution:
#     def __init__(self,head=None):
#         self.head= head
#
#
#     def addTwoNumbers(self, l1, l2):
#         new =ListNode(l1)
#         if new is not None:
#             new.next = new
#             print(new.val ,new.next,new.pre)
#
#
#
#
# new= Solution()
# new.addTwoNumbers(10,0)
# new.addTwoNumbers(12,0)
# new.addTwoNumbers(13,0)
# new.addTwoNumbers(14,0)




class ListNode:
    def __init__(self, val=0, next=None,pre=None):
        self.pre = pre
        self.val = val
        self.next = next
class Solution:
    def __init__(self,head=None,tail=None):
        self.head= head
        self.tail=tail


    def addTwoNumbers(self, l1):
        node =ListNode(l1)
        if self.tail is None:
            self.head = node
            self.tail = node

        else:

            self.tail.next = node
            self.pre = self.tail
            print(self.tail.next.val,self.pre.val,self.tail.next)



new1= Solution()

new1.addTwoNumbers(10)
new1.addTwoNumbers(12)
new1.addTwoNumbers(13)
new1.addTwoNumbers(14)





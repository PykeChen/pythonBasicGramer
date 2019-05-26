""" 深度搜索和广度搜索算法 """

import queue


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


node4 = Node(4, None, None)
node5 = Node(5, None, None)
node6 = Node(6, None, None)
node7 = Node(7, None, None)

node2 = Node(2, node4, node5)
node3 = Node(3, node6, node7)

node1 = Node(1, node2, node3)


# 广度搜索算法
myQue = queue.Queue()
myQue.put(node1)
while not myQue.empty():
    curNode = myQue.get()
    if curNode.left is not None:
        myQue.put(curNode.left)
    if(curNode.right is not None):
        myQue.put(curNode.right)
    print(curNode.value, end=', ')
print('\n-------')

# 深度搜索算法-递归写法


def dsfSearch(curnode):
    if(curnode is None):
        return
    print(curnode.value, end='-')
    dsfSearch(curnode.left)
    dsfSearch(curnode.right)


dsfSearch(node1)
print('\n-------')

# 深度搜索算法-递归写法 列表返回


def dsfSearchList(curnode):
    if(curnode is None):
        return []
    return [curnode.value] + dsfSearchList(curnode.left) + dsfSearchList(curnode.right)


sdfList = dsfSearchList(node1)
print(sdfList)

# 深度搜索算法-非递归写法


def dsfSearchStack(myList, curnode):
    if(curnode is None):
        return
    myStack = queue.deque()
    myStack.append(curnode)
    while len(myStack) > 0:
        tmpNode = myStack.pop()
        myList.append(tmpNode.value)
        if(tmpNode.left is not None):
            myStack.append(tmpNode.right)
        if(tmpNode.right is not None):
            myStack.append(tmpNode.left)


myList = []
dsfSearchStack(myList, node1)
print(myList)

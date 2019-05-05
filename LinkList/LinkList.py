#/usr/bin/python
#-*- coding: utf-8 -*-

class Node(object):
	def __init__(self, value, p=None):
		self.data = value
		self.next =  p


class LinkList(object):
	def __init__(self):
		self.header = None
	
	def addNode(self, value):  #尾插
		new_node = Node(value)
		if self.header == None:
			self.header = new_node
		else:
			tmp = self.header.next
			while(tmp.next):
				tmp = tmp.next
			tmp.next = new_node
			new_node.next = None
	
	def addNode_start(self, value): # 头插
		new_node = Node(value)
		if self.header == None:
			self.header = new_node
		else:
			new_node.next = self.header
			self.header = new_node
	
	def popNode(self): #删除最后一个
		if self.header == None:
			print("LinkList is empty")
		else:
			tmp = self.header.next
			while(tmp.next.next):
				tmp = tmp.next
			tmp.next = tmp.next.next
			
	
	def insertNode(self, index,value): #在中间任一位置插入
		#index 是要插入的位置
		new_node = Node(value)
		tmp = self.header  #这里假设header不只是有next指针还有数据，所以从header就开始。若header仅有next指针，则tmp=self.header.next
		count = 0
		while(count<index):	
			temp1 = tmp      #存储要插入位置的前一个点的信息，用于后续
			tmp = tmp.next
			count = count +1
		temp1.next = new_node
		new_node.next = tmp
			
	def removeNode(self, index): #在中间任一位置移除
		#index 是要删除的位置
		tmp = self.header
		count = 0
		while(count<index):
			temp1 = tmp
			tmp = tmp.next
			count = count +1
		temp1.next = tmp.next
	
	def search(self, num):  #在链表中搜索num
		index = 0
		tmp = self.header
		while(tmp.next != None):
			if (tmp.data == num):
				return index
			tmp = tmp.next
		print("num not found!")
				
		
	def deleteNode(self, num): #通过搜索num删除节点
		tmp = self.header
		if tmp.data == num:
			self.header = tmp.next
			tmp.next = None
			del tmp
		else:
			while(tmp.data != num):
				temp1 = tmp
				tmp = tmp.next
			temp1.next = tmp.next
			tmp.next = None
			del tmp

			
			
	def reverseLinkList(self):
		if (self.header is None):
			return None
		else:
			curNode = self.header 		# 当前节点
			prevNode = None       		# 当前节点的上一个节点
			nextNode = curNode.next  # 当前节点的下一个节点
			newHeader = None #若header有data的，不用考虑这个指针。
		
			while(curNode.next != None):
				curNode.next = prevNode
				nextNode.next = curNode
				prevNode = curNode
				curNode = nextNode
				nextNode = curNode.next
			return curNode
	
	def reverseLinkListRecursion(self, pHead): #用递归的方法反转链表[!!!]
		'''求链表 A->B->C->D 的反转链表， 可以先求 B->C->D 的反转链表 D->C->B，然后将 A 连在B后面就完成了。'''
		'''这就将原问题转变为求更小的子问题：求 B->C->D 的反转链表 ...... 依次往下转变就行。'''
		#pHead是头指针
		if not pHead or not pHead.next:
			return pHead
		newHeader = self.reverseLinkListRecursion(pHead.next)
		pHead.next.next = pHead
		pHead.next = None
		return newHeader
	
	def hasCircle1(self, pHead): #判断链表有没有环路, 用集合的方法
		mapping = set()
		flag = False
		p = pHead
		while (p):
			if p not in mapping:
				mapping.add(p)
			else:
				flag = True
				return flag
			p = p.next
		return flag
	
	def hasCircle2(self, pHead): #用快慢指针的方法判断链表有没环路
		#快指针一次走两步，慢指针一次走一步，如果有环一定会相遇
		p = pHead
		if (p is None):
			return False
		fast = p.next.next
		slow =p.next
		flag = False
		
		while(fast is not slow):
			if fast.next is None  or fast.next.next is None: #fast指针到达了链表尾部（fast肯定比slow快）
				return flag
			fast = fast.next.next
			slow = slow.next
		
		flag = True #跳出while，相遇了，flag置True
		return flag

	def findCircleEntry(self, pHead): 
	#判断链表有没有环路，有环路找到环路入口
	#用快慢指针的方法，两指针能相遇即有环路，此时把快指针回到链表头部，慢指针留在第一次相遇处，两指针每次步长为一再次运动，相遇处为环路入口。
		p = pHead
		if (p is None):
			return False
		fast = p.next.next
		slow = p.next
		
		while(fast is not slow):
			if fast.next is None or fast.next.next is None: #fast指针到达了链表尾部（fast肯定比slow快）
				print("This LinkList has no circle!")
			fast = fast.next.next
			slow = slow.next
		print("This LinkList has Circle.")
		
		#find the circle entry
		fast = pHead  #fast移动到表头，slow留在相遇处
		while(fast is not slow): #步长为1继续走直到相遇 
			fast = fast.next
			slow = slow.next
		return fast  #第二次相遇跳出循环，返回位置
		
	def mergeLinkList(self, l1, l2): #合并两个有序链表
		if (l1 is None):
			return l2
		if (l2 is None ):
			return l1
		
		pHead = Node(0) #新建一个链表头用于返回最后合并结果
		while(l1 is not None or l2 is not None): #有一个走完就跳出，然后剩下的直接合并到结尾
			if (l1.data < l2.data):
				pHead.next = l1
				l1 = l1.next
			elif(l1.data > l2.data):
				pHead.next = l2
				l2 = l2.next
			pHead = pHead.next
			
		if l1 is None:        #l2先跑完，后面接上剩下的l1
			pHead.next = l1
		if l2 is None:         #l1先跑完，后面接上剩下的l2
			pHead.next = l2
			
		return pHead
	
	
	def mergeLinkListRecursion(self, l1, l2): #用递归的方法合并链表
		pHead = None    #每一层递归用pHead做，该层递归（仅有两个节点操作）的头指针。
		
		if (l1 is None):  #递归出口
			return l2
		elif (l2 is None):  #递归出口
			return l1 
		elif (l1.data < l2.data):
			pHead = l1
			pHead.next = mergeLinkList(l1.next, l2)
		elif (l1.data > l2.data):
			pHead = l2
			pHead.next = mergeLinkList(l1, l2.next)
		
		return pHead   #每次递归调用后都返回该层的头指针用于上一层的合并。
		
	
	def findDS_K_Number(self, pHead, k): #找到链表倒数第k个节点
		if (pHead is None or k<1):  #输入的head为空指针或者k不合法
			return None
			
		fast = pHead
		slow = pHead
		
		for (int i = 0; i < k-1; i++):
			if (fast.next is not None): #输入的以head为头结点的链表的结点总数是否少于k
				fast = fast.next
			else:
				return None
				
		while(fast.next is not None):
			fast = fast.next
			slow =slow.next
		
		return slow
		
	
	def findMiddleNode(self, pHead): #找到链表的中间节点
		#用快慢指针法，快指针一次走2步，慢指针一次走1步，当快指针到达时，慢指针所在位置即为链表中间节点
		if (pHead is None):
			return None
			
		fast = pHead
		slow = pHead
		
		while(fast is None or fast.next is None): #fast is None 是链表有偶数个节点时会出现的情况，fast.next is None 是链表有奇数个节点时会出现的情况。
			fast = fast.next.next
			slow = slow.next
		
		return slow
				
		
			
			
		
		
		
	
		
		
			
		
	
			
		
			
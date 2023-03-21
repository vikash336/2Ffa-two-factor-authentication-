# def fun(a):
#     l=[]
#     for i in range(len(a)-1):
#         if a[i]>a[i+1] or a[i]==a[i+1]:
#             l.append(i)
#             l.append(i+1)
#     res=[]
#     for i in range(len(a)):
#         if i in l:
#             pass
#         else:
#             res.append(a[i])
#     res2=[]
#     for i in range(0, len(res),2):
#         final=[]
#         final.append(res[i])
#         final.append(res[i+1])
#         res2.append(final)

#     print(res2)

# a=  [[1,4],[0,4]]
# remove_b=[]
# for i in a:
#     for j in i:
#         remove_b.append(j)
# fun(remove_b)

# nums = [5,0,1,2,3,4]
# l=[]
# for i in range(len(nums)):
#     a=nums[nums[i]]
#     print(a)

# print(nums)


# s={1,2,322,45,False}

# print(s)

# s = "pwwkew"
# print(s[0])
# temp=[]
# for i in range(0,len(s)):
#     for j in range(i,len(s)):
#         temp.append(s[i:j+1])
# print(temp)



# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):
	
	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Polygon()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

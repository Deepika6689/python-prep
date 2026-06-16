# name=input("enter your name")
# ptr = open("deepika.txt","w")
# ptr.write(name)
# ptr.close()
import threading

# name = input("Enter your name: ")
# ptr=open("deepika.txt","w")
# ptr.write(name)
# ptr.close()

# name = input("Enter your name: ")
# ptr=open("deepika.txt","a")
# ptr.write(name + "\n")
# ptr.close()


# ptr=open("deepika.txt","a")
# ptr.write("deepika\nniki\nshami\nsoumya\njaya\n")
# ptr.close()
# print("5 names")



# ptr=open("deepika.txt","w")
# for i in range(5):
#     name = input("Enter your name: ")
#     ptr.write(name + "\n")
# ptr.close()
# print("5 names added")


# ptr1=open("deepika.txt","r")
# data=ptr1.read()
# print(data)
# ptr1.close()


# ptr1=open("deepika.txt","r")
# data=ptr1.read(7)
# print(data)
# ptr1.close()
# deepika

# ptr1=open("deepika.txt","r")
# data=ptr1.readline()
# print(data)
# ptr1.close()
# deepika

# ptr1=open("deepika.txt","r")
# data=ptr1.readlines()
# print(data)
# ptr1.close()


# tell() and seek()
# ptr=open("deepika.txt","r")
# pos1=ptr.tell()
# print(pos1)
# # 0
# res1=ptr.read(8)
# print(res1)
# pos2=ptr.tell()
# print(pos2)
# ptr.seek(3)
# pos3=ptr.tell()
# print(pos3)
# ptr.seek(0)
# pos4=ptr.tell()
# print(pos4)
# res2=ptr.read(15)
# print(res2)
# pos5=ptr.tell()
# print(pos5)
# ptr.close()



# ptr=open("car.jpg","rb")
# data=ptr.read(90000)
# print(data)
# ptr.close()
# ptr1=open("newcar.jpg","wb")
# ptr1.write(data)
# ptr1.close()

# pickling
# import pickle
# class Employee:
#     def __init__(self,name,age):
#         self.ename = name
#         self.eage = age
#     def dis(self):
#         print(self.ename)
#         print(self.eage)
# e1=Employee("deepika",22)
# f=open("deepika.txt","wb")
# pickle.dump(e1,f)
# f.close()
#
# class Employee:
#     def __init__(self,name,age):
#         self.ename = name
#         self.eage = age
#     def dis(self):
#         print(self.ename)
#         print(self.eage)
# f=open("deepika.txt","rb")
# e=pickle.load(f)
# e.dis()
# f.close()

#take one list pickle nd unpickle
# import pickle
# l=[1,2,3,4,5]
# ptr=open("deepika.txt","wb")
# pickle.dump(l,ptr)
# ptr.close()
# pt1=open("deepika.txt","rb")
# res=pickle.load(pt1)
# print(res)
# pt1.close()


#take two threads one thred should print odd numbers another thread should print even numbers but in should give output in the sequences


from threading import Thread
# def odd():
#     for i in range(1,11,2):
#         print(i)
# def even():
#     for i in range(2,11,2):
#         print(i)
# t1=threading.Thread(target=odd)
# t2=threading.Thread(target=even)
# t1.start()
# t2.start()


# import time
# from threading import Thread
# class task1(Thread):
# def even():
#     for i in range(1,11,2):
#         print(i)
#         time.sleep(2)
# class task2(Thread):
# def odd():
#     for i in range(2,11,2):
#         print(i)
#         time.sleep(2)
# t1=task1
# t2=task2
# t1.start()
# t2.start()

file=open("deepika.txt","w")
for i in range(10):
    name=input("enter name")
    file.write(name + "\n")
file.close()
file=open("deepika.txt")
data=file.readlines()
print(data)
file.close()








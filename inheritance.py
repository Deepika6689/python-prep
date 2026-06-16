# -------------1---------------
# class parent:
#     def __init__(self):
#         self.a=10
# class child(parent):
#     def __init__(self):
#         parent.__init__(self)
#         self.b=20
# c1=child()
# print(c1.b)
# print(c1.a)


# -------------2--------------
# class A:
#     def __init__(self):
#         self.a=100
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.b=200
# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.c=300
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)


# ------------3-------------#super method
# class A:
#     def __init__(self):
#         self.a=100
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.b=200
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.c=300
# c1=C()
# print(c1.c)
# print(c1.b)
# print(c1.a)


# class plane:
#     def takeoff(self):
#         print("take off")
#     def fly(self):
#         print("flying")
#     def land(self):
#         print("landing")
# class passenger(plane):
#     def carry_p(self):
#         print("carry p")
# class cargo(plane):
#     def carry_g(self):
#         print("carry g")
# class fighter(plane):
#     def carry_w(self):
#         print("carry w")
# p1=passenger()
# c1=cargo()
# f1=fighter()
# p1.takeoff()
# p1.fly()
# p1.land()
# p1.carry_p()
# c1.takeoff()
# c1.fly()
# c1.land()
# c1.carry_g()
# f1.takeoff()
# f1.fly()
# f1.land()
# f1.carry_w()

#
# class animal:
#     def eat(self):
#         print("eat")
#     def sleep(self):
#         print("sleep")
#     def hunt(self):
#         print("hunt")
# class lion(animal):
#     pass
# class tiger(animal):
#     pass
# class fox(animal):
#     pass
# l1 = lion()
# t2 = tiger()
# f3 = fox()
# l1.eat()
# l1.sleep()
# l1.hunt()
# t2.eat()
# t2.sleep()
# t2.hunt()
# f3.eat()
# f3.sleep()
# f3.hunt()



# class a:
#     def display(self):
#         print("a")
# class b:
#     def display(self):
#         print("b")
# class c:
#     def display(self):
#         print("c")
# c1=c()
# c1.display()
# c1.display()
# c1.display()

# class a:
#     def disp(self,a,b,c):
#         print(a,b,c)
# class b(a):
#     def disp(self,a,b):
#         print(a,b)
# class c(b):
#     def disp(self,a):
#         print(a)
#
# c1=c()
# c1.disp(10)
# c1.disp(10,20)
# c1.disp(10,20,30)


# class charger:
#     def __init__(self, name):
#         self.cname = name
#     def getcharger(self):
#         print("charger us pulgged in")
# class mobile:
#     def __init__(self, name):
#         self.mname = name
#         self.c=""
#     def hasmobile(self,p):
#         self.c=p
# m1=mobile("iq")
# c1=charger("c pin")
# m1.hasmobile(c1)
# print(m1.mname)
# print(m1.c.cname)
# m1.c.getcharger()
# del m1
# print(c1.cname)
# c1.getcharger()

#doubt
class heart:
    def __init__(self):
        self.status = "empty"
        print("heart is pumping")
    def heartAttack(self):
        print("heart attack")


class cycle:
    def __init__(self, name):
        self.cname = name
    def cycleattack(self):
        print("cycle")
class person:
    def __init__(self, name):
        self.pname = name
        self.c=""
p1=person("abc")
c1=cycle("ladybird")
h1=heart("HB")
p1.hasperson(c1)

print(p1.pname)
print(p1.c.pname)
p1.c.heartattack()
p1.c.cycleattack()
del p1
print(c1.pname)
print(h1.pname)
h1.heartattack()
c1.cycleattack()







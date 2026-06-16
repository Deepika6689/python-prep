# class book:
#     def __init__(self,page):
#         self.__pages = page
# b1=book(100)
# print(b1.__pages)
# class book:
#     def __init__(self,page):
#         self.__pages=page
#     def setter(self,val):
#         if val > 0:
#             self.__pages=val
#     def getter(self):
#         return self.__pages
# b1=book(100)
# res1=b1.getter()
# print(res1)
# b1.setter(200)
# res2=b1.getter()
# print(res2)
# b1.setter(-99)
# res3=b1.getter()
# print(res3)

# normal encapsulation:::::::::
#
# class person:
#     def __init__(self):
#         self.__name=""
#     def setter(self,val):
#         self.__name=val
#     def getter(self):
#         return self.__name
# p1=person()
# p1.setter("savita")
# res=p1.getter()
# print(res)


# class person:
#     def __init__(self):
#         self.__name=""
#     def getter(self):
#         return self.__name
#     def setter(self,val):
#         self.__name=val
#     getset=property(getter,setter)
# p1=person()
# p1.getset="deepika"
# res=p1.getset
# print(res)

# class Person:
#     def __init__(self):
#         self.__name=""
#     @property
#     def dataAccess(self):
#         return self.__name
#     @dataAccess.setter
#     def dataAccess(self, value):
#         self.__name = value
# p1=Person()
# p1.dataAccess="deepika"
# res=p1.dataAccess
# print(res)

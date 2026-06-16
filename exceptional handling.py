# a=int(input("enter a"))
# b=int(input("enter b"))
# try:
#     res=a/b
#     print(res)
# except Exception as e:
#     print("throwing error")


# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured in fun 1")
#     print("leaving fun1")
# def fun2():
#     print("entering fun2")
#     res=10/0
#     print(res)
#     print("leaving fun2")
# print("pgm started")
# fun1()
# print("pgm ended")


# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured in fun 1")
#     print("leaving fun1")
# def fun2():
#     print("entering fun2")
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print("error occured in fun 2")
#         raise e /////////////re throwing an error
#     print("leaving fun2")
# print("pgm started")
# fun1()
# print("pgm ended")


# def fun1():
#     print("entering fun1")
#     try:
#         fun2()
#     except Exception as e:
#         print("error occured in fun 1")
#     print("leaving fun1")
# def fun2():
#     print("entering fun2")
#     try:
#         res=10/0
#         print(res)
#     except Exception as e:
#         print("error occured in fun 2")
#         raise e
#     finally: /////
#         print("leaving fun2")
# print("pgm started")
# fun1()
# print("pgm ended")



# try:
#     a=int(input("enter a number"))
#     b=(input("enter another number"))
#     res=a/b
#     print(res)
# except ValueError as e:
#     print("it is VE")
# except ZeroDivisionError as e:
#     print("it is ZDE")
# except Exception as e:
#     print("error ocurred")

# try:
#     a=int(input("enter a number"))
#     b=int(input("enter another number"))
#     res=a/b
#     print(res)
# except (ValueError,ZeroDivisionError) as e:
#     print("it is VE or ZDE")
#
#
# except Exception as e:
#     print("error ocurred")



# try:
#     a=int(input("enter a number"))
#     b=(input("enter another number"))
#     res=a/b
#     print(res)
# # except (ValueError,ZeroDivisionError) as e:
# #     print("it is VE or ZDE")
#
#
# except Exception as e:
#     print("error ocurred")
try:
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    res = a / b
    print(res)
except Exception as e:
    print("error occured")
    print(e.__str__())
else:
    print("program finished")



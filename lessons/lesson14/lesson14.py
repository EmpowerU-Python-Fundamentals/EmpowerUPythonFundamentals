# f = open("int.txt")
# f = open("lessons/lesson14/int1.txt")
# print(f.read())

# # f.close()
# f  = None
# try:
#     f = open("lessons/lesson14/int.txt")
#     # r = f.read(10)
#     r = f.readline()
#     print(r)
#     print("***"*10)
#     r = f.readlines()
#     print(r)
#     # print(r)
#     print(f"{f.tell()=}")
#     f.seek(5)
#     print(f"{f.tell()=}")
#     for line in f:
#         print(line)
#     print(f"{f.tell()=}")
# except Exception as err:
#     print(err)
# finally:
#     if f:
#         f.close()
import datetime
# file = open("lessons/lesson14/out.txt")
try:
    with open("lessons/lesson14/out.txt", "a") as file:
        for i in range(5):
            file.write(f"{datetime.datetime.now()} line {i*i}\n")

        l = map(str, list(range(10, 20)))
        file.writelines(l)

    # __enter__
    # __exit__
    
except Exception as err:
    print(err)

# class FileManager:
#     def __enter__(self):
#         print("__enter__")
#         return "text"
#     def __exit__(self, *args):
#         print("__exit__")


# print("run")
# with FileManager() as fm:
#     print("start with")
#     print(fm)
#     print("end with")
# print("end script")
from functools import reduce

# # from random import randint
# #
# # def print_pocessed_list(l: list[int], f):
# #     for el in l:
# #         print( f(el), end = " " )
# #
# # def squre(x):
# #     return x**2
# #
# L = [1,2,45, 464,8]
# # # print_pocessed_list( L, lambda x: x**2 )
# # print_pocessed_list( L, squre )
# # # print_pocessed_list( L, lambda x: x/10)
# # # print_pocessed_list( L, lambda x: 0)
# # # print_pocessed_list( L, lambda x: randint(0,10) )
#
#
# # for el in map(  lambda x: f"{x/10:.5f}", L):
# #     print(el, end = " ")
#
# # for i, el in enumerate(L):
# #     print(f"L[{i}] = {el}")
# X = [1, 2, 3]
# Y = [4, 6, 2]
#
# S = 0.0
# for x,y in zip(X, Y):
#     S += x*y
# print(S)
reduce( lambda sum,x: sum+x,    [1,2,3,4,5] )

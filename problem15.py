"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import math
# можно решить через сочения. привет тервер
# n!/(n − m)!/m! где m - размер сетки. n - число в 2 раза больше. 
# тоесть формула сводится до (2*m)!/((m!) ** 2). где м - размер сетки
grid = 20
routes = math.factorial(grid*2)/(math.factorial(grid) ** 2)
print (routes)
# BRUTE FORCE. долго.
# route_count = 0
# right_pred = 20
# down_pred = 20
# def route_found(right, down):
#     global route_count

#     if right == right_pred and down == down_pred:
#         route_count += 1
#         return True

#     if right < right_pred:
#         route_found(right + 1, down)
    
#     if down < down_pred:
#         route_found(right, down + 1)

# route_found(0,0)
# print (route_count)

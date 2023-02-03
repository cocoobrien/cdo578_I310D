# File: volume_of_a_sphere.py

# Hands-On Activity 3 for i310D
# 02/03/2023
# E1: create python file volume_of_sphere.py
#     implement function def_calculate_volume_of_sphere(radius)
#     compute & print volume of spheres radii for 30 and 40; save file
#     add file to the project I310D from command line using git add volume_of_sphere.py command
#     push changes to repository at GitHub
from typing import Union, Any


def calculate_volume_of_sphere(radius):
    # formula: V = 4/3(pi)(r^3)
    pi: float = 3.14
    volume: Union[float, Any]=4/3 * pi * (radius**3)
    return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f'The volume of a sphere with a radius of {radius1} is {volume1}.')

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(f'The volume of a sphere with a radius of {radius2} is {volume2}.')

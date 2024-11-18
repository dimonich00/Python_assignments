from math import pi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("radius", help="Radius of the circle", type=float)
args = parser.parse_args()
radius = args.radius

print(f"Area of the circle ={pi * radius * radius: .4f}")
print(f"Circumference of the circle ={2 * pi *radius: .4f}")

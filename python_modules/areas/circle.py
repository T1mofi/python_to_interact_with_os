import math as m

def circle(radius):
	return m.pi*(radius**2)

def donut(outside_radius, inside_radius):
	return circle(outside_radius) - circle(inside_radius)

import math

def find_angle_mbc_python(a, b):
	M = math.sqrt(a**2+b**2)
	theta = math.acos(b / M)
	print(f'{round(math.degrees(theta))}°')


if __name__ == '__main__':
	a = int(input())
	b = int(input())
	find_angle_mbc_python(a, b)

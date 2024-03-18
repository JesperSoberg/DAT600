def calc():
	for v4 in range(0, 2):
		for v5 in range(0, 2):
			z = 5*v4 - 5*((v5+v4) % 2)
			print(f'For v4: {v4}, v5:{v5}, z = {z}')

if __name__ == "__main__":
	calc()
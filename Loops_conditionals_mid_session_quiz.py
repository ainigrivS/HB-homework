#1
def draw_square(i):
	
	for x in range(i):
		x = ("*" +" ")* i 
		print x

draw_square(4)

#2
def draw_checkerboard(i):
	for i in range(i): 
		if i%2 == 0:
			y = ("X" + " " + "O" + " ") * 4
			print y
			
		else: 
			z = ("O" + " " + "X" + " ") * 4 
			print z
	i=i+1ct
draw_checkerboard(8)
	
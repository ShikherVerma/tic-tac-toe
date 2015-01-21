import sys
import time
import os
#display function start
def disp():
	for x in range(3):
		for y in range(3):
			if a[x][y] == -10:
				print "_  ",
			elif a[x][y] == 0 :
				print "O  ",
			else :
				print "X  ",
		print "\n"
#display function end

#check function 
def check():
	for x in range(3):
		sumrow = a[x][0] + a[x][1] + a[x][2] 
		if sumrow == 3:
			return -10
		elif sumrow == 0:
			return 10
	for x in range(3):
		sumcol = a[0][x] + a[1][x] + a[2][x] 
		if sumcol == 3:
			return -10
		elif sumcol == 0:
			return 10
	sumdiag1 = a[0][0] + a[1][1] + a[2][2]
	if sumdiag1 == 3:
		return -10
	elif sumdiag1 == 0:
		return 10
	sumdiag2 = a[0][2] + a[1][1] + a[2][0]
	if sumdiag2 == 3:
		return -10
	elif sumdiag2 == 0:
		return 10
	flag = 0  #flag is for checking if any move is possible
	for x in range(3):
		for y in range(3):
			if a[x][y] == -10:
				flag = 1
	if flag == 0:
		return 0
#check funtion end
#input
def user_move():
	x = int(input())
	y = int(input())	
	if x>2 or x < 0 or y>2 or y<0 or a[x][y] != -10 :
		 print "illegal move"
		 user_move()
	else :
		 a[x][y] = 1
#input close
#minmax start
def minmax(game,depth,move_whose):
	if check() == 10:
		return 10 - depth
	if check() == -10:
		return depth - 10
	if check() == 0:
		return 0
	maximum = -10000
	minimum = 10000
	for x in range(3):
		for y in range(3):
			if game[x][y] == -10:
				if move_whose:
					game[x][y] = 1
				else:
					game[x][y] = 0
				temp = minmax(game,depth+1,not(move_whose))
				if move_whose:
					if minimum > temp:
						minimum = temp
				else:
					if maximum < temp:
						maximum = temp
				game[x][y] = -10
	if move_whose:
		return minimum
	else:
		return maximum
#next move
def ttt_move():
	score = [[-100 for x in range(3)] for x in range(3)]
	for x in range(3):
		for y in range(3):
			if a[x][y] == -10:
				a[x][y] = 0
				score[x][y] = minmax(a,0,True)   #depth = 0 for 1st time and 3rd parameter is whose move it is False == computer and True == user
				a[x][y] = -10
	maximum = -100
	bestx = 1        
	besty = 1
	for x in range(3):
		for y in range(3):
			if score[x][y] > maximum:
				maximum = score[x][y]
				bestx = x
				besty = y 
	a[bestx][besty] = 0
#next move end
#initial choice
def initial_choice():
	ans = raw_input("wanna play first?")
	if ans == "n":
		ttt_move()
		disp()
	elif ans == "y":
		return
	elif ans !="y":
		print "What the fuck ! type y or n"
		initial_choice()
#initial_choice end
#int main
a = [[-10 for x in range(3)] for x in range(3)]
initial_choice()
while True :
	user_move()
	disp()
	if check() == -10:
		sys.exit("YOU WON MOTHERFUCKER!!!")
	elif check() == 0:
		sys.exit("IS THIS THE BEST YOU CAN DO??? SISSY PANTS!!!")
	print "thinking........"
	time.sleep(3)
	os.system('clear')
	ttt_move()
	disp()
	if check() == 10:
		sys.exit("FUCK OFF!!! GO CRY ON YOUR MAMMA LAP")
	elif check() == 0:
		sys.exit("IS THIS THE BEST YOU CAN DO??? SISSY PANTS!!!")

#int main end


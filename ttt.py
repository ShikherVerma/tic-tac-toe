'''
	Project - Tic Tic Tac Toe

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys#
import time#for wait of 1 seconds
import os
import random#for adding randomness into program so that the computer's move is not always the same
#display function start
def disp():
	for x in range(3):
		for y in range(3):
			if a[x][y] == -100:
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
			return -100
		elif sumrow == 0:
			return 100
	for x in range(3):
		sumcol = a[0][x] + a[1][x] + a[2][x] 
		if sumcol == 3:
			return -100
		elif sumcol == 0:
			return 100
	sumdiag1 = a[0][0] + a[1][1] + a[2][2]
	if sumdiag1 == 3:
		return -100
	elif sumdiag1 == 0:
		return 100
	sumdiag2 = a[0][2] + a[1][1] + a[2][0]
	if sumdiag2 == 3:
		return -100
	elif sumdiag2 == 0:
		return 100
	flag = 0  #flag is for checking if any move is possible
	for x in range(3):
		for y in range(3):
			if a[x][y] == -100:
				flag = 1
				return
	#code can be optimized here by removing flag and playing with the return statement, if loop exits the nested for then no a[][]=-100 so return 0
	if flag == 0:
		return 0
#check funtion end
#input
def user_move():
	x = int(input())
	y = int(input())	
	if x>2 or x < 0 or y>2 or y<0 or a[x][y] != -100 :
		 print "illegal move"
		 user_move()
	else :
		 a[x][y] = 1
#input close
#minmax start
def minmax(game,depth,move_whose):
	if check() == 100:
		return 100 - depth,0
	if check() == -100:
		return depth - 100,0
	if check() == 0:
		return 0,0
	maximum =-10000
	minimum = 10000
	trick=0
	trickmaxmove=0
	tricksumminmove=0
	trickmat = [[-10000 for x in range(3)] for x in range(3)]

	for x in range(3):
		for y in range(3):
			if game[x][y] == -100:
				if move_whose:
					game[x][y] = 1
				else:
					game[x][y] = 0
				temp,trick = minmax(game,depth+1,not(move_whose))
				trickmat[x][y]=trick
				if (temp==100-depth-1) and not(move_whose):#dont evaluate further if move is of computer and there is an instant win,
					#THIS ALSO REDUCES THE TRICK CASES WHERE WE INSTEAD OF CLAIMING INSTANT WIN , TRY TO MAKE A TRICK
					game[x][y]=-100
					return temp,trick
				#code can be optimized by moving these conditions into the if below
				if (temp==100-depth-2)and (move_whose):
					trick+=1
					disp()
					print "\n\n"
					time.sleep(1)
				if move_whose:
					tricksumminmove+=trick
					if minimum > temp:
						minimum = temp
				else:
					if maximum < temp:
						maximum = temp
						trickmaxmove=trick
				game[x][y] = -100
	if depth==0:
		print trickmat
	
	if move_whose:
		return minimum,tricksumminmove
	else:
		if tricksumminmove!=0:
			print trickforminmove
		return maximum,trickmaxmove
	
#next move
def ttt_move():
	score = [[-10000 for x in range(3)] for x in range(3)]
	trick = [[-10000 for x in range(3)] for x in range(3)]
	for x in range(3):
		for y in range(3):
			if a[x][y] == -100:
				a[x][y] = 0
				score[x][y],trick[x][y] = minmax(a,0,True)#round(random.random(),2)
				score[x][y]=score[x][y]+trick[x][y]#random() adds random values from 0 to 1 so that there is some randomness in the program
				#depth = 0 for 1st time and 3rd parameter is whose move it is False == computer and True == user
				a[x][y] = -100
	maximum = -10000
	bestx = 1
	besty = 1
	for x in range(3):
		for y in range(3):
			if score[x][y] > maximum:
				maximum = score[x][y]
				bestx = x
				besty = y 
	a[bestx][besty] = 0
	print score
	print trick
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
		print "type y or n"
		initial_choice()
#initial_choice end
#int main


'''a trick is defined as a position where for every move of the opponent the pc wins , 
if there is no sure short win already 
and if opponent plays a little non perfect by choosing the second least tree'''


a = [[-100 for x in range(3)] for x in range(3)]
initial_choice()
while True :
	user_move()
	disp()
	if check() == -100:
		sys.exit("YOU WON!!!")
	elif check() == 0:
		sys.exit("IS THIS THE BEST YOU CAN DO???!!!")
	print "thinking........"
	time.sleep(1)
	os.system('clear')
	ttt_move()
	disp()
	if check() == 100:
		sys.exit("YOU LOSE")
	elif check() == 0:
		sys.exit("IS THIS THE BEST YOU CAN DO???!!!")
#int main end


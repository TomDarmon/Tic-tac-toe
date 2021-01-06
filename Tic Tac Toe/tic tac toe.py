from scene import *
import ui

grid_cor = [(75,550),(250,550),(425,550),
						(75,350),(250,350),(425,350),
						(75,150),(250,150),(425,150)]

grid = [ 0,0,0, #0 = none, 1 = cross, 2 = circle
	 			 0,0,0,
	 			 0,0,0 ]
	 
load_view = True
	
def button_tapped(sender):
	reset_grid()
	print("button_tapped")
	global load_view
	load_view = True
	no_stroke()

					 
def reset_grid():
	global grid
	grid = [ 0,0,0, #0 = none, 1 = cross, 2 = circle
			 		 0,0,0,
					 0,0,0 ]
		
	
def get_index(x, y): # 1 = circle
	if (x > 25) and (x < 200) and (y > 100) and (y < 300):
		return 6
	elif (x > 25) and (x < 200) and (y > 300) and (y < 500):
		return 3
	elif (x > 25) and (x < 200) and (y > 500) and (y < 700):
		return 0
	elif (x > 200) and (x < 400) and (y > 300) and (y < 500):
		return 4	
	elif (x > 200) and (x < 400) and (y > 100) and (y < 300):
		return 7
	elif (x > 200) and (x < 400) and (y > 500) and (y < 700):
		return 1
	elif (x > 400) and (x < 600) and (y > 100) and (y < 300):
		return 8
	elif (x > 400) and (x < 600) and (y > 300) and (y < 500):
		return 5
	elif (x > 400) and (x < 600) and (y > 500) and (y < 700):
		return 2
	else:
		return False

def over(grid):
	k = 0
	for move in grid:
			if move != 0:
				k += 1
	if k == 9:
		stroke(255,0,0)
		return True
	
def win(grid):
	true = False
	new_grid = grid
	i = 0
	while i < len(new_grid) - 2: #checking for horizontal
		if new_grid[i] == new_grid[i + 1] == new_grid[i + 2] != 0:
			stroke(0,255,0)
			true = True
		i += 3
		
	i = 0
	while i < len(grid) / 3: #checking for vertical
		if new_grid[i] == new_grid[i+3] == new_grid[i + 6] != 0:
			stroke(0,255,0)
			true = True
		i += 1
		
	if new_grid[0] == new_grid[4] == new_grid[8] != 0: #checking for diagognals
		stroke(0,255,0)
		true = True
	elif new_grid[2] == new_grid[4] == new_grid[6] != 0:
		stroke(0,255,0)	
		true = True
	return true

	
def draw_lines():
		line(25, 300, 550, 300) #horizontal en bas
		line(25, 500, 550, 500) #horizontal en haut
		line(200, 100, 200, 700) #vertical a gauche
		line(400, 100, 400, 700) #vertical a droite
		
def draw_grid(grid):
		for i, move in enumerate(grid):
			if move == 1:
				ellipse(grid_cor[i][0],grid_cor[i][1], 25, 25)
			elif move == 2:
				ellipse(grid_cor[i][0], grid_cor[i][1], 100, 100)
												
		
def change_turn(played, next_move):
	if played:
		played = False
		next_move = 2
	else:
		played = True
		next_move = 1
	return played
							
								
class MyScene(Scene):

	def setup(self):
		no_stroke()
		self.background_color = "white"
		self.player_turn = True
		self.next_move = 1
		self.played = True
		
	def touch_began(self, touch):
		x, y = touch.location
		grid[get_index(x, y)] = self.next_move
		self.played = change_turn(self.played, self.next_move)
		if self.played == True:
			self.next_move = 1
		else:
			self.next_move = 2
			
	def draw(self):
		global load_view
		stroke_weight(10)
		if win(grid):		
			if load_view: #If we want to make the view appear
				ui.load_view('My UI').present('sheet') #make the view appear
				load_view = False # stop the view from appearing in the draw loop
		
		if over(grid): #check if the grid is full
			if load_view:
				ui.load_view('My UI').present('sheet')
				load_view = False
		draw_lines()
		draw_grid(grid)	#draw the moves (circle or cross) in the grid
		
run(MyScene())



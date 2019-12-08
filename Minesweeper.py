# -*- coding: utf-8 -*-
"""

@author: Edgar
"""
import random

class Node:
    def __init__(self, data, flag = False):
        self.data = data
        self.flag = flag
        

class MineSweeper(object):
    
    def __init__(self, Rows, Columns, Bombs):
        self.rows = Rows
        self.columns = Columns
        self.bombs = Bombs
        self.memory_clicks = []
        self.status = 'Currently PLaying'
        self.data_for_nodes = ' '
        self.grid = self.create_grid()
        
    def create_grid(self):
        grid = []
        for i in range(self.rows):
            r = []
            for j in range(self.columns):
                r.append(Node(self.data_for_nodes))
            
            grid.append(r)
        
        return grid
                
    def show_grid_admin(self):
        grid = []
        for row in self.grid:
            r = []
            for node in row:
                if node.flag:
                    if node.data == 'X':
                        r.append('XF')
                    else:
                        r.append('F')
                else:
                    r.append(node.data)
            grid.append(r)
        
        for row in grid:
            print(row)
            
    def show_grid_player(self):
        grid = []
        for row in self.grid:
            r = []
            for node in row:
                if node.flag:
                    r.append('F')
                elif node.data == 'X':
                    r.append(self.data_for_nodes)
                else:
                    r.append(node.data)
            grid.append(r)
        
        for row in grid:
            print(row)
                
                
    def place_bombs(self):
        Bombs = self.bombs
        
        while Bombs:
            random_location = (random.randint(0, self.rows-1), random.randint(0,self.columns-1))
            
            if self.grid[random_location[0]][random_location[1]].data != 'X':
                self.grid[random_location[0]][random_location[1]].data = 'X'
                Bombs-=1
                
        return
        
    def click(self, Location):
        assert type(Location) == tuple, 'Location must be a tuple'
        
        i, j = Location
        if self.grid[i][j].data == 'X':
            self.status = False
            
        elif self.grid[i][j].flag == True:
            return
            
        else:
            self.Flood(Location)
            
    def flag(self, Location):
        i, j = Location
        
        if (i,j) not in self.memory_clicks:
            self.grid[i][j].flag = not self.grid[i][j].flag
            
    def Flood(self, Location):
        if Location in self.memory_clicks:
            return
        else:
            self.memory_clicks.append(Location)
            i, j = Location
            neighbors = [(x,y) for x in range(i-1, i+2) for y in range(j-1, j+2) if 0<= x < self.rows and 0<= y < self.columns]
            
            neighbors_w_X = []
            direct_neighbors_wo_X = []
            for neighbor in neighbors:
                x, y = neighbor
                
                if self.grid[neighbor[0]][neighbor[1]].data == 'X':
                    neighbors_w_X.append(neighbor)
                else:
                    if self.grid[x][y].flag == False:
                        if neighbor!= Location:
                            if abs(neighbor[0] - i) == 1 and abs(neighbor[1] - j) == 1:
                                pass
                            else:
                                direct_neighbors_wo_X.append(neighbor)
    
            self.grid[i][j].data = len(neighbors_w_X)
            
            for direct_neighbor_wo_X in direct_neighbors_wo_X:
                self.Flood(direct_neighbor_wo_X)
                
                
    def Check_Status(self):
        if len(self.memory_clicks) == self.rows*self.columns - self.bombs:
            self.show_grid_admin()
            print('You have Won!')
            return True
        else:
            if self.status == False:
                self.show_grid_admin()
                print('You have Lost!')
                return True
                
        return False
            
    def Play(self):
        while self.status:
            self.show_grid_player()
            print('')
            self.show_grid_admin()
            print('')
            
            q = False
            action = 'NONE'
            while True:
                print('Select action: ')
                action = input('To flag enter [f], to click enter [c], to quit enter [q]: ')
                action.lower()
                if action == 'f' or action == 'c':
                    break
                elif action == 'q':
                    q = True
                    break
            if q:
                print('Thanks for playing!')
                break
            
            while True:
                i = int(input('Enter the row of the location you want to execute your action: '))
                j = int(input('Enter the column of the location you want to execute your action: '))
                
                try:
                    self.grid[i][j]
                    break
                except:
                    'Invalid input'
            Location = (i,j)
            
            if action == 'f':
                self.flag(Location)
            elif action == 'c':
                self.click(Location)
    
            
            if self.Check_Status() == True:
                print('Thanks for playing!')
                break
            
        
            
#-------------------------------------
Game = MineSweeper(5,5,8)
Game.place_bombs()
Game.Play()



        
        
        
        
        
        

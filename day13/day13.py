import os
import random
import time
class Universe():
    def __init__(self,W,H,P):
        self.H=H
        self.W=W
        self.P=P
        self.grid1 = [[' ' for i in range(W)] for j in range(H)]
        self.grid2 = [[' ' for i in range(W)] for j in range(H)]
        self.current_grid = self.grid1
        self.next_grid = self.grid2
    def be_alive(self,x,y):
        if x < 0 or x >= self.W or y < 0 or y >= self.H:
            return False
        return self.current_grid[y][x] == '*'
    def show(self):
        for row in self.current_grid:
            print(''.join(row))
        print()
        time.sleep(1)
    def seed(self):
        for row in self.current_grid:
            for i in range(len(row)):
                if random.random()<self.P:
                    row[i] = '*'
    def neighbors(self,x,y):
        count=0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i==0 and j==0:
                    continue
                nx,ny= x+i, y+j
                if (0<= nx<self.W)and(0<=ny<self.H)and self.be_alive(nx, ny):
                    count+=1
        return count
    def next(self, x, y):
        alive=self.be_alive(x,y)
        count=self.neighbors(x,y)
        if alive and (count<2 or count>3):
            return False
        elif not alive and count==3:
            return True
        return alive
    def step(self):
        self.current_grid, self.next_grid = self.next_grid, self.current_grid
        for y in range(self.H):
            for x in range(self.W):
                self.current_grid[y][x] = '*' if self.next(x, y) else ' '
def main():
    world=Universe(80,15,0.25)
    world.seed()
    for k in range(100):
        world.show()
        world.step()
if __name__=='__main__':
    main()


    
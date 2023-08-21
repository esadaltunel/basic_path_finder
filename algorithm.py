import time

matris = [["1","0","0","1","1"],
          ["A","0","0","0","0"],
          ["0","0","1","0","0"],
          ["1","1","0","0","0"],
          ["B","0","0","1","1"]]

def sqrt(nm):
    return nm**(1/2)

class Map:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.column = len(matrix[0])
        self.start = []
        self.end = []
        
        for i in range(len(self.matrix)):
            
            for j in range(len(self.matrix[i])):
                
                if matrix[i][j] == "1":
                    matrix[i][j] = "X"
                
                elif matrix[i][j] == "0":
                    matrix[i][j] = " "
                    
                elif matrix[i][j] == "A":
                    self.start = [i, j]
                    
                elif matrix[i][j] == "B":
                    self.end = [i, j]
                    
    def show_way(self, way):
        k = 0
        while True:
            if k == len(way):
                break
            cur_dot = way[k]
            for i in range(len(self.matrix)):
                
                for j in range(len(self.matrix[i])):
                    
                    if [i, j] == cur_dot:
                        print("#",end="  ")
                    else:
                        print(self.matrix[i][j], end="  ")
                
                print("\n")
            print("-----------------------")
            k += 1
            time.sleep(0.5)
        
class Algorithm(Map):
    
    def __init__(self, matrix):
        super().__init__(matrix)
        
    def h_score(self, p):
    	x, y = p
    	return sqrt(abs(x - self.end[0])**2 + abs(y - self.end[1])**2)
    
    def g_score(self, p):
        x, y = p
        return sqrt(abs(x - self.start[0])**2 + abs(y - self.start[1])**2)
    
    def bubbleSort(self, matrix):

    	for i in range(len(matrix)-1):

    		for j in range(0, len(matrix)-i-1):

    			if matrix[j][0] > matrix[j + 1][0]:
    				matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
    	return matrix
        
        
    def run(self):
        self.current_node = self.start
        self.path = [self.start]
        self.parent = [self.start]
        self.flag = 1
        
        self.way_list = []
        for i in range(len(self.matrix)):
            
            for j in range(len(self.matrix[i])):
                
                if self.matrix[i][j] != "X":
                    self.way_list.append([i, j])
            
        while True:
            temp = []
            x = self.current_node[0] # en başta 1
            y = self.current_node[1] # en başta 0
            if x < len(self.matrix) - 1: 
                if self.matrix[x + 1][y] != "X" and self.parent.count([x + 1,y]) == 0:
                            neg1_f = self.h_score([x+1, y]) - self.g_score([x+1, y])
                            neg1_indeks = [x + 1, y]
                            temp.append([neg1_f, neg1_indeks])
            if x != 0:
                if self.matrix[x - 1][y] != "X" and self.parent.count([x - 1,y]) == 0:
                            neg2_f = self.h_score([x-1, y]) - self.g_score([x-1, y])
                            neg2_indeks = [x - 1, y]
                            temp.append([neg2_f, neg2_indeks])
            if y < len(self.matrix[0]) -1:
                if self.matrix[x][y + 1] != "X"and self.parent.count([x,y+1]) == 0:
                            neg3_f = self.h_score([x, y+1]) - self.g_score([x, y+1])
                            neg3_indeks = [x, y + 1]
                            temp.append([neg3_f, neg3_indeks])
            if y != 0:
                if self.matrix[x][y - 1] != "X"and self.parent.count([x,y-1]) == 0:
                            neg4_f = self.h_score([x, y-1]) - self.g_score([x, y-1])
                            neg4_indeks = [x,y - 1]
                            temp.append([neg4_f, neg4_indeks])

            if not bool(temp):
                try: 
                    self.way_list.remove(self.current_node)
                    self.current_node = self.start
                    self.path = []
                except ValueError:
                    print("Way couldn't find")
                    self.flag = 0
                    break
                    

            else: 
                self.parent.append(self.current_node)
                self.current_node = self.bubbleSort(temp)[0][1]
                self.path.append(self.current_node)


            if self.current_node == self.end:
                self.flag = 1
                break



                
                        
                
    

 
maze = Algorithm(matris) 
maze.run()
if maze.flag:
    maze.show_way(maze.path)

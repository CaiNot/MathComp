import moudel


class FindPath:
    nodes = []
    D = []
    paths = []
    length = 0
    graph = None

    def __init__(self, graph_input):
        self.graph = graph_input
        self.nodes = graph_input.nodes
        self.length = self.graph.length
        self.D = [[[0 for j in range(self.length + 1)]
                   for i in range(self.length + 1)]
                  for k in range(self.length + 1)]
        self.paths = [[[0 for j in range(self.length + 1)]
                       for i in range(self.length + 1)]
                      for k in range(self.length + 1)]

    def solveByFloydWarshall(self):
        self.D[0] = self.nodes

        for i in range(0, self.length+1):
            # self.paths[0][i] = [0 for i in range(self.length)]
            for j in range(0, self.length+1):
                self.paths[0][i][j] = i if self.graph.hasEdge(i, j) else -1

        t1 = 0
        t2 = 0
        for k in range(1, self.length + 1):
            for i in range(1, self.length + 1):
                for j in range(1, self.length + 1):
                    # print(k, i, j)
                    t1 = self.D[k - 1][i][j]
                    t2 = self.D[k - 1][i][k] + self.D[k - 1][k][j]
                    if t1 <= t2:
                        if t1 < 32767:
                            self.D[k][i][j] = t1
                            self.paths[k][i][j] = self.paths[k - 1][i][j]
                        else:
                            self.D[k][i][j] = 32867
                            self.paths[k][i][j] = -1
                    else:
                        if t2 < 32767:
                            self.D[k][i][j] = t2
                            self.paths[k][i][j] = self.paths[k - 1][k][j]
                        else:
                            self.D[k][i][j] = 32867
                            self.paths[k][i][j] = -1

    def showD(self):
        # for k in range(self.length):
        print("D", self.length)
        for i in range(1, self.length + 1):
            for j in range(1, self.length + 1):
                print(self.D[self.length][i][j], end='\t')
            print()

    def showPath(self):
        # for k in range(self.length):
        print("P", self.length)

        for i in range(1, self.length + 1):
            for j in range(1, self.length + 1):
                print(self.paths[self.length][i][j], end='\t')
            print()


fileProc = moudel.FileProc()
fileProc.readGraph()
findPath = FindPath(fileProc.graph)

findPath.solveByFloydWarshall()
findPath.showD()
print()
findPath.showPath()

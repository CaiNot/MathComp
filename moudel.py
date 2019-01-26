UNREACHABLE = 100


class Graph:
    nodes = []
    length = 0

    def hasEdge(self, i, j):
        return i != j and self.nodes[i][j] < UNREACHABLE


class FileProc:
    input_path = "input.dat"
    output_path = "output.dat"
    graph = Graph()

    def readGraph(self):

        with open(self.input_path, 'r') as input_file:
            vex_num = int(input_file.readline().strip('\n'))
            list_vexs = input_file.readlines()
            self.graph.length = vex_num
            self.graph.nodes.append([0 for i in range(vex_num+1)])

            for i in range(vex_num):
                vexs = [0]
                for vex in list_vexs[i].strip('\n').split():
                    vex = int(vex)
                    vex = vex if vex < 100 else 32867
                    vexs.append(vex)
                self.graph.nodes.append(vexs)
            print("read over")

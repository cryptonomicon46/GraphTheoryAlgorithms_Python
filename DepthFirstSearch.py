
class Node():

    leafSum= 0 
    def __init__(self,name):
        self.name = name
        self.children= []

    def addChild(self,name):
        self.children.append(Node(name))
        return self

    
    def addLeafSum(self):
        print(f"Added {self.name}")
        self.leafSum += self.name


    def sizeOf(self):
        return len(self.children)

    def isleafNode(self):
        if self.sizeOf()== 0:
            return self.name

    #Print V traverse to children print them before continuining to print other Vs
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

    #Find the sum of the leaf nodes only
    def sumLeafNodes(self):
        if self.isleafNode():
            return self.name
        total=0 
        for child in self.children:
            total += child.sumLeafNodes()
        return total
                

    # def treeHeight(self):
    #     for child in self.children:
    #         height = max(child.treeHeight(),
if __name__ == "__main__":
        graph1 = Node("A")
        graph1.addChild("B").addChild("C").addChild("D")
        graph1.children[0].addChild("E").addChild("F")
        graph1.children[2].addChild("G").addChild("H")
        graph1.children[0].children[1].addChild("I").addChild("J")
        graph1.children[2].children[0].addChild("K")

        graph2 = Node(5)
        graph2.addChild(4).addChild(3)
        graph2.children[0].addChild(1).addChild(-6)
        graph2.children[0].children[0].addChild(2).addChild(9)
        graph2.children[1].addChild(0).addChild(7).addChild(-4)
        graph2.children[1].children[1].addChild(8)



        print("\n======= GRAPH ============")
        print("""          A         """)
        print("""        / |  \      """)
        print("""       B  C  D     """)
        print("""      / \   /  \   """)
        print("""     E   F  G    H  """)
        print("""        /  \  \      """)
        print("""       I    J  K  \n""")


        print("\n======= GRAPH1 ============")
        print("""          5         """)
        print("""        /     \      """)
        print("""       4       3     """)
        print("""      / \    /  | \  """)
        print("""     1   -6  0  7  -4  """)
        print("""    /  \        |      """)
        print("""   2    9       8   \n""")

        dfs_check1 = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
        dfs_check2 = [5, 4, 1, 2, 9, -6, 3, 0, 7, 8, -4]
        dfs_output1 =[]
        dfs_output2 =[]
        graph1.depthFirstSearch(dfs_output1)
        graph2.depthFirstSearch(dfs_output2)
        leafSum = graph2.sumLeafNodes()

        test1 = (dfs_output1 == dfs_check1)
        test2 = (dfs_output2 == dfs_check2)
        test3 = (leafSum == 9)  # (2,9,-6,0,8,-4)

        print("TEST1: Checking DFS ARRAY \n ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H'] \n")
        print("DFS TEST1 PASS\n" if test1 else "DFS TEST1 FAIL") #Ternary Operator
        print("TEST2: Checking DFS ARRAY  \n [5, 4, 1, 2, 9, -6, 3, 0, 7, 8, -4]")
        print("DFS TEST2 PASS \n" if test2 else "DFS TEST2 FAIL \n") 
        print("TEST3: Checking DFS Leaf Node SUM:  \n[2,9,-6,0,8,-4]  = 9")
        print("DFS TEST3 PASS \n" if test3 else "DFS TEST3 FAIL \n") 

        print("\n")

        #Time Complexity O(V+E)  V= Vertices, E = Edges 
        #Space Complexity O(V))




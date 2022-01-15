import unittest
from DepthFirstSearch import *

class test_DepthFirstSearch(unittest.TestCase):
    def setUp(self):

        self.graph1 = Node("A")
        self.graph1.addChild("B").addChild("C").addChild("D")
        self.graph1.children[0].addChild("E").addChild("F")
        self.graph1.children[2].addChild("G").addChild("H")
        self.graph1.children[0].children[1].addChild("I").addChild("J")
        self.graph1.children[2].children[0].addChild("K")

        self.graph2 = Node(5)
        self.graph2.addChild(4).addChild(3)
        self.graph2.children[0].addChild(1).addChild(-6)
        self.graph2.children[0].children[0].addChild(2).addChild(9)
        self.graph2.children[1].addChild(0).addChild(7).addChild(-4)
        self.graph2.children[1].children[1].addChild(8)

        self.leafSum  = 0
        self.dfs_check1 = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
        self.dfs_check2 = [5, 4, 1, 2, 9, -6, 3, 0, 7, 8, -4]
        self.dfs_output1 =[]
        self.dfs_output2 =[]

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

       

        print("\n")

    def test_depthFirstSearch(self):
       
        self.graph1.depthFirstSearch(self.dfs_output1)
        self.graph2.depthFirstSearch(self.dfs_output2)
        self.leafSum = self.graph2.sumLeafNodes()

        self.assertEqual(self.dfs_check1,self.dfs_output1)
        self.assertEqual(self.dfs_check2,self.dfs_output2)
        self.assertEqual(9,self.leafSum)

      
    def tearDown(self):
        self.graph1 = None
        self.graph2 = None
        self.dfs_check1 = None
        self.dfs_check2 = None
        self.dfs_output1 = None
        self.dfs_output2 = None


if __name__ == "__main__":
    unittest.main()

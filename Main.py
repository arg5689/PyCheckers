import GameBoard, sys

class Main:
    def __init__(self):
        self.game = GameBoard.GameBoard(self.startup())
        self.test()


    def startup(self):
        ##################
        # if 1<10:
        #     return "Board3" # THIS LINE FOR TESTING PURPOSES ONLY
        ##################
        print("Welcome!!!\n"
              "This is a game of checkers.\n"
              "Please Choose a Board:\n"
              "\n"
              "1:\n"
              "")
        while True:
            input1 = input()
            if input1 == "2":
                return "Board" + input1
            elif input1 == "":
                return "Board" + input1


    def mainMenu(self):
        print("Main Menu:\n\n"
              "Please enter a menu choice:\n"
              "1. Start Game with two players\n"
              "2. Change Boards\n"
              "3. Quit\n")

        while True:
            choice = input()
            if choice == "1":
                self.Game()
            elif choice == "2":
                Main()
            elif choice == "3":
                sys.exit("Exited")
            else:
                print("Not in range")

    def test(self):
        #self.game.drawBoard()
        #self.mainMenu()
        self.game.Game()
        # x = GameBoard("Board2")
        # x.drawBoard()
        # #x.updatePosition(3, 7, 4, 10)
        # #x.drawBoard()
        # #x.updatePosition(H2[0],H2[1],D2[0],D2[1])
        #
        # x.deletePiece(H2[0], H2[1])
        # x.deletePiece(H4[0], H4[1])
        # x.deletePiece(H6[0], H6[1])
        # x.deletePiece(H8[0], H8[1])
        # x.drawBoard()
        #
        # x.deletePiece(G1[0], G1[1])
        # x.deletePiece(G3[0], G3[1])
        # x.deletePiece(G5[0], G5[1])
        # x.deletePiece(G7[0], G7[1])
        # x.drawBoard()
        #
        # x.deletePiece(F2[0], F2[1])
        # x.deletePiece(F4[0], F4[1])
        # x.deletePiece(F6[0], F6[1])
        # x.deletePiece(F8[0], F8[1])
        # x.drawBoard()
        #
        # x.deletePiece(E1[0], E1[1])
        # x.deletePiece(E3[0], E3[1])
        # x.deletePiece(E5[0], E5[1])
        # x.deletePiece(E7[0], E7[1])
        # x.drawBoard()
        #
        # x.deletePiece(D2[0], D2[1])
        # x.deletePiece(D4[0], D4[1])
        # x.deletePiece(D6[0], D6[1])
        # x.deletePiece(D8[0], D8[1])
        # x.drawBoard()
        #
        # x.deletePiece(C1[0], C1[1])
        # x.deletePiece(C3[0], C3[1])
        # x.deletePiece(C5[0], C5[1])
        # x.deletePiece(C7[0], C7[1])
        # x.drawBoard()
        #
        # x.deletePiece(B2[0], B2[1])
        # x.deletePiece(B4[0], B4[1])
        # x.deletePiece(B6[0], B6[1])
        # x.deletePiece(B8[0], B8[1])
        # x.drawBoard()
        #
        # x.deletePiece(A1[0], A1[1])
        # x.deletePiece(A3[0], A3[1])
        # x.deletePiece(A5[0], A5[1])
        # x.deletePiece(A7[0], A7[1])
        # x.drawBoard()



Main()
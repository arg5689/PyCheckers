class GameBoard:

    def __init__(self, boardChoice):
        self.file = boardChoice
        with open(self.file) as file:
            lines = file.readlines()

        stuff = []
        for line in lines:
            stuff.append(list(str(line.rstrip())))
        self.nestedBoard = stuff
        self.piecesLeftRed = 12  #Red is player 1
        self.piecesLeftBlack = 12  #Black is player 2
        self.raw_location_list = self.locations()
        self.map = ["A1","A3","A5","A7","B2","B4","B6","B8","C1","C3","C5","C7","D2","D4","D6","D8","E1","E3","E5","E7","F2","F4","F6","F8","G1","G3","G5","G7","H2","H4","H6","H8"]
        self.jump = False


    def drawBoard(self):
        counter = 0
        for itemx in self.nestedBoard:     #Y-Axis of board
            print()  #adds new line for printing correctly

            for itemy in self.nestedBoard[counter]:       #X-Axis of board
                print(itemy, end="")
            counter += 1
        print()
        return


    def movePiece(self, oldLoc, newLoc):
        print(oldLoc)
        print(newLoc)
        temp = self.nestedBoard[oldLoc[0]][oldLoc[1]]
        self.nestedBoard[oldLoc[0]][oldLoc[1]] = " "
        self.nestedBoard[newLoc[0]][newLoc[1]] = temp
        return

    def deletePiece(self,piece):
        self.nestedBoard[piece[0]][piece[1]] = " "


    def available_moves(self,location ,start_piece,  turn):
        list_of_moves = []
        if start_piece == "o":
            #this is the left most pieces for the 'o'
            if location[1] == 4 and self.nestedBoard[(location[0]-1)][(location[1]+3)] == " ":
                list_of_moves.append([(location[0]-1),(location[1]+3)])
            elif location[1] == 4 and \
                (self.nestedBoard[(location[0]-1)][(location[1]+3)] == "X" or self.nestedBoard[(location[0]-1)][(location[1]+3)] == "K")\
                and self.nestedBoard[(location[0]-2)][(location[1]+6)] == " ":
                list_of_moves.append([(location[0] - 2), (location[1] + 6)])
                self.jump = True

            # this is for the left non-jump middle of the board pieces 'o'
            elif (self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == " ") and (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22):
                list_of_moves.append([(location[0] - 1), (location[1] - 3)])

            #jump-left 'o'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0]-1)][(location[1]-3)] == "X" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "K"):
                    if self.nestedBoard[(location[0]-2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] - 2), (location[1] - 6)])
                        self.jump = True

            #this is for the right non-jump middle of the board pieces 'o'
            if (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and (self.nestedBoard[(location[0]-1)][(location[1]+3)] == " "):
                list_of_moves.append([(location[0] - 1), (location[1] + 3)])

            # jump-right 'o'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[
                1] == 19 or location[1] == 22) \
                 and \
                 (self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "X" or
                  self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "K"):
                if self.nestedBoard[(location[0] - 2)][(location[1] + 6)] == " ":
                    list_of_moves.append([(location[0] - 2), (location[1] + 6)])
                    self.jump = True

            # right most 'o' pieces of the board, non-jump
            if (self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == " ") and (location[1] == 25):
                list_of_moves.append([(location[0] - 1), (location[1] - 3)])

            # right most 'o' pieces of the board, jumping
            elif (location[1] == 25) and (self.nestedBoard[(location[0]-1)][(location[1]-3)] == "X" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "K"):
                    if self.nestedBoard[(location[0]-2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] - 2), (location[1] - 6)])
                        self.jump = True

        if start_piece == "8":
            #this is the left most pieces for the '8'
            if location[1] == 4 and self.nestedBoard[(location[0]-1)][(location[1]+3)] == " ":
                list_of_moves.append([(location[0]-1),(location[1]+3)])
            elif location[1] == 4 and \
                (self.nestedBoard[(location[0]-1)][(location[1]+3)] == "X" or self.nestedBoard[(location[0]-1)][(location[1]+3)] == "K")\
                and self.nestedBoard[(location[0]-2)][(location[1]+6)] == " ":
                list_of_moves.append([(location[0] - 2), (location[1] + 6)])
                self.jump = True

            # this is for the left non-jump middle of the board pieces '8'
            elif (self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == " ") and (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22):
                list_of_moves.append([(location[0] - 1), (location[1] - 3)])

            #jump-left '8'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0]-1)][(location[1]-3)] == "X" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "K"):
                    if self.nestedBoard[(location[0]-2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] - 2), (location[1] - 6)])
                        self.jump = True

            #this is for the right non-jump middle of the board pieces '8'
            if (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and (self.nestedBoard[(location[0]-1)][(location[1]+3)] == " "):
                list_of_moves.append([(location[0] - 1), (location[1] + 3)])

            # jump-right '8'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[
                1] == 19 or location[1] == 22) \
                 and \
                 (self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "X" or
                  self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "K"):
                if self.nestedBoard[(location[0] - 2)][(location[1] + 6)] == " ":
                    list_of_moves.append([(location[0] - 2), (location[1] + 6)])
                    self.jump = True

            # right most '8' pieces of the board, non-jump
            if (self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == " ") and (location[1] == 25):
                list_of_moves.append([(location[0] - 1), (location[1] - 3)])

            # right most '8' pieces of the board, jumping
            elif (location[1] == 25) and (self.nestedBoard[(location[0]-1)][(location[1]-3)] == "X" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "K"):
                    if self.nestedBoard[(location[0]-2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] - 2), (location[1] - 6)])
                        self.jump = True

            # this is the left most pieces for the '8'
            if location[1] == 4 and self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == " ":
                list_of_moves.append([(location[0] + 1), (location[1] + 3)])
            elif location[1] == 4 and \
                    (self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "X" or
                     self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "K") \
                    and self.nestedBoard[(location[0] + 2)][(location[1] + 6)] == " ":
                list_of_moves.append([(location[0] + 2), (location[1] + 6)])
                self.jump = True

            # this is for the left non-jump middle of the board pieces '8'
            elif (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == " ") and (
                    location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or
                    location[1] == 19 or location[1] == 22):
                list_of_moves.append([(location[0] + 1), (location[1] - 3)])

            # jump-left '8'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or
                  location[1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "X" or
                     self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == "K"):
                if self.nestedBoard[(location[0] + 2)][(location[1] - 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] - 6)])
                    self.jump = True

            # this is for the right non-jump middle of the board pieces '8'
            if (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[
                1] == 19 or location[1] == 22) \
                    and (self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == " "):
                list_of_moves.append([(location[0] + 1), (location[1] + 3)])

            # jump-right '8'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or
                  location[
                      1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "X" or
                     self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "K"):
                if self.nestedBoard[(location[0] + 2)][(location[1] + 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] + 6)])
                    self.jump = True

            # right most '8' pieces of the board, non-jump
            if (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == " ") and (location[1] == 25):
                list_of_moves.append([(location[0] + 1), (location[1] - 3)])

            # right most '8' pieces of the board, jumping
            elif (location[1] == 25) and (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "X" or
                                          self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "K"):
                if self.nestedBoard[(location[0] + 2)][(location[1] - 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] - 6)])
                    self.jump = True

        if start_piece == "X":
            #this is the left most pieces for the 'X'
            if location[1] == 4 and self.nestedBoard[(location[0]+1)][(location[1]+3)] == " ":
                list_of_moves.append([(location[0]+1),(location[1]+3)])
            elif location[1] == 4 and \
                (self.nestedBoard[(location[0]+1)][(location[1]+3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]+3)] == "8")\
                and self.nestedBoard[(location[0]+2)][(location[1]+6)] == " ":
                list_of_moves.append([(location[0] + 2), (location[1] + 6)])
                self.jump = True

            # this is for the left non-jump middle of the board pieces 'X'
            elif (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == " ") and (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22):
                list_of_moves.append([(location[0] + 1), (location[1] - 3)])

            #jump-left 'X'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0]+1)][(location[1]-3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "8"):
                    if self.nestedBoard[(location[0]+2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] + 2), (location[1] - 6)])
                        self.jump = True

            #this is for the right non-jump middle of the board pieces 'X'
            if (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and (self.nestedBoard[(location[0]+1)][(location[1]+3)] == " "):
                list_of_moves.append([(location[0] + 1), (location[1] + 3)])

            # jump-right 'X'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[
                1] == 19 or location[1] == 22) \
                 and \
                 (self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "o" or
                  self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "8"):
                if self.nestedBoard[(location[0] + 2)][(location[1] + 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] + 6)])
                    self.jump = True

            # right most 'X' pieces of the board, non-jump
            if (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == " ") and (location[1] == 25):
                list_of_moves.append([(location[0] + 1), (location[1] - 3)])

            # right most 'X' pieces of the board, jumping
            elif (location[1] == 25) and (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "o" or
                                          self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "8"):
                if self.nestedBoard[(location[0] + 2)][(location[1] - 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] - 6)])
                    self.jump = True

        if start_piece == "K":
            #this is the left most pieces for the 'K'
            if location[1] == 4 and self.nestedBoard[(location[0]+1)][(location[1]+3)] == " ":
                list_of_moves.append([(location[0]+1),(location[1]+3)])
            elif location[1] == 4 and \
                (self.nestedBoard[(location[0]+1)][(location[1]+3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]+3)] == "8")\
                and self.nestedBoard[(location[0]+2)][(location[1]+6)] == " ":
                list_of_moves.append([(location[0] + 2), (location[1] + 6)])
                self.jump = True

            # this is for the left non-jump middle of the board pieces 'K'
            elif (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == " ") and (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22):
                list_of_moves.append([(location[0] + 1), (location[1] - 3)])

            #jump-left 'K'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0]+1)][(location[1]-3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "8"):
                    if self.nestedBoard[(location[0]+2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] + 2), (location[1] - 6)])
                        self.jump = True

            #this is for the right non-jump middle of the board pieces 'K'
            if (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and (self.nestedBoard[(location[0]+1)][(location[1]+3)] == " "):
                list_of_moves.append([(location[0] + 1), (location[1] + 3)])

            # jump-right 'K'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[
                1] == 19 or location[1] == 22) \
                 and \
                 (self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "o" or
                  self.nestedBoard[(location[0] + 1)][(location[1] + 3)] == "8"):
                if self.nestedBoard[(location[0] + 2)][(location[1] + 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] + 6)])
                    self.jump = True

            # right most 'K' pieces of the board, non-jump
            if (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == " ") and (location[1] == 25):
                list_of_moves.append([(location[0] + 1), (location[1] - 3)])

            # right most 'K' pieces of the board, jumping
            elif (location[1] == 25) and (self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "o" or
                                          self.nestedBoard[(location[0] + 1)][(location[1] - 3)] == "8"):
                if self.nestedBoard[(location[0] + 2)][(location[1] - 6)] == " ":
                    list_of_moves.append([(location[0] + 2), (location[1] - 6)])
                    self.jump = True

            if location[1] == 4 and self.nestedBoard[(location[0]-1)][(location[1]+3)] == " ":
                list_of_moves.append([(location[0]-1),(location[1]+3)])
            elif location[1] == 4 and \
                (self.nestedBoard[(location[0]-1)][(location[1]+3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]+3)] == "8")\
                and self.nestedBoard[(location[0]-2)][(location[1]+6)] == " ":
                list_of_moves.append([(location[0] - 2), (location[1] + 6)])
                self.jump = True

            # this is for the left non-jump middle of the board pieces 'K'
            elif (self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == " ") and (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22):
                list_of_moves.append([(location[0] - 1), (location[1] - 3)])

            #jump-left 'K'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and \
                    (self.nestedBoard[(location[0]-1)][(location[1]-3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "8"):
                    if self.nestedBoard[(location[0]-2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] - 2), (location[1] - 6)])
                        self.jump = True

            #this is for the right non-jump middle of the board pieces 'K'
            if (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[1] == 19 or location[1] == 22) \
                    and (self.nestedBoard[(location[0]-1)][(location[1]+3)] == " "):
                list_of_moves.append([(location[0] - 1), (location[1] + 3)])

            # jump-right 'K'
            elif (location[1] == 7 or location[1] == 10 or location[1] == 13 or location[1] == 16 or location[
                1] == 19 or location[1] == 22) \
                 and \
                 (self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "o" or
                  self.nestedBoard[(location[0] - 1)][(location[1] + 3)] == "8"):
                if self.nestedBoard[(location[0] - 2)][(location[1] + 6)] == " ":
                    list_of_moves.append([(location[0] - 2), (location[1] + 6)])
                    self.jump = True

            # right most 'K' pieces of the board, non-jump
            if (self.nestedBoard[(location[0] - 1)][(location[1] - 3)] == " ") and (location[1] == 25):
                list_of_moves.append([(location[0] - 1), (location[1] - 3)])

            # right most 'K' pieces of the board, jumping
            elif (location[1] == 25) and (self.nestedBoard[(location[0]-1)][(location[1]-3)] == "o" or self.nestedBoard[(location[0]-1)][(location[1]-3)] == "8"):
                    if self.nestedBoard[(location[0]-2)][(location[1]-6)] == " ":
                        list_of_moves.append([(location[0] - 2), (location[1] - 6)])
                        self.jump = True

        if list_of_moves == []:
            print("You chose a piece with no possible moves.")
            # print(location[1])
            # print(start_piece)

        return list_of_moves


    def fill_all_spaces(self, character_to_use):
        """
        for testing initial spacing system
        """
        for item in self.raw_location_list:
            self.nestedBoard[item[0]][item[1]] = character_to_use


    def getPiece(self,location):
        cat = self.raw_location_list[self.map.index(location)]
        #print(self.map.index(location))     #used for testing purposes
        return self.nestedBoard[cat[0]][cat[1]]

    def Turn(self, turn):
        if turn:
            print("\nPlayer ONE's turn.\n"
                  "------------------")
        else:
            print("\nPlayer TWO's turn.\n"
                  "------------------")

        self.drawBoard()
        while True:
            print("Choose a piece to move: ")
            input1 = input()
            if input1.upper() in self.map:
                yours = False
                empty = True

                if turn:
                    if self.getPiece(input1.upper()) == "o" or self.getPiece(input1.upper()) == "8":
                        yours = True
                        empty = False
                    if self.getPiece(input1.upper()) == "X" or self.getPiece(input1.upper()) == "K":
                        yours = False
                        empty = False
                    if self.getPiece(input1.upper()) == " ":
                        empty = True

                else:
                    if self.getPiece(input1.upper()) == "X" or self.getPiece(input1.upper()) == "K":
                        yours = True
                        empty = False
                    if self.getPiece(input1.upper()) == "o" or self.getPiece(input1.upper()) == "8":
                        yours = False
                        empty = False
                    if self.getPiece(input1.upper()) == " ":
                        empty = True


                if yours == True and empty == False:
                    #print(self.getPiece(input1.upper()))
                    moves = self.available_moves(self.raw_location_list[self.map.index(input1.upper())], self.getPiece(input1.upper()), turn)
                    if moves == []:
                        self.Turn(turn)
                        break
                    print(moves)
                    print("Choose a new location for the piece selected")
                    newLoc = input()
                    start = self.raw_location_list[self.map.index(input1.upper())]
                    end = moves[int(newLoc)-1]
                    middle = []
                    print(end[0]+1)
                    print(end[1]-3)
                    if (end[0] > start[0]) and (end[1] > start[1]):
                        middle.append(end[0]-1)
                        middle.append(end[1]-3)
                    elif (end[0] > start[0]) and (end[1] < start[1]):
                        middle.append(end[0] - 1)
                        middle.append(end[1] + 3)
                    elif (end[0] < start[0]) and (end[1] > start[1]):
                        middle.append(end[0]+1)
                        middle.append(end[1]-3)
                    elif (end[0] < start[0]) and (end[1] < start[1]):
                        middle.append(end[0] + 1)
                        middle.append(end[1] + 3)

                    print(start)
                    print(end)
                    print(middle)
                    print("above")
                    self.movePiece(self.raw_location_list[self.map.index(input1.upper())], moves[int(newLoc)-1])
                    if self.jump:
                        self.deletePiece(middle)
                        self.jump = False
                    if turn and end[0] == 1:
                        print("Your piece has been kinged.")
                        self.nestedBoard[end[0]][end[1]] = "8"
                    if not turn and end[0] == 8:
                        print("Your piece has been kinged.")
                        self.nestedBoard[end[0]][end[1]] = "K"


                    return
                elif empty == True:
                    print("That space is empty, Try again.")
                elif yours == False:
                    print("That piece isn't  yours, Try again.")
            else:
                print("That is not a usable space or something weird was typed!  Try again.")

        return

    def Game(self):
        turn = True
        while self.piecesLeftBlack != 0 and self.piecesLeftRed != 0:
            self.Turn(turn)
            #input()
            self.piecesLeftRed-=2

            if turn:
                turn = False
            else:
                turn = True


    def locations(self):
        alist = []
        H2 = [1,7]
        H4 = [1,13]
        H6 = [1,19]
        H8 = [1,25]
        G1 = [2,4]
        G3 = [2,10]
        G5 = [2,16]
        G7 = [2,22]
        F2 = [3,7]
        F4 = [3,13]
        F6 = [3,19]
        F8 = [3,25]
        E1 = [4,4]
        E3 = [4,10]
        E5 = [4,16]
        E7 = [4,22]
        D2 = [5,7]
        D4 = [5,13]
        D6 = [5,19]
        D8 = [5,25]
        C1 = [6,4]
        C3 = [6,10]
        C5 = [6,16]
        C7 = [6,22]
        B2 = [7,7]
        B4 = [7,13]
        B6 = [7,19]
        B8 = [7,25]
        A1 = [8,4]
        A3 = [8,10]
        A5 = [8,16]
        A7 = [8,22]
        alist.append(A1)
        alist.append(A3)
        alist.append(A5)
        alist.append(A7)
        alist.append(B2)
        alist.append(B4)
        alist.append(B6)
        alist.append(B8)
        alist.append(C1)
        alist.append(C3)
        alist.append(C5)
        alist.append(C7)
        alist.append(D2)
        alist.append(D4)
        alist.append(D6)
        alist.append(D8)
        alist.append(E1)
        alist.append(E3)
        alist.append(E5)
        alist.append(E7)
        alist.append(F2)
        alist.append(F4)
        alist.append(F6)
        alist.append(F8)
        alist.append(G1)
        alist.append(G3)
        alist.append(G5)
        alist.append(G7)
        alist.append(H2)
        alist.append(H4)
        alist.append(H6)
        alist.append(H8)
        return alist

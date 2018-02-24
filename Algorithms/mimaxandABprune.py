def minimax(self, H, V, depth, myPlayer):
    if(depth == 0 or self.game_ends(H,V)):
        return evaluate()

    if(myPlayer):
        bestValue = 0
        for move in list_possible_moves(H,V):
            newH, newV, score = self.next_state(move, H, V)

            value = minimax(newH, newV, depth-1, False)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = 36
        for move in list_possible_moves(H,V):
            newH, newV, score = self.next_state(move, H, V)

            value = minimax(newH, newV, depth-1, True)
            bestValue = min(bestValue, value)
        return bestValue


def alphabetapruning(self, H, V, depth, A, B, myPlayer):
    if(depth == 0 or self.game_ends(H,V)):
        return evaluate()

    if(myPlayer):
        bestValue = 0
        for move in list_possible_moves(H,V):
            newH, newV, score = self.next_state(move, H, V)

            value = max(value, minimax(newH, newV, depth-1, False))
            A = max(A, value)
            if(B <= A):
                break
        return value
    else:
        bestValue = 36
        for move in list_possible_moves(H,V):
            newH, newV, score = self.next_state(move, H, V)

            value = min(value, minimax(newH, newV, depth-1, True))
            B = min (B, value)
            if(B <= A):
                break
        return value

















#Modded minimax, works well enough.....
#This is most recent








        def minimax(self, H, V, depth, originDepth, myPlayer, playerID, points):
        if(depth == 0 or self.game_ends(H,V)):
            return points#self.evaluate(H,V,playerID, points)


        movelist = self.list_possible_moves(H,V)
        temp_h = H
        temp_v = V
        next_move=self.list_possible_moves(H,V);
        bestMove = movelist[0];
        best_score=0;
        for move in movelist:
            temp_h,temp_v,score=self.next_state(move,temp_h,temp_v);
            if(score>best_score):
                best_score=score;
                bestMove=move;

        if(myPlayer):
            bestValue = 0
            
            for move in movelist:
                newH, newV, score = self.next_state(move, H, V)
                #pointVal = points + score
                value = self.minimax(newH, newV, depth-1, originDepth, False, playerID, score)
                if(playerID == 1):
                    scoring = value + self.score_player2
                else:
                    scoring = value + self.score_player1
                if(bestValue < scoring):
                    bestValue = scoring
                    bestMove = move
            if(depth == originDepth):
                self.make_move(bestMove, playerID)
            return bestValue
        else:
            bestValue = 36
            #movelist = self.list_possible_moves(H,V)
            for move in movelist:
                newH, newV, score = self.next_state(move, H, V)
                #pointVal = points + score
                value = self.minimax(newH, newV, depth-1, originDepth, True, playerID, score)
                if(playerID == 1):
                    scoring = -value + self.score_player2
                else:
                    scoring = -value + self.score_player1
                if(bestValue > scoring):
                    bestValue = scoring
            return bestValue 





#Older minimax
#THIS IS OPTIMAL


    def minimax(self, H, V, depth, maxingPlyr):
        goodChoice = [-1,-1,-1]       

        if (maxingPlyr):
            worth = 0
            movelist = self.list_possible_moves(H,V)
            for move in movelist:
                
                newH, newV, score = self.next_state(move, H, V)
                #print move, score
                if(depth-1 == 0 or self.game_ends(newH, newV)):
                    possiWorth = score#self.evaluate(H,V,move)
                
                else:
                    idea, possiWorth = self.minimax(newH, newV, depth-1, False)
                scoring = possiWorth + score
                if(scoring >= worth):
                    worth = scoring
                    goodChoice = move

        else:
            worth = 36
            movelist = self.list_possible_moves(H,V)
            for move in movelist:
                newH, newV, score = self.next_state(move, H, V)
                #print move, score
                if(depth-1 == 0 or self.game_ends(newH, newV)):
                    possiWorth = score#self.evaluate(H,V,move)
                
                else:
                    idea, possiWorth = self.minimax(newH, newV, depth-1, True)
                #scoring = score - possiWorth
                scoring = self.score_player2 - score
                if(scoring <= worth):
                    worth = scoring
                    goodChoice = move
        
        #below gives a valid, okay default value if nothing was found
        if (goodChoice == [-1,-1,-1]):

            temp_h = H
            temp_v = V
            next_move=self.list_possible_moves(temp_h,temp_v);
            best_move=next_move[0];
            best_score=worth;
        
            for move in next_move:
            
                temp_h,temp_v,score=self.next_state(move,temp_h,temp_v);
                
                if(score>best_score):
                    best_score=score;
                    best_move=move;

            goodChoice = best_move

        return goodChoice, worth; 
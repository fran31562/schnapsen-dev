import random
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Score, Hand
from schnapsen.deck import Suit, Card, Rank
from typing import Optional

class BullyBot(Bot):

    def __init__(self, seed: int) -> None:
        self.seed = seed


    def get_move(self,
                 state: PlayerPerspective,
                 leader_move: Optional[Move]) -> Move:

        moves: list[Move] = state.valid_moves()
        scorer = SchnapsenTrickScorer()

        trumpCardsMove=[]
        opponentSuitMove=[]
        max_score = 2


        for move in moves:
            if move.cards[0].suit == state.get_trump_suit():
                trumpCardsMove.append(move)
        if len(trumpCardsMove) > 0:
            return random.choice(trumpCardsMove)


        elif state.am_i_leader() == False:
            for move in moves:
                if move.cards[0].suit == leader_move.cards[0].suit:
                    opponentSuitMove.append(move)
            if len(opponentSuitMove) > 0:
                return random.choice(opponentSuitMove)


            else:
                for move in moves:
                    if scorer.rank_to_points(move.cards[0].rank) > max_score:
                        max_score = scorer.rank_to_points(move.cards[0].rank)
                        my_move = move
                return my_move
















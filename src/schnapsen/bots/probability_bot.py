import random
from abc import ABC
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer


class ProbabilityBot(Bot, ABC):
    def __init__(self) -> None:
        super().__init__()

    def get_move(self,
                 state: PlayerPerspective,
                 leader_move: Optional[Move]) -> Move:

        moves: list[Move] = state.valid_moves()
        scorer = SchnapsenTrickScorer()

        trumpCardsMove = []
        opponentSuitMove = []
        max_score = 2


#PlayerPerspective get_talon_size -> Finds amount of cards still in talon
#PlayerPerspective get_won_cards
#PlayerPerspective get_opponent_won_cards
#PP get_known_cards_of_opponents_hand
#PP seen_cards -> all cards that have been seen by the bot

'''
Probability Bot


Stock open:
	We are following:
		Try to use a non-trump trick to win
		If opponent played a non-trump Ace or 10, use a trump card
		If there is no option, try to play a trump card
		if no card in hand can beat what opponent has played, discard lowest value card

	We are leading:
		Is there a possible trump exchange? Yes do it
		Calculate probabilities for each card
		Calculate probabilities for trump cards
		
		

Elif stock closed:
	We are following:
		xxx

	We are leading:
		xxx


'''


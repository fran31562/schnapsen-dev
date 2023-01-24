import random
from abc import ABC
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, GameState, GamePhase


class ProbabilityBot(Bot, ABC):
    def __init__(self) -> None:
        super().__init__()

    def get_move(self,
                 state: PlayerPerspective,
                 leader_move: Optional[Move]) -> Move:

        moves: list[Move] = state.valid_moves()
        my_move: Move = moves[0]
        scorer = SchnapsenTrickScorer()

        trumpCardsMove = []
        opponentSuitMove = []
        max_score = 2

        if GameState.game_phase() == GamePhase.ONE:
            if not PlayerPerspective.am_i_leader():

            else:

        if GameState.game_phase() == GamePhase.TWO:
            if not PlayerPerspective.am_i_leader():
                current_trump = state.get_trump_suit()
                valid_moves = []
                trump_moves = []
                for x in moves:
                    if x.cards[0].suit == current_trump:
                        trump_moves.append(x)
                if len(trump_moves) > 0:
                    ace_trump = trump_moves.filter_rank('ACE')
                    ten_trump = trump_moves.filer_rank('TEN')
                    king_trump = trump_moves.filter_rank('KING')
                    queen_trump = trump_moves.filter_rank('QUEEN')
                    jack_trump = trump_moves.filter_rank('JACK')
                    if ace_trump > 0:
                        my_move = ace_trump[0]
                    elif ten_trump > 0:
                        my_move = ten_trump[0]
                    elif king_trump > 0:
                        my_move = ten_trump[0]
                    elif queen_trump > 0:
                        my_move = queen_trump[0]
                    elif jack_trump > 0:
                        my_move = jack_trump[0]
                return my_move

            else:
                current_trump = state.get_trump_suit()
                for x in moves:
                    if x.cards[0].suit == current_trump:
                        my_move = x
                    return my_move


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
		lowest ranked card that can win
		or trump card
		if cant win, play lowest rank card.

	We are leading:
		


'''


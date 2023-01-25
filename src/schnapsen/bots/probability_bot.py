import random
from abc import ABC
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, GameState, GamePhase, Hand, Talon, Card


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
        valid_moves = []
        max_score = 2

        if GameState.game_phase() == GamePhase.ONE:
            if not PlayerPerspective.am_i_leader():
                #use non-trump trick to win

                #If player uses a non-trump ace or 10, use a trump card
                #If no option, play a trump card
                #If no card in hand can beat opponent, discard card of least value

            #This is for when we are following not leading
            else:
                trump_suit = state.get_trump_suit()
                trump_card = state.get_trump_card()
                cards_in_hand = state.get_hand()
                talon_size = state.get_talon_size()

                opponent_hand = state.get_known_cards_of_opponent_hand()
                opponent_won_cards = state.get_opponent_won_cards()
                my_won_cards = state.get_won_cards()
                seen_cards = state.seen_cards()

                for move in moves:
                    if move.cards[0].suit == trump_suit:
                        trumpCardsMove.append(move)

                # Is there a possible trump exchange, if yes do it
                if not trump_card.rank == "JACK":
                    for move in trumpCardsMove:
                        if move.cards[0].rank == "JACK":
                            Talon.trump_exchange(move)

                probability_dictionary: dict = {
                "TEN_OF_HEARTS" : [0, Card.TEN_HEARTS, 10],
                "JACK_OF_HEARTS" : [0, Card.JACK_HEARTS, 2],
                "QUEEN_OF_HEARTS" : [0, Card.QUEEN_HEARTS, 3],
                "KING_OF_HEARTS" : [0, Card.KING_HEARTS, 4],
                "ACE_OF_HEARTS" : [0, Card.ACE_HEARTS, 11],

                "TEN_OF_SPADES": [0, Card.TEN_SPADES, 10],
                "JACK_OF_SPADES": [0, Card.JACK_SPADES, 2],
                "QUEEN_OF_SPADES": [0, Card.QUEEN_SPADES, 3],
                "KING_OF_SPADES": [0, Card.KING_SPADES, 4],
                "ACE_OF_SPADES": [0, Card.ACE_SPADES, 11],

                "TEN_OF_CLUBS": [0, Card.TEN_CLUBS, 10],
                "JACK_OF_CLUBS": [0, Card.JACK_CLUBS, 2],
                "QUEEN_OF_CLUBS": [0, Card.QUEEN_CLUBS, 3],
                "KING_OF_CLUBS": [0, Card.KING_CLUBS, 4],
                "ACE_OF_CLUBS": [0, Card.ACE_CLUBS, 11],

                "TEN_OF_DIAMONDS": [0, Card.TEN_DIAMONDS, 10],
                "JACK_OF_DIAMONDS": [0, Card.JACK_DIAMONDS, 2],
                "QUEEN_OF_DIAMONDS": [0, Card.QUEEN_DIAMONDS, 3],
                "KING_OF_DIAMONDS": [0, Card.KING_DIAMONDS, 4],
                "ACE_OF_DIAMONDS": [0, Card.ACE_DIAMONDS, 11]
                }

                for card in probability_dictionary:
                    if probability_dictionary[card][1] not in seen_cards:
                        temp = 5 + talon_size
                        temp2 = 1 / temp
                        probability_dictionary[card][0] = temp2 * 100

                    if probability_dictionary[card][1] in opponent_hand:
                        probability_dictionary[card][0] = 100

                for card in cards_in_hand:
                    rank = card.rank()
                    value = 0
                    suit = card.suit()
                    points = 0
                    if rank == "TEN":
                        value = 10
                    elif rank == "JACK":
                        value = 2
                    elif rank == "QUEEN":
                        value = 3
                    elif rank == "KING":
                        value = 4
                    elif rank == "ACE":
                        value = 11
                    templist = []
                    for x in probability_dictionary:
                        if x






                #Calculate the probabilities of each card


                #Calculate the probabilities the opponent has a trump card

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


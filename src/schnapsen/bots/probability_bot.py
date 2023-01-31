import random
from abc import ABC
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, SchnapsenTrickImplementer, GameState, GamePhase, Hand, Talon, Card


class ProbabilityBot(Bot, ABC):
    def __init__(self) -> None:
        self.talon = Talon
        self.state = GameState
        super().__init__()

    def get_move(self,
                 state: PlayerPerspective,
                 leader_move: Optional[Move]) -> Move:
        moves: list[Move] = state.valid_moves()
        my_move: Move = moves[0]
        scorer = SchnapsenTrickScorer()

        trumpCardsMove = []
        max_score = 2

# ----------------------------------------------------- #
# GAME PHASE 1 #
# ----------------------------------------------------- #

        if state.get_phase == GamePhase.ONE:
            if not state.am_i_leader():
                # Get the card that was just played by the opponent
                opp_played_card = SchnapsenTrickImplementer.get_leader_move()

                # The card value of the opponent played card will be stored in the below variable
                card_value = 0

                # Get the trump suit of the game
                trump_suit = state.get_trump_suit()

                # The list of the best trump moves to select from
                best_moves_trump = []

                # The list of the best moves that are not trump
                best_moves_non_trump = []

                # Analyze the card rank of the opponents played card and give it the appropriate value
                if opp_played_card.rank == "TEN":
                    card_value = 10
                elif opp_played_card.rank == "JACK":
                    card_value = 2
                elif opp_played_card.rank == "QUEEN":
                    card_value = 3
                elif opp_played_card.rank == "KING":
                    card_value = 4
                elif opp_played_card.rank == "ACE":
                    card_value = 11

                # If the card played by the opponent is a trump suit card
                if opp_played_card.suit == trump_suit:

                    # Loop through all valid moves
                    for move in moves:

                        # The move value for each move in the bots hand
                        move_value = 0

                        # Assign the appropriate value for the move depending on the rank
                        if move.rank == "JACK":
                            move_value = 2
                        elif move.rank == "QUEEN":
                            move_value = 3
                        elif move.rank == "KING":
                            move_value = 4
                        elif move.rank == "TEN":
                            move_value = 10
                        elif move.rank == "ACE":
                            move_value = 11

                        # If the current move is a trump suit card, and has a greater value than the
                        # card played by the opponent, add it to the best_moves list
                        if move.suit == trump_suit:
                            if move_value > card_value:
                                best_moves_trump.append(move)

                        # If the current move is not a trump suit card, add it to the best_moves_non_trump list
                        # along with its value
                        elif not move.suit == trump_suit:
                            temp: list = [move, move_value]
                            best_moves_non_trump.append(temp)

                    # If we have a card that can beat the trump card played by the opponent, play it
                    if len(best_moves_trump) > 0:
                        my_move = best_moves_trump[0]

                    # If we have no trump card that can beat the opponents played card, discard of a card of low value
                    elif len(best_moves_trump) == 0:
                        temp = 12
                        for x in best_moves_non_trump:
                            if x[1] < temp:
                                temp = x[1]
                                my_move = x[0]

                # If the opponent plays a non trump card
                elif not opp_played_card.suit == trump_suit:

                    # If the opponent plays a non-trump ace or 10, use at trump card to beat it
                    if card_value == 11 or card_value == 10:
                        for move in moves:
                            if move.suit == trump_suit:
                                best_moves_trump.append(move)

                        if len(best_moves_trump) > 0:
                            my_move = best_moves_trump[0]

                        elif len(best_moves_trump) == 0:
                            for move in moves:
                                # The move value for each move in the bots hand
                                move_value = 0

                                # Assign the appropriate value for the move depending on the rank
                                if move.rank == "JACK":
                                    move_value = 2
                                elif move.rank == "QUEEN":
                                    move_value = 3
                                elif move.rank == "KING":
                                    move_value = 4
                                elif move.rank == "TEN":
                                    move_value = 10
                                elif move.rank == "ACE":
                                    move_value = 11

                                # If we have a card that can beat the opponents card, add it to the list
                                if move_value >= card_value:
                                    best_moves_non_trump.append(move)

                            # If we do have a card that can beat the opponents card, play it
                            if len(best_moves_non_trump) > 0:
                                my_move = best_moves_non_trump[0]

                            # If we do not have a card that can beat the opponents card, dispose of a low value card
                            elif len(best_moves_non_trump) == 0:
                                temp: list = []
                                for move in moves:
                                    # The move value for each move in the bots hand
                                    move_value = 0

                                    # Assign the appropriate value for the move depending on the rank
                                    if move.rank == "JACK":
                                        move_value = 2
                                    elif move.rank == "QUEEN":
                                        move_value = 3
                                    elif move.rank == "KING":
                                        move_value = 4
                                    elif move.rank == "TEN":
                                        move_value = 10
                                    elif move.rank == "ACE":
                                        move_value = 11

                                    temp2: list = [move, move_value]
                                    temp.append(temp2)

                                for move in temp:
                                    temp3 = 12
                                    if move[1] < temp3:
                                        temp3 = move[1]
                                        my_move = move

                    else:
                        for move in moves:
                            move_value = 0

                            # Assign the appropriate value for the move depending on the rank
                            if move.rank == "JACK":
                                move_value = 2
                            elif move.rank == "QUEEN":
                                move_value = 3
                            elif move.rank == "KING":
                                move_value = 4
                            elif move.rank == "TEN":
                                move_value = 10
                            elif move.rank == "ACE":
                                move_value = 11

                            if move_value > card_value and move.suit != trump_suit:
                                temp2 = [move, move_value]
                                best_moves_non_trump.append(temp2)
                            elif move_value > card_value and move.suit == trump_suit:
                                temp2 = [move, move_value]
                                best_moves_trump.append(temp2)

                        if len(best_moves_non_trump) > 0:
                            for move in best_moves_non_trump:
                                temp3 = 12
                                if move[1] < temp3:
                                    temp3 = move[1]
                                    my_move = move

                        elif len(best_moves_non_trump) == 0:
                            if len(best_moves_trump) > 0:
                                my_move = best_moves_trump[0]

                            else:
                                my_move = random.choice(moves)

            else:
                trump_suit = state.get_trump_suit()
                trump_card = state.get_trump_card()
                cards_in_hand = list(state.get_hand())
                talon_size = state.get_talon_size()

                opponent_hand = state.get_known_cards_of_opponent_hand()
                seen_cards = list(state.seen_cards(leader_move))

                for move in moves:
                    if move.cards[0].suit == trump_suit:
                        trumpCardsMove.append(move)

                # Is there a possible trump exchange, if yes do it
                if not trump_card.rank == "JACK":
                    for move in trumpCardsMove:
                        if move.rank == "JACK":
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
                        probability_dictionary[card][0] = temp2

                    if probability_dictionary[card][1] in opponent_hand:
                        probability_dictionary[card][0] = 1

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
                        if probability_dictionary[x][2] >= value:
                            templist.append(probability_dictionary[x])

                        if card.suit(probability_dictionary[x][1]) == trump_suit:
                            templist.append(probability_dictionary[x])

                    total: float = 0
                    total_probability_dict: dict = {}
                    for x in templist:
                        total += x[0]
                        total_probability_dict[card] = total

                best_move = {"prob": 0, "card": ""}
                for move in total_probability_dict:
                    if total_probability_dict[move] < best_move["prob"]:
                        best_move["prob"] = total_probability_dict[move]
                        best_move["card"] = move
                my_move = best_move["card"]


# ----------------------------------------------------- #
# GAME PHASE 2 #
# ----------------------------------------------------- #

        if state.get_phase == GamePhase.TWO:
            if not PlayerPerspective.am_i_leader():
                current_trump = state.get_trump_suit()
                valid_moves = []
                trump_moves = []
                ace_normal = moves.filter_rank('ACE')
                ten_normal = moves.filter_rank('TEN')
                king_normal = moves.filter_rank("KING")
                queen_normal = moves.filter_rank('QUEEN')
                jack_normal = moves.filter_rank('JACK')
                for x in moves:
                    if x.cards[0].suit == current_trump:
                        trump_moves.append(x)
                if len(trump_moves) > 0:
                    ace_trump = trump_moves.filter_rank('ACE')
                    ten_trump = trump_moves.filer_rank('TEN')
                    king_trump = trump_moves.filter_rank('KING')
                    queen_trump = trump_moves.filter_rank('QUEEN')
                    jack_trump = trump_moves.filter_rank('JACK')
                    if len(ace_trump) > 0:
                        my_move = ace_trump[0]
                    elif len(ten_trump) > 0:
                        my_move = ten_trump[0]
                    elif len(king_trump) > 0:
                        my_move = ten_trump[0]
                    elif len(queen_trump) > 0:
                        my_move = queen_trump[0]
                    elif len(jack_trump) > 0:
                        my_move = jack_trump[0]
                elif len(ace_normal) > 0:
                    my_move = ace_normal[0]
                elif len(ten_normal) > 0:
                    my_move = ten_normal[0]
                elif len(king_normal) > 0:
                    my_move = king_normal[0]
                elif len(queen_normal) > 0:
                    my_move = queen_normal[0]
                elif len(jack_normal) > 0:
                    my_move = jack_normal[0]


            else:
                ace_normal = moves.filter_rank('ACE')
                ten_normal = moves.filter_rank('TEN')
                king_normal = moves.filter_rank("KING")
                queen_normal = moves.filter_rank('QUEEN')
                jack_normal = moves.filter_rank('JACK')
                current_trump = state.get_trump_suit()
                for x in moves:
                    if x.cards[0].suit == current_trump:
                        my_move = x
                    elif len(ace_normal) > 0:
                        my_move = ace_normal[0]
                    elif len(ten_normal) > 0:
                        my_move = ten_normal[0]
                    elif len(king_normal) > 0:
                        my_move = king_normal[0]
                    elif len(queen_normal) > 0:
                        my_move = queen_normal[0]
                    elif len(jack_normal) > 0:
                        my_move = jack_normal[0]
        return my_move



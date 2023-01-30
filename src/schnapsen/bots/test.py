import random
from abc import ABC
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, SchnapsenTrickImplementer, GameState, GamePhase, Hand, Talon, Card

class TestBot(Bot):

    def __init__(self) -> None:

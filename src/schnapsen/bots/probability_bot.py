import random
from abc import ABC
from typing import Optional
from schnapsen.game import Bot, PlayerPerspective, Move


class ProbabilityBot(Bot):
    def __init__(self) -> None:
        super().__init__()



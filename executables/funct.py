import random
from abc import ABC
from typing import Optional

from schnapsen.bots.probability_bot import ProbabilityBot
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, SchnapsenTrickImplementer, GameState, \
    GamePhase, Hand, Talon, Card, Bot, GamePlayEngine, SchnapsenGamePlayEngine
from schnapsen.bots import probability_bot, rand, rdeep, bully
from executables.cli import play_games_and_return_stats
from schnapsen.bots.rand import RandBot


play_games_and_return_stats(SchnapsenGamePlayEngine(), ProbabilityBot(), RandBot(1212121), 1000)
import random
from schnapsen.bots import SchnapsenServer
from schnapsen.bots import RandBot, AlphaBetaBot, RdeepBot, BullyBot
from schnapsen.bots.probability_bot import ProbabilityBot
from schnapsen.game import SchnapsenGamePlayEngine, Bot
import click


@click.command()
@click.option('--bot', '-b',
              type=click.Choice(['BullyBot', 'AlphaBetaBot', 'RdeepBot', 'MLDataBot', 'MLPlayingBot', 'RandBot', 'ProbabilityBot'], case_sensitive=False),
              default='RandBot', help="The bot you want to play against.")
def main(bot: str) -> None:
    """Run the GUI."""
    engine = SchnapsenGamePlayEngine()
    bot1: Bot
    with SchnapsenServer() as s:
        if bot.lower() == "randbot":
            bot1 = RandBot(12)
        elif bot.lower() in ["alphabeta", "alphabetabot"]:
            bot1 = AlphaBetaBot()
        elif bot.lower() == "rdeepbot":
            bot1 = RdeepBot(num_samples=16, depth=4, rand=random.Random(42))
        elif bot.lower() == "bullybot":
            bot1 = BullyBot(12)
        elif bot.lower() == "probabilitybot":
            bot1 = ProbabilityBot()
        else:
            raise NotImplementedError
        bot2 = s.make_gui_bot(name="mybot2")
    #    bot1 = s.make_gui_bot(name="mybot1")
        engine.play_game(bot1, bot2, random.Random(100))


if __name__ == "__main__":
    main()

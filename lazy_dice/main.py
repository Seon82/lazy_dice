import os

import hikari
from dotenv import load_dotenv

from lazy_dice.engine import Engine
from lazy_dice.formatter import format_engine
from lazy_dice.parser import parse

load_dotenv()

bot = hikari.GatewayBot(intents=hikari.Intents.GUILD_MESSAGES, token=os.environ["BOT_TOKEN"])
command_prefix = os.getenv("COMMAND_PREFIX", "!")


@bot.listen()
async def roll(event: hikari.GuildMessageCreateEvent) -> None:
    # Check for empty and bot messages
    msg = event.content
    if event.is_bot or not msg:
        return

    # Check for command and strip leading command symbol
    if msg.startswith(2 * command_prefix):
        msg = msg[2:]
        one_step = False
    elif msg.startswith(command_prefix):
        msg = msg[1:]
        one_step = True
    else:
        return

    # Core
    dice = parse(msg)
    if not dice:
        return
    engine = Engine(dice=dice)
    if one_step:
        engine.step()
    else:
        engine.step_until_done()

    # Respond
    await event.message.respond(format_engine(engine))


bot.run()

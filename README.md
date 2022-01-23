# LazyDice
[![Linter Actions Status](https://github.com/Seon82/lazy_dice/actions/workflows/black.yml/badge.svg?branch=master)](https://github.com/Seon82/lazy_dice/actions)
[![Linter Actions Status](https://github.com/Seon82/lazy_dice/actions/workflows/mypy.yml/badge.svg?branch=master)](https://github.com/Seon82/lazy_dice/actions)

A discord bot with support for [Savage Worlds](https://peginc.com/savage-settings/savage-worlds/) dice parsing.

## Installation
### With docker (recommended)
* Install [docker](https://docs.docker.com/get-docker/).
* Clone the repository: `git clone https://github.com/Seon82/lazy_dice`.
* Build the image: `docker build -t lazy_dice:latest .`
* Get a bot token (guide [here]((https://discordpy.readthedocs.io/en/stable/discord.html)).
* Run the image: `docker run lazy_dice -e BOT_TOKEN={YOUR_TOKEN} -e COMMAND_PREFIX={YOUR_PREFIX}`.

### Manually
* Install [python3](https://www.python.org/).
* Clone the repository: `git clone https://github.com/Seon82/lazy_dice`.
* Install the package: `python3 -m pip install lazy_dice`.
* Rename `.env.dist` to `.env`, and fill in the bot token (guide [here]((https://discordpy.readthedocs.io/en/stable/discord.html)) and command prefix.
* Run the bot from the repo's root: `python3 lazy_dice/main.py`.

## Contributing
Contributions are welcome! This project uses [poetry](https://github.com/python-poetry/poetry) for dependency management.
Please run your code against [black](https://github.com/psf/black) and [mypy](https://mypy.readthedocs.io/en/stable/) before opening a PR.
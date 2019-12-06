# uwubot

uwu bot is a fun discord bot with the intent of making cute comments and spreading culture. The bot translates any previous comment into uwu language. 
It was originally created by kawaiiCirno (https://github.com/kawaiiCirno).

## Installation

1. Python 3 and `discord.py` library is required to run uwubot. You can install it by executing the following line in your Command Line/Terminal:

```bash
python3 -m pip install -U discord.py
```

2. Replace the `TOKEN` variable in `uwubot.py` with your bot token (read the link below to get your own token).

3. Start the main Python script by doing:
```bash
python3 uwubot.py
```

## Commands
`!uwuhelp` - Lists all commands

`!uwu` - Uwufies the newest message in a text channel

`!uwuall` - Uwufies ALL incoming messages

`!uwustop` - Stops uwufying all incoming messages

## Deploying
In order to put this in your Discord server, you will have to run the `uwubot.py` Python script in a local machine first.
I ran this in a Raspberry Pi 4B so that it was always active.
Please follow the steps here to get your bot set up: https://discordpy.readthedocs.io/en/latest/discord.html.

I run this program on a Raspberry Pi and run it in the background indefinitely by doing the following command in the Linux shell (make sure that the path is adjusted for your scenario):
```nohup python3 -u /home/pi/Desktop/uwubot/uwubot.py &```

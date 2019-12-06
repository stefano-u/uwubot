import discord
from uwulater import uwulate
from discord.ext import commands

# REPLACE WITH OWN TOKEN
TOKEN = 'NjUwMzI0NDczODM2NDcwMjgy.XeLpgQ.5mdhqIEhs-kPt7H6NvymyhTpM2c'

bot = commands.Bot(command_prefix="!")
client = discord.Client()
is_uwu = False

# Command for !uwu
@bot.command()
async def uwu(ctx):
    print("Command: !uwu")

    # Embed message to be displayed
    embed_message = discord.Embed(
        colour=discord.Colour.blue()
    )

    # Get last message in the channel (as Message object, not string)
    selected_msg = None

    # Last 100 messages
    message_list = await ctx.history(limit=100).flatten()

    # Cycles through the list of newest 100 messages
    for message in message_list:
        if message.author.name != "uwubot" and not message.content.startswith("!uwu"):
            selected_msg = message

            # Gets the contents of the message
            embed_message.description = uwulate(message.content)

            # Get the username + avatar picture of the person who sent that message
            embed_message.set_author(name=selected_msg.author.display_name,
                                     icon_url=selected_msg.author.avatar_url)

            break

    if selected_msg == None:
        embed_message.description = "Sowwy, can't find any valid text!"

    # Display embed message
    await ctx.channel.send(embed=embed_message)


# Command for !uwuhelp
@bot.command()
async def uwuhelp(ctx):
    print("Command: !uwuhelp")
    description = ("```----------!uwuhelp----------```\n"
                   "Uwufy previous message with: \n```!uwu```\n"
                   "Uwufy ALL messages with:\n```!uwuall```\n"
                   "Stop uwufying all messages with ```!uwustop```\n"
                   "Originally created by kawaiiCirno (https://github.com/kawaiiCirno/uwubot)\n"
                   "Modified by stefano-u (https://github.com/stefano-u/uwubot)")
    embed_message = discord.Embed(
        colour=discord.Colour.blue(),
        description=description
    )
    await ctx.channel.send(embed=embed_message)

# Command for !uwuall
@bot.command()
async def uwuall(ctx):
    print("Command: !uwuall")
    global is_uwu
    if not is_uwu:
        embed_message = discord.Embed(
            colour=discord.Colour.blue(),
            description="Uwufying ALL messages! Use `!uwuall` to disable. `ԅ(≖⌣≖ԅ)`"
        )
        await ctx.channel.send(embed=embed_message)
        is_uwu = True

# Command for !uwustop
@bot.command()
async def uwustop(ctx):
    print("Command: !uwustop")
    global is_uwu
    if is_uwu:
        embed_message = discord.Embed(
            colour=discord.Colour.blue(),
            description="No longer uwufying all messages! `ಠ╭╮ಠ`"
        )
        await ctx.channel.send(embed=embed_message)
        is_uwu = False

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    global is_uwu

    if is_uwu and message.author.name != "uwubot":
        # Embed message to be displayed
        embed_message = discord.Embed(
            colour=discord.Colour.blue()
        )

        # Get last message in the channel (as Message object, not string)
        selected_msg = None

        # Last 100 messages
        message_list = await message.channel.history(limit=100).flatten()

        # Cycles through the list of newest 100 messages
        for message in message_list:
            if message.author.name != "uwubot" and not message.content.startswith("!uwu"):
                selected_msg = message

                # Gets the contents of the message
                embed_message.description = uwulate(message.content)

                # Get the username + avatar picture of the person who sent that message
                embed_message.set_author(name=selected_msg.author.display_name,
                                            icon_url=selected_msg.author.avatar_url)

                break

        if selected_msg == None:
            embed_message.description = "Sowwy, can't find any valid text!"

        # Display embed message
        await message.channel.send(embed=embed_message)
        is_uwu2 = False



@bot.event
async def on_ready():
    activity = discord.Activity(
        name=' - !uwuhelp', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    print('uwubot starting!')

bot.run(TOKEN)

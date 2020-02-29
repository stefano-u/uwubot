import discord
from uwulater import uwulate
from discord.ext import commands

# REPLACE WITH OWN TOKEN
TOKEN = ""

bot = commands.Bot(command_prefix="!uwu ")
bot.remove_command("help")
is_uwu = False
delete_message = False
bot.embed_color = discord.Colour.blue()

# Takes in a message, outputs a uwufyied(?) version of it
async def send_uwuify(message : commands.Context):
    embed_message = discord.Embed(
        colour=message.author.color
    )

    # Gets the contents of the message
    embed_message.description = uwulate(message.content)

    # Get the username + avatar picture of the person who sent that message
    embed_message.set_author(name=message.author.display_name,
                             icon_url=message.author.avatar_url)

    # Display embed message
    await message.channel.send(embed=embed_message)

# Command for !uwu
@bot.command()
async def uwuify(ctx : commands.Context):
    print("Command: !uwu uwuify")

    # Last 5 messages
    message_list = await ctx.history(limit=5).flatten()

    # Cycles through the list of newest 5 messages
    for message in message_list:
        if message.author != bot.user and not message.content.startswith(bot.command_prefix):
            await send_uwuify(message)
            return

    embed_message.description = "Sowwy, can't find any valid text!"

# Command for !uwuhelp
@bot.command()
async def help(ctx : commands.Context):
    print("Command: !uwuhelp")
    description = ("```----------!uwuhelp----------```\n"
                   "Uwufy previous message with: \n```!uwu uwuify```\n"
                   "Uwufy ALL messages with (Toggle off with same command):\n```!uwu all```\n"
                   "Originally created by kawaiiCirno (https://github.com/kawaiiCirno/uwubot)\n"
                   "Modified by stefano-u (https://github.com/stefano-u/uwubot)\n"
                   "Further modified by Znunu (https://github.com/Znunu/uwubot)")
    embed_message = discord.Embed(
        colour=bot.embed_color,
        description=description
    )
    await ctx.channel.send(embed=embed_message)

# Command for !uwuall
@bot.command()
async def all(ctx : commands.Context, to_delete : str = None):
    global is_uwu
    global delete_message

    # Toggle on
    if not is_uwu:
        print("Command: !uwu all toggled on")
        embed_message = discord.Embed(
            colour=bot.embed_color,
            description="Uwufying ALL messages! Use `!uwu all` to toggle off. `ԅ(≖⌣≖ԅ)`"
        )
        await ctx.channel.send(embed=embed_message)
        is_uwu = True
        if to_delete == "delete":
            delete_message = True
    # Toggle off
    else:
        print("Command: !uwu all toggled off")
        embed_message = discord.Embed(
            colour=bot.embed_color,
            description="No longer uwufying all messages! `ಠ╭╮ಠ`"
        )
        await ctx.channel.send(embed=embed_message)
        is_uwu = False
        delete_message = False

@bot.event
async def on_message(message : discord.message):
    global is_uwu

    #It's a command, send for processing:
    if message.content[:len(bot.command_prefix)] == bot.command_prefix and message.author != bot.user:
        await bot.process_commands(message)
    #uwuify all is on, uwuify the message
    elif is_uwu and message.author != bot.user:
        await send_uwuify(message)
        #Delete message is on, delete the message
        if delete_message:
            await message.delete()

@bot.event
async def on_ready():
    activity = discord.Activity(
        name=f" - {bot.command_prefix} help", type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    print("uwubot starting!")

if __name__ == "__main__":
    bot.run(TOKEN)

import discord
from uwulater import uwulate
from discord.ext import commands

# REPLACE WITH OWN TOKEN
TOKEN = 'NjUwMzI0NDczODM2NDcwMjgy.XeJxQg.lQvg1LNXJ0pRrem9q2NF7kTvIoI'

client = commands.Bot(command_prefix="!")

# Command for !uwu
@client.command()
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
    # print(len(message_list))

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
@client.command()
async def uwuhelp(ctx):
    print("Command: !uwuhelp")

    description = ("```----------!uwuhelp----------```\n"
                   "Uwufy pwevious messages with\n```"
                   "!uwu```\nUwufy aww messages with\n"
                   "```!uwufy```\n"
                   "and tuwn off with\n```!nouwu```\n"
                   "Originally created by kawaiiCirno (https://github.com/kawaiiCirno/uwubot)\n"
                   "Modified by Stefano Gregor Unlayao (https://github.com/stefano-u/uwubot)")

    embed_message = discord.Embed(
        colour=discord.Colour.blue(),
        description=description
    )

    await ctx.channel.send(embed=embed_message)

# @client.event
# async def on_message(message):
#     global prev_msg
#     global is_uwu

#     # Get the username of the person that sent the message
#     embed_message.set_author(name=message.author.display_name,
#                              icon_url=message.author.avatar_url)

#     # Gets the text channel
#     current_text_channel = message.channel


#     if message.author == client.user:
#         return
#     ##Help
#     if message.content.startswith('!helpuwu'):
#         embed_message.description = help_message
#         await message.channel.send(embed=embed_message)
#     #Well discord doesn't support this okay
#     #Disable uwufy mode

#     elif message.content.startswith('!nouwu'):
#         is_uwu[hash(message.guild)] = False
#         embed_message.description = "Disabling uwufy mode!"
#         await message.channel.send(embed=embed_message)

#     if message.content.startswith('!uwufy'):
#         is_uwu[hash(message.guild)] = True
#         embed_message.description = 'Uwufying all messages! Use !nouwu to disable pls dont ( ; ω ; )'
#         await message.channel.send(embed=embed_message)

#     #Check uwu mode
#     elif hash(message.guild) in is_uwu and is_uwu[hash(message.guild)]:
#         #await message.edit(content = uwulate(message.content))
#         # await message.delete()
#         channel_last_msg = current_text_channel.last_message.content
#         embed_message.description = uwulate(channel_last_msg)
#         await message.channel.send(embed=embed_message)

#     #Uwufy previous message
#     elif message.content.startswith('!uwu'):
#         async for text in current_text_channel.history(limit=100):
#             if text.author != "uwubot":
#                 embed_message.description = uwulate(text)
#                 # await message.channel.send(embed=embed_message)
#                 print(embed_message.description)
#             else:
#                 print(f"No: " + text)


#         # if hash(message.guild) not in prev_msg:
#         #     embed_message.description = 'Sowwy, nyothing to uwufy uwu!'
#         #     await message.channel.send(embed=embed_message)
#         # else:
#         #     uwu_message = uwulate(prev_msg[hash(message.guild)])
#         #     # channel_last_msg = current_text_channel.last_message.content
#         #     # embed_message.description = uwulate(channel_last_msg)
#         #     embed_message.description = uwu_message
#         #     await message.channel.send(embed=embed_message)
#     # else:
#     #     prev_msg[hash(message.guild)] = message.content


@client.event
async def on_ready():
    activity = discord.Activity(
        name='you !uwuhelp', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print('uwubot starting!')

client.run(TOKEN)

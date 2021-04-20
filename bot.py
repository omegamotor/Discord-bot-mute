import discord
from discord.ext import commands
import keyboard
import json

prefix = "$"
bot = commands.Bot(command_prefix=prefix)

with open("data.txt") as json_file:
    data = json.load(json_file)
    for p in data['config']:
        TOKEN = p['TOKEN']
        idMainChannel = int(p['idMainChannel'])
        idSilentChannel = int(p['idSilentChannel'])
        muteButton = p['muteButton']
        unMuteButton = p['unMuteButton']

@bot.event
async def on_ready():
    print("Bot jest gotowy.")
    await bot.change_presence(activity=discord.Game(name=f"Tłumie zagrożenia"))


@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def m(ctx, member: discord.Member):
    while True:
        if keyboard.is_pressed(muteButton):
            await member.move_to(ctx.guild.get_channel(idSilentChannel))

        elif keyboard.is_pressed(unMuteButton):
            await member.move_to(ctx.guild.get_channel(idMainChannel))

        elif keyboard.is_pressed('-'):
            print('bot przestał wyciszać gracza')
            break


bot.run(TOKEN)



import discord
from discord.ext.commands import Bot,when_mentioned
from discord import Intents,Embed
import os

BOT_TOKEN = 'MTI3MTc3MzgxMTQ4MTY0MTAyMg.Ggkcbg.ddbUiKwZsOJPROq4olZlOzIOXm9x1OTjrYvAjE'

intents = Intents()
intents.members = True
intents.guilds = True

bot = Bot(when_mentioned,intents=intents)

@bot.event
async def on_member_join(member:discord.member.Member):
    embed = Embed(colour=0x70ff8f,title=f'새로운 유저가 PIXEL에 접속하셨어요!',description=f'{member.display_name}이(가) PIXEL의 {member.guild.member_count}번째 유저가 되셨습니다!')
    await member.guild.get_channel(1271773665893027901).send(embed=embed)

acces_token = os.environ["BOT_TOKEN"]
bot.run(BOT_TOKEN)

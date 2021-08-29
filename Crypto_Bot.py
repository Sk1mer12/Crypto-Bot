import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix = "!", case_insensitive = True)
BOT_TOKEN = "ODgxMjYxMzYzMjQxMDQxOTUy.YSqQmg.FYoFVN_LW3H70QakS-8U3j-KrL4"
final = 0

@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.command(name="prices")
async def preços(ctx):
    def getCrypto(crypto):
        
        URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur"
        res = requests.get(URL)
        data = res.json()
        for i in range(len(data)):
            if data[i]['id'] == crypto:
                j = format(data[i]['current_price'], '.9f')
                d = data[i]['id'].upper()
                f = data[i]['price_change_percentage_24h']
                print('\n' ,d, ' => ' ,j,'€', ' | ', f, '%')
                final ="```" + d + '  =>  ' + j + '€' + "```"
                return final
    
    aman = getCrypto('bitcoin')
    await ctx.send(aman)
    aman = getCrypto('ethereum')
    await ctx.send(aman)
    aman = getCrypto('cardano')
    await ctx.send(aman)
    aman = getCrypto('binancecoin')
    await ctx.send(aman)
    aman = getCrypto('dogecoin')
    await ctx.send(aman)
    aman = getCrypto('shiba-inu')
    await ctx.send(aman)
    aman = getCrypto('litecoin')
    await ctx.send(aman)
    aman = getCrypto('solana')
    await ctx.send(aman)

    
bot.run(BOT_TOKEN)

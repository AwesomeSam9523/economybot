import discord
import asyncio
from utils import *
import datetime

bot: EconomyBot = None

class Bank(discord.cog.Cog):
    def __init__(self):
        super().__init__()

    @discord.slash_command()
    async def balance(
        self,
        ctx: CustomCtx,
        member: discord.Option(discord.Member, description='The member you want to view the balance of. Leave empty to see for self.', required=False)
    ):
        """
        Shows the coins in wallet, bank and stocks owned by the user.
        """
        await ctx.defer()
        if member is None:
            userid = ctx.author.id
        else:
            userid = member.id
        account = await ctx.getAccount(userid)
        bank_type = account.bank_type
        wallet = account.wallet
        bank = account.bank
        stocks_num = 0
        embed = discord.Embed(title=f'__{bank_details[bank_type]["name"]}__', colour=embedcolor)
        embed.add_field(name=f'**<:wallet:836814969290358845> Wallet**', value=f'> `{commait(wallet)}`', inline=False)
        embed.add_field(name=f'**🏦 Bank**', value=f'> `{commait(bank)}`', inline=False)
        embed.add_field(name=f'**<:stocks:839162083324198942> Stocks**', value=f'> `{commait(stocks_num)}`', inline=False)
        fetched = bot.get_user(userid)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        embed.set_author(name=fetched.name, icon_url=fetched.display_avatar.url)

        await ctx.respond(embed=embed)
    
    @balance.error
    async def handleErrors(self, error, ctx):
        print(error)
        print(ctx)


def setup(bot_):
    global bot
    bot = bot_
    bot.add_cog(Bank())
import discord
import asyncio
from utils import *
import datetime

bot: EconomyBot = None

class Bank(discord.cog.Cog):
    def __init__(self):
        print('Bank Loaded.')
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
        user = member or ctx.author
        account = await ctx.getAccount(user.id)
        bank_type = account.bank_type
        wallet = account.wallet
        bank = account.bank
        stocks_num = 0
        embed = discord.Embed(title=f'__{bank_details[bank_type]["name"]}__', colour=embedcolor)
        embed.add_field(name=f'**<:wallet:836814969290358845> Wallet**', value=f'> `{commait(wallet)}`', inline=False)
        embed.add_field(name=f'**🏦 Bank**', value=f'> `{commait(bank)}`', inline=False)
        embed.add_field(name=f'**<:stocks:839162083324198942> Stocks**', value=f'> `{commait(stocks_num)}`', inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        embed.set_author(name=user.name, icon_url=user.display_avatar.url)

        await ctx.respond(embed=embed)
    
    @balance.error
    async def handleErrors(self, ctx: CustomCtx, error: InternalError):
        embed = discord.Embed()
        if isinstance(error, AccountNotFound):
            embed.title = error.name
            embed.description = str(error)
            embed.color = error_embed
        
        await ctx.send(embed=embed)


def setup(bot_):
    global bot
    bot = bot_
    bot.add_cog(Bank())
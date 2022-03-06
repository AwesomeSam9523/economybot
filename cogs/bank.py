import discord
import asyncio
from utils import *
from ui import *
import datetime
from discord.commands import slash_command, errors

bot: EconomyBot = None

class Bank(discord.cog.Cog):
    def __init__(self, bot_):
        self.bot = bot_
        print('Bank Loaded.')
        super().__init__()

    @slash_command()
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
        embed = balance.getEmbed(account)
        uiView = balance.ButtonsView(account, ctx)
        msg = await ctx.respond(embed=embed, view=uiView)
        uiView.msg = msg
        uiView.raiseError = self.on_command_error
    
    @slash_command()
    async def deposit(
        self,
        ctx: CustomCtx,
        amount: discord.Option(str, description='Amount to deposit to from your wallet to bank.')
    ):
        '''
        Move coins from your wallet to your bank.
        '''
        await ctx.defer()
        person = await ctx.getAccount(ctx.author.id)
        wallet = person.wallet

        if amount == 'all':
            amount = wallet
        elif amount == 'half':
            amount = int(wallet/2)
        else:
            amount = int(amount)
        if amount < 0:
            raise NegativeMoney(ctx.author)
        if amount == 0:
            raise ZeroMoney(ctx.author)

        await person.depositAction(amount)
        await ctx.respond(f'{ctx.author.mention} Successfully deposited `{commait(amount)}` coins.')
    
    @slash_command()
    async def withdraw(
        self,
        ctx: CustomCtx,
        amount: discord.Option(str, description='Amount to withdraw to from your bank to wallet.')
    ):
        '''
        Move coins from your bank to your wallet.
        '''
        await ctx.defer()
        person = await ctx.getAccount(ctx.author.id)
        bank = person.bank

        if amount == 'all':
            amount = bank
        elif amount == 'half':
            amount = int(bank/2)
        else:
            amount = int(amount)
        if amount < 0:
            raise NegativeMoney(ctx.author)
        if amount == 0:
            raise ZeroMoney(ctx.author)

        await person.withdrawAction(amount)
        await ctx.respond(f'{ctx.author.mention} Successfully withdrawn `{commait(amount)}` coins.')

    async def on_command_error(self, ctx: CustomCtx, error):
        embed = discord.Embed(color=error_embed)
        if isinstance(error, errors.ApplicationCommandInvokeError):
            error = getattr(error, 'original', error)

        try:
            embed.title = error.name
            embed.description = str(error)
        except:
            print(error)
            if isinstance(error, ValueError):
                embed.title = 'Incorrect Amount'
                embed.description = 'Coins should be `all` / `half` or numbers only.'
            else:
                embed.title = 'Unknown Error'

        await ctx.respond(embed=embed)


def setup(bot_):
    global bot
    bot = bot_
    bot.add_cog(Bank(bot_))
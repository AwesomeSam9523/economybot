import discord
import asyncio
from utils import *
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
            embed.description = 'Unknown Error.'
            print(error)

        await ctx.respond(embed=embed)


def setup(bot_):
    global bot
    bot = bot_
    bot.add_cog(Bank(bot_))
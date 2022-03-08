import discord
import asyncio
from core import *
from utils import *
from ui import *
import datetime
from discord.commands import slash_command, errors
from discord.ext import tasks
import logging
log = logging.getLogger(__name__)

bot: EconomyBot = None

@tasks.loop(seconds=30)
async def updateAverageBalance():
    _data = await bot.database.getCollection('users').find({})
    _data_len = len(_data)
    for index, account in enumerate(_data):
        log.info(f'[{index+1}/{_data_len}] Updating Average data for {account["userid"]}')
        old_avg = account.get('average', 0)
        time_made = int(time.time()) - account['joined']
        if time_made < 30:
            #log.info(f'Avg. Balance skipped for {account["userid"]} (Time Difference: {time_made})')
            return
        iterations = int(time_made/30)
        _sum = old_avg * iterations
        new_avg = (_sum + account['bank']) / (iterations + 1)
        new_avg = round(new_avg)
        if new_avg == old_avg:
            continue
        asyncio.create_task(bot.database['users'].findOneAndUpdate(
            { 'userid': account['userid'] },
            { '$set': { 'average': new_avg } }
        ))
        #log.info(f'Avg. Balance set for {account["userid"]}: {new_avg} (Iterations: {iterations})')

@updateAverageBalance.error
async def handle_task_error(error: Exception):
    printError(error)

class Bank(discord.cog.Cog):
    def __init__(self, bot_):
        self.bot = bot_
        #updateAverageBalance.start()
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
        if user == ctx.author:
            uiView = balance.ButtonsView(account, ctx)
            msg = await ctx.respond(embed=embed, view=uiView)
            uiView.msg = msg
            uiView.raiseError = self.cog_command_error
            return
        
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
    
    @slash_command()
    async def bank(
        self,
        ctx: CustomCtx,
        member: discord.Option(discord.Member, description='The member you want to view the bank of. Leave empty to see for self.', required=False)
    ):
        '''
        Check the tier, name, interest rate and average balance in your bank.
        You can also change your tier if you have enough coins!
        '''
        await ctx.defer()
        user = member or ctx.author

        person = await ctx.getAccount(user.id)
        btype = person.bank_type

        embed = discord.Embed(description='Here are your bank details:\n\u200b', color=embedcolor)
        embed.add_field(name='Bank Name', value=f'{bank_details[btype]["name"]}')
        embed.add_field(name='Bank Tier', value=f'{bank_details[btype]["tier"]}')
        embed.add_field(name='\u200b', value='\u200b')
        embed.add_field(name='Daily Interest', value=f'{bank_details[btype]["rate"]}%')
        embed.add_field(name='Current Balance', value=f'`{commait(person.bank)}`')
        embed.add_field(name='Average Balance', value=f'`{commait(person.average_balance)}`')
        embed.add_field(name='Note:', value='To claim interest, use `e.daily`.\n'
                                            'Your average balance in last 24 hours will be taken in account for that.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        embed.set_author(name=f'{user.name} | 🏦 Know Your Bank!', icon_url=user.display_avatar.url)

        view = bank.BankView(ctx)
        msg = await ctx.respond(embed=embed, view=view)
        view.msg = msg

    async def cog_command_error(self, ctx: CustomCtx, error):
        embed = discord.Embed(color=error_embed)
        if isinstance(error, errors.ApplicationCommandInvokeError):
            error = getattr(error, 'original', error)

        try:
            embed.title = error.name
            embed.description = str(error)
        except:
            printError(error)
            if isinstance(error, ValueError):
                embed.title = 'Incorrect Amount'
                embed.description = 'Coins should be `all` / `half` or numbers only.'
            else:
                embed.title = 'Unknown Error'

        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot_):
    global bot
    bot = bot_
    bot.add_cog(Bank(bot_))
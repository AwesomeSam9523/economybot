import asyncio
from discord import ui
import discord
from core import *
from utils import *
import datetime


class WithdrawModal(ui.Modal):
    def __init__(self, view) -> None:
        super().__init__('Withdraw Coins')
        self.view = view
        self.add_item(ui.InputText(
            style=discord.InputTextStyle.short,
            label='Enter amount of coins to withdraw:',
            placeholder='Enter \'all\' / \'half\' / exact amount in numbers',
            required=True
        ))
    
    async def callback(self, interaction: discord.Interaction):
        view: ButtonsView = self.view
        value = self.children[0].value.lower()
        await view.updateAccount()
        coins = view.account.bank
        if value == 'all':
            value = coins
        elif value == 'half':
            value = int(coins/2)
        else:
            value = int(value)

        try:
            await view.processAction('withdraw', value)
        except Exception as e:
            view.ctx.interaction_respond = interaction.response.send_message
            asyncio.create_task(view.raiseError(view.ctx, e))
        else:
            value = commait(value)
            await interaction.response.send_message(f'Successfully withdrawn `{value}` coins.', ephemeral=True)


class DepositModal(ui.Modal):
    def __init__(self, view) -> None:
        super().__init__('Deposit Coins')
        self.view = view
        self.add_item(ui.InputText(
            style=discord.InputTextStyle.short,
            label='Enter amount of coins to deposit:',
            placeholder='Enter \'all\' / \'half\' / exact amount in numbers',
            required=True
        ))

    async def callback(self, interaction: discord.Interaction):
        view: ButtonsView = self.view
        value = self.children[0].value.lower()
        await view.updateAccount()
        coins = view.account.wallet
        if value == 'all':
            value = coins
        elif value == 'half':
            value = int(coins/2)
        else:
            value = int(value)

        try:
            await view.processAction('deposit', value)
        except Exception as e:
            view.ctx.interaction_respond = interaction.response.send_message
            asyncio.create_task(view.raiseError(view.ctx, e))
        else:
            value = commait(value)
            await interaction.response.send_message(f'Successfully deposited `{value}` coins.', ephemeral=True)

class ButtonsView(ui.View):
    def __init__(self, account: UserAccount, ctx: CustomCtx):
        self.msg: discord.Message = None
        self.account = account
        self.ctx = ctx
        super().__init__()

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                random.choice(self.ctx.bot.phrases['inter']).format(usertag=str(self.ctx.author)),
                ephemeral=True
            )
            return False
        return True
    
    async def updateAccount(self):
        self.account = await self.ctx.getAccount(self.ctx.author.id)

    async def on_timeout(self) -> None:
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)
    
    async def raiseError(self, ctx: CustomCtx, error: Exception) -> None:
        print(error)

    async def processAction(self, action: str, coins: int) -> None:
        if action == 'deposit':
            await self.account.depositAction(coins)
            await self.msg.edit(embed=getEmbed(self.account))
        else:
            await self.account.withdrawAction(coins)
            await self.msg.edit(embed=getEmbed(self.account))

    @discord.ui.button(label='Deposit', style=discord.ButtonStyle.green)
    async def deposit_via_ui(self, button, interaction: discord.Interaction):
        modal = DepositModal(self)
        await interaction.response.send_modal(modal)
    
    @discord.ui.button(label='Withdraw', style=discord.ButtonStyle.blurple)
    async def withdraw_via_ui(self, button, interaction: discord.Interaction):
        modal = WithdrawModal(self)
        await interaction.response.send_modal(modal)

def getEmbed(account: UserAccount):
    '''
    Returns a `discord.Embed` object against the `account`.
    '''
    bank_type = account.bank_type
    wallet = account.wallet
    bank = account.bank
    stocks_num = 0
    embed = discord.Embed(title=f'__{bank_details[bank_type]["name"]}__', colour=embedcolor)
    embed.add_field(name=f'**<:wallet:836814969290358845> Wallet**', value=f'> `{commait(wallet)}`', inline=False)
    embed.add_field(name=f'**🏦 Bank**', value=f'> `{commait(bank)}`', inline=False)
    embed.add_field(name=f'**<:stocks:839162083324198942> Stocks**', value=f'> `{commait(stocks_num)}`', inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    
    return embed
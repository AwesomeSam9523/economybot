import asyncio
from discord import ui
import discord
from core import *
from utils import *
import datetime
from prettytable import PrettyTable

class BankView(discord.ui.View):
    def __init__(self, ctx: CustomCtx):
        super().__init__()
        self.ctx = ctx
        self.msg: discord.Message = None
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                random.choice(self.ctx.bot.phrases['inter']).format(usertag=str(self.ctx.author)),
                ephemeral=True
            )
            return False
        await interaction.response.defer()
        return True

    @discord.ui.button(label='Change Tier', style=discord.ButtonStyle.green)
    async def tier(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        x = PrettyTable()
        x.field_names = ['Bank Name', 'Tier', 'Interest']
        for i in bank_details.values():
            x.add_row([i['name'], i['tier'], f'{i["rate"]}%'])

        embed = discord.Embed(
            title='List of Banks',
            description=f'Choose your bank to get higher interest rate, loans and more benefits!\n```\n{x}```\n',
            color=embedcolor
        )

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=ctx.bot.pfp)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        self.clear_items()
        self.add_item(BankTiers(ctx, self.msg))
        await self.msg.edit(embed=embed, view=self)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.msg.edit(view=self)

class BankTiers(discord.ui.Select):
    def __init__(self, ctx: CustomCtx, msg: discord.Message):
        options = [
            discord.SelectOption(
                label='Tier I',
                emoji='🏦',
                description='Common Finance Bank Ltd.',
                value=1,
            ),
            discord.SelectOption(
                label='Tier II',
                emoji='🏦',
                description='National Bank Pvt. Ltd.',
                value=2,
            ),
            discord.SelectOption(
                label='Tier III',
                emoji='🏦',
                description='International Bank of Finance Ltd.',
                value=3,
            ),
        ]
        self.ctx = ctx
        self.msg = msg
        super().__init__(
            placeholder='Click here to choose tier...',
            options=options, row=4
        )

    async def callback(self, interaction: discord.Interaction):
        ctx = self.ctx
        bot = ctx.bot
        assert self.view is not None
        view: UpgradeBank = self.view

        tier = int(self.values[0])
        user = await ctx.getAccount(interaction.user.id)

        if tier <= 0 or tier > 3:
            return await interaction.followup.send(
                content=f'{ctx.author.mention} Invalid Tier'
            )
        elif user.bank_type == tier:
            return await interaction.followup.send(
                content=f'{ctx.author.mention} You already own a account in this bank'
            )
        elif user.bank_type > tier:
            return await interaction.followup.send(
                content=f'{ctx.author.mention} You cannot downgrade your bank tier'
            )

        bal = user.totalBalance
        price = 5000 if tier == 2 else 10000
        total = int(bal * 0.01 + price)

        x = PrettyTable()
        x.field_names = ['Name', '      ', 'Cost']
        x.align['Cost'] = 'l'
        x.add_row(['Account Opening', '      ', price])
        x.add_row(['Transfering', '      ', bal * 0.01])
        x.add_row(['      ', '      ', '      '])
        x.add_row(['Grand Total', '      ', total])

        embed = discord.Embed(
            title='Upgrade your bank',
            description=f'Here is the cost for upgrading your bank: \n```\n{x}```',
            color=embedcolor
        )
        await self.msg.edit(embed=embed, view=UpgradeBank(ctx, tier, self.msg))

class UpgradeBank(discord.ui.View):
    def __init__(self, ctx: CustomCtx, tier: int, msg: discord.Message):
        super().__init__()
        self.ctx = ctx
        self.tier = tier
        self.msg = msg
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                random.choice(self.ctx.bot.phrases['inter']).format(usertag=str(self.ctx.author)),
                ephemeral=True
            )
            return False
        await interaction.response.defer()
        return True

    @discord.ui.button(label='Accept', style=discord.ButtonStyle.green, emoji=economysuccess)
    async def accept(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        bot = ctx.bot
        tier = self.tier
        user = await ctx.getAccount(ctx.author.id)
        bal = user.totalBalance
        price = 5000 if tier == 2 else 10000
        total = int(bal * 0.01 + price)
        if total > user.bank:
            embed = discord.Embed(
                title=f'{economyerror} Insufficient Funds in bank!',
                description=random.choice(bot.phrases['less_bal']),
                color=error_embed
            )
        else:
            await user._set_coins(
                {
                    'bank': user.bank - total,
                    'bank_type': tier
                }
            )
            embed = discord.Embed(
                title=f'{economysuccess} Success!',
                description=f'Bank upgraded to `Tier {tier}` successfully!',
                color=success_embed
            )
        await self.msg.edit(embed=embed, view=None)

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red, emoji=economyerror)
    async def cancel(self, button, interaction: discord.Interaction):
        embed = discord.Embed(
            title=f'{economyerror} Cancelled!',
            color=error_embed
        )
        await self.msg.edit(embed=embed, view=None)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.msg.edit(view=self)

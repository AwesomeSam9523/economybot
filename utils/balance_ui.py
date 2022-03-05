from discord import ui
import discord
from utils import economybot
from utils.functions import commait

class ModalManager():
    def __init__():
        pass

    async def createDepositModal():
        return DepositModal()


class DepositModal(ui.Modal):
    def __init__(self) -> None:
        super().__init__('Deposit Coins')
        self.add_item(ui.InputText(
            style=discord.InputTextStyle.short,
            label='Enter amount of coins to deposit:',
            placeholder='Enter "all" / "half" / exact amount in numbers',
            required=True
        ))

    async def callback(self, interaction: discord.Interaction):
        value = self.children[0].value
        followup = interaction.response.send_message
        try:
            value = int(value)
            value = commait(value)
            await followup(f'Deposited `{value}` coins successfully!', ephemeral=True)
        except:
            await followup(f'You just tried to mess with me but failed :(', ephemeral=True)

class ButtonsView(ui.View):
    def __init__(self, ctx: economybot.CustomCtx):
        self.msg: discord.Message = None
        self.ctx = ctx
        super().__init__()

    
    async def on_timeout(self) -> None:
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)
    
    @discord.ui.button(label='Deposit', style=discord.ButtonStyle.green)
    async def deposit_via_ui(self, button, interaction: discord.Interaction):
        modal = DepositModal()
        await interaction.response.send_modal(modal)

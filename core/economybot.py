from typing import Union
import discord
from utils import *
from .errors import *
from .database import Database
import time

class EconomyBot(discord.Bot):
    def __init__(self):
        intents = discord.Intents(
            guild_reactions=True,
            guild_messages=True,
            guilds=True,
            dm_messages=True,
            members=True
        )
        super().__init__(intents=intents, debug_guilds=[708067789830750449])
        self.unsaved = {}
        self.phrases = {}
        self.current_stock = []
        self.total_lines = 0
        self.pfp = ''
        self.raw_status = ''
        self.shopc = {}
        self.items = {}
        self.emotes = {}
        self.unboxbgs = {}
        self.allitems = allItems
        self.cachedinv = {}
        self.used = {}
        self.ms = {}
        self.activems = {"users": [], "games":[]}
        self.waitings = {}
        self.globaltrades = []
        self.random_status = True
        self.maint = False
        self.cooldown = {}
        with open('files/bot_data.json', 'r') as c:
            data = json.load(c)
            self.phrases = data["phrases"]
            self.shopc = data["shop"]["category"]
            self.items = data["items"]
            self._status = data["status"]
            self.cooldown = data["cooldown"]
        self.database = Database()
    
    async def get_application_context(self, interaction: discord.Interaction, cls=None) -> discord.ApplicationContext:
        return await super().get_application_context(interaction, cls=cls or CustomCtx)
    
    async def on_ready(self):
        print(self.pending_application_commands)
        print('Ready!')


class CustomCtx(discord.ApplicationContext):

    def __init__(self, bot, interaction):
        self._interaction_respond = None
        super().__init__(bot, interaction)
    
    @property
    def respond(self):
        if self.interaction_respond is None:
            return super().respond
        else:
            return self.interaction_respond

    @property
    def interaction_respond(self):
        '''
        Returns ~`discord.Interaction` instead of `Context.respond` to handle modals.
        '''
        return self._interaction_respond
    
    @interaction_respond.setter
    def interaction_respond(self, new_respond):
        self._interaction_respond = new_respond
    
    async def _getuserAccount(self, id: int, upsert: bool):
        document = await self.bot.database['users'].findOne({ 'userid': id })
        
        if document is None and upsert:
            document = await self.bot.database['users'].insertOne({
                'userid': self.author.id,
                'bank_type': 1,
                'wallet': 500,
                'bank': 0,
                'joined': int(time.time())
            })
        elif document is None:
            raise AccountNotFound(self.bot.get_user(id))

        return UserAccount(self.bot, document)
    
    async def getAccount(self, userid: int = None, upsert: Union[bool, None] = None):
        userid = userid or self.author.id
        if upsert is None:
            upsert = userid == self.author.id
        return await self._getuserAccount(userid, upsert)

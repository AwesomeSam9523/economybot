from motor.motor_asyncio import *
import pymongo
import discord
from utils.errors import *
from .consts import *
from .accounts import *
import time
import os

class CustomCtx(discord.ApplicationContext):
    
    async def _getuserAccount(self, id: int, upsert):
        document = await self.bot.db.users.find_one({ 'userid': id })
        if document is None:
            if upsert:
                await self.bot.db.users.insert_one({
                    'userid': self.author.id,
                    'bank_type': 1,
                    'wallet': 500,
                    'bank': 0,
                    'joined': int(time.time())
                })
                document = await self.bot.db.users.find_one({ 'userid': id })
            else:
                raise AccountNotFound(self.bot.get_user(id))
        
        return UserAccount(self.bot, document)
    
    async def getAccount(self, userid=None, upsert=None):
        userid = userid or self.author.id
        if upsert is None:
            upsert = userid == self.author.id
        return await self._getuserAccount(userid, upsert)

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
        client = AsyncIOMotorClient(os.environ['MONGO'])
        self.db = client.economy
    
    async def get_application_context(self, interaction: discord.Interaction, cls=None) -> discord.ApplicationContext:
        return await super().get_application_context(interaction, cls=cls or CustomCtx)
    
    async def on_ready(self):
        print(self.pending_application_commands)
        print('Ready!')

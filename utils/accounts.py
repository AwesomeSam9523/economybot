from .errors import *
import pymongo

class UserAccount():

    def __init__(self, bot, document: dict) -> None:
        self.bot = bot
        self.document = document
    
    @property
    def user(self):
        '''
        Return `discord.User` or `None`.
        '''
        return self.bot.get_user(self.document['id'])
    
    @property
    def userid(self):
        '''
        Returns the userid for the `User`.
        '''
        if (self.user):
            return self.user.id
    
    @property
    def wallet(self) -> int:
        '''
        Returns the balance in the wallet of the user.
        '''
        return self.document['wallet']
    
    @property
    def bank(self) -> int:
        '''
        Returns the balance in the bank of the user.
        '''
        return self.document['bank']
    
    @property
    def bank_type(self) -> int:
        '''
        Returns the bank type for the user.
        '''
        return self.document['bank_type']
    
    @property
    def totalBalance(self):
        '''
        Shorthand for getting total balance of the user.
        '''
        return self.wallet + self.bank
    
    async def _modify_coins(self, data: dict):
        self.document = await self.bot.db.users.find_one_and_update(
            { 'userid': self.userid },
            { '$inc': data },
            return_document=pymongo.ReturnDocument.AFTER
        )
    
    async def _set_coins(self, data: dict):
        self.document = await self.bot.db.users.find_one_and_update(
            { 'userid': self.userid },
            { '$set': data },
            return_document=pymongo.ReturnDocument.AFTER
        )
    
    async def _ensure_coins(self, coins: int):
        _coins = await self.bot.db.users.find_one({
            { 'userid': self.userid }
        })
        _coins = _coins.get('coins', 0)
        return coins >= _coins, _coins
    
    async def addCoins(self, coins: int, type: int = 1, returnType: int = None):
        '''
        Adds coins to user's account and returns the balance.
        '''
        returnType = returnType or type
        if type == 0:
            data = { 'wallet': coins }
        else:
            data = { 'bank': coins }
        
        await self._modify_coins(data)

        if returnType == 0:
            return self.wallet
        elif returnType == 1:
            return self.bank
        else:
            return self.totalBalance
    
    async def removeCoins(self, coins: int, type: int = 1, returnType: int = None, safe=False, silent=False):
        '''
        Removes coins from user's account and returns the balance.
        '''
        returnType = returnType or type

        if safe:
            _safe, _coins = await self._ensure_coins(coins)
            if not _safe:
                if silent:
                    coins = _coins
                else:
                    raise NotEnoghCoins
    
        coins *= -1
        if type == 0:
            data = { 'wallet': coins }
        else:
            data = { 'bank': coins }

        await self._modify_coins(data)

        if returnType == 0:
            return self.wallet
        elif returnType == 1:
            return self.bank
        else:
            return self.totalBalance
    
    async def resetAccount(self):
        data = {
            'wallet': 0,
            'bank': 0
        }

        await self._set_coins(data)

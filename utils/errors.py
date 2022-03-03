import random
import discord
from .consts import phrases

class InternalError(Exception):
    def __init__(self, name: str, type: str, **kwargs):
        self._name = name
        self._type = type
        self._user = kwargs.pop('user', None)

        super().__init__()

    @property
    def name(self) -> str:
        '''
        Returns the name of the error
        '''
        return self._name
    
    @property
    def type(self) -> str:
        '''
        Returns the type of the error. Use this for internal handeling only.
        '''
        return self._type
    
    @property
    def user(self) -> discord.User:
        '''
        Returns the user associated with it (if any at all).
        '''
        return self._user
    
    def getRandomMessage(self):
        '''
        Returns a random insult message.
        '''
        type = self.type
        return random.choice(phrases.get(self.type) or ['Smh imagine not having an account..'])
    
    def __str__(self):
        mention = ''
        if self.user:
            mention += f'{self.user.mention} '
        
        return mention + self.getRandomMessage()

class NotEnoughCoins(InternalError):
    def __init__(self, user) -> None:
        super().__init__(
            'Insufficient Coins',
            'less_bal',
            user = user
        )

class AccountNotFound(InternalError):
    def __init__(self, user) -> None:
        super().__init__(
            'Account Not Found',
            'noAcc',
            user = user
        )

class NegativeMoney(InternalError):
    def __init__(self, user) -> None:
        super().__init__(
            'Negative Money',
            'negative',
            user = user
        )

class ZeroMoney(InternalError):
    def __init__(self, user) -> None:
        super().__init__(
            'Zero Money',
            'zero',
            user = user
        )
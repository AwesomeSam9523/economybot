import discord

class InternalError(Exception):
    def __init__(self, name: str, type: str, **kwargs):
        self.name = name
        self.type = type
        self.user = kwargs.pop('user', None)

        super().__init__()

    @property
    def name(self) -> str:
        '''
        Returns the name of the error
        '''
        return self.name
    
    @property
    def type(self) -> str:
        '''
        Returns the type of the error. Use this for internal handeling only.
        '''
        return self.type
    
    @property
    def user(self) -> discord.User:
        '''
        Returns the user associated with it (if any at all).
        '''
        return self.user
    
    def getRandomMessage(self):
        '''
        Returns a random insult message.
        '''
        type = self.type
        return 'Smh imagine not having an account..'
    
    def __str__(self):
        mention = ''
        if self.user:
            mention += f'{self.user.mention} '
        
        return mention + self.getRandomMessage()

class NotEnoghCoins(Exception):
    pass

class AccountNotFound(InternalError):
    def __init__(self, user) -> None:
        super().__init__(
            'Account Not Found',
            'noAcc',
            { 'user': user }
        )
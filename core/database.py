from typing import Dict, Optional
import pymongo
import os
from motor.motor_asyncio import *
from .errors import *

class DbCollection:

    def __init__(self, collection) -> None:
        self._cached_documents: Dict[str, dict] = {}
        self._collection = collection

    async def findOne(self, data: dict, cache=False, sync=True) -> dict:
        '''
        Returns back `pymongo` Document matching the `data`.
        If `cache` is `True`, it just returns back the cached document.
        If `sync` is `True`, it syncs the cached document with the one from server.
        '''
        if cache:
            try:
                _id = data.get('userid')
                return self._cached_documents[_id]
            except KeyError:
                raise DocumentNotInCache
        
        doc = await self._collection.find_one(data)
        if doc is not None:
            _id = doc['userid']
            if sync:
                self._cached_documents[_id] = doc

        return doc
    
    async def findOneAndUpdate(self, filter: dict, data: dict, sync=True) -> dict:
        '''
        Finds a document matching `data` and updates it. 
        If `sync` is `True`, it syncs the cached document with the one from server.
        '''
        doc = await self._collection.find_one_and_update(
            filter,
            data,
            return_document=pymongo.ReturnDocument.AFTER
        )
        if doc is not None:
            _id = doc['userid']
            if sync:
                self._cached_documents[_id] = doc

        return doc


class Database:

    def __init__(self):

        self._database_connecter = AsyncIOMotorClient(os.environ['MONGO'])
        self._database = self._database_connecter.economy
        
        collections = ['users']
        self._collections = {}

        for i in collections:
            dbCol = self._database[i]
            self._collections[i] = DbCollection(dbCol)
    
    def __getitem__(self, _name: str):
        '''
        Shorthand for `.getCollection()`
        '''
        return self.getCollection(_name)
        
    @property
    def collections(self) -> Dict[str, DbCollection]:
        '''
        Returns all the collections found in the database. 
        '''
        return self._collections

    def getCollection(self, name: str) -> Optional[DbCollection]:
        '''
        Returns a collection (if found), else raises `core.errors.CollectionNotFound`.
        '''
        try:
            return self._collections[name]
        except KeyError:
            raise CollectionNotFound

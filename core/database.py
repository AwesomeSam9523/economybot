from typing import Dict, Optional
import pymongo
import os
from motor.motor_asyncio import *
from .errors import *
import logging
log = logging.getLogger(__name__)

class DbCollection:

    def __init__(self, collection) -> None:
        self._cached_documents: Dict[str, dict] = {}
        self._collection = collection
    
    @property
    def collection(self):
        '''
        Returns back collection for low-level use. This should rarely be used.
        '''
        return self._collection
    
    async def find(self, data: dict) -> list:
        log.info(f'Looking up for {data}.')
        _results = await self.collection.find(data).to_list(length=None)
        log.info(f'Mongo returned us with {len(_results)} results against {data}.')
        return _results

    async def findOne(self, data: dict, sync=False) -> dict:
        '''
        Returns back `Document` matching the `data`.
        If `cache` is `True`, it just returns back the cached document.
        If `sync` is `True`, it syncs the cached document with the one from server.
        '''
        _id = data.get('userid')
        log.info(f'Lookup for {data} with sync {sync}')

        doc = self._cached_documents.get(_id)
        log.info(f'Document with filter {data} in internal cache: {doc}')

        if sync or doc is None:
            _doc = await self.collection.find_one(data)
            log.info(f'Updated cache for {_id}: {self._cached_documents.get(_id)} => {_doc}')
            self._cached_documents.setdefault(_id, {}).update(_doc)
        
        logging.info(f'Returning {self._cached_documents.get(_id)} for {data}')
        return self._cached_documents.get(_id)
    
    async def findOneAndUpdate(self, filter: dict, data: dict, sync=True) -> dict:
        '''
        Finds a document matching `data` and updates it. 
        If `sync` is `True`, it syncs the cached document with the one from server.
        '''
        log.info(f'Updating {filter} to {data} with sync {sync}.')
        doc = await self.collection.find_one_and_update(
            filter,
            data,
            return_document=pymongo.ReturnDocument.AFTER
        )
        log.info(f'Atlas returned us {doc}')
        if doc is not None:
            _id = doc['userid']
            if sync:
                log.info(f'Synced {doc} to internal cache.')
                self._cached_documents.setdefault(_id, {}).update(doc)
        
        log.info(f'Returning {doc} with filter: {filter} and data: {data}')
        return doc
    
    async def insertOne(self, data: dict, sync=True) -> dict:
        '''
        Inserts a `document` and returns back the inserted document.
        If `sync` is `True`, it adds the document to insernal cache. 
        '''
        log.info(f'Inserting {data} with sync as {sync}.')
        await self.collection.insert_one(data)
        return await self.findOne(data, sync=sync)

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

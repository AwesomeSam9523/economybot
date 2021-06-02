"""
The MIT License (MIT)

Copyright (c) 2021-present BlackThunder#4007
"""

import discord
import ujson
from concurrent.futures import ThreadPoolExecutor
import requests
import functools

class FileUploadError(Exception):pass

class ConcurrentUploader:
    def __init__(self, client):
        self.client = client
        
    def sync_upload_file(self, channel, file_data, filename, embed, content):
        file = {
            filename: file_data
        }
        
        data_json = {}
        
        if embed is not None:
            data_json["embed"] = embed.to_dict()

        if content is not None:
            data_json["content"] = str(content)

        return requests.post(
            f"https://discord.com/api/v8/channels/{channel.id}/messages",
            files = file,
            data = {"payload_json": ujson.dumps(data_json)},
            headers = {"Authorization":"Bot " + self.client.http.token}
        )

    async def upload_file(self, channel, bytes_io, filename="unknown.png", embed=None, content=None):
        """
        Upload files concurrently in async
        """
        with ThreadPoolExecutor(max_workers = 1) as executor:
            response = await self.client.loop.run_in_executor(executor,
                                                              functools.partial(self.sync_upload_file,
                                                                                channel,
                                                                                bytes_io,
                                                                                filename,
                                                                                embed,
                                                                                content
                                                                                )
                                                              )
        if response.status_code != 200:
            raise FileUploadError(f"Received Response: {response.status_code}")
        return discord.Message(
            state = self.client._get_state(),
            channel=channel,
            data = response.json()
        )

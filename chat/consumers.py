# chat/consumers.py
import json
import time

#from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

from rentapp.models import Mensaje

class ChatConsumer (AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        # Informa al cliente del exito
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        ''' Cliente envia informacion y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        amistad = text_data_json["amistad"]
        message = text_data_json["message"]
        pub_date = text_data_json["pub_date"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", 
                                   "amistad": amistad,
                                   "message": message,
                                   "pub_date": pub_date, }
        )
    # Receive message from room group
    async def chat_message(self, event):
        amistad = event["amistad"]
        message = event["message"]
        pub_date = event["pub_date"]
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            {
                'amistad': amistad,
                "message": message, 
                "pub_date": pub_date,       
            }
        )
    )

        '''await Mensaje(
           # amistad = self.room_name,
            amistad = 54,
            texto = message
        ).save()
        '''


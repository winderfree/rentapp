# chat/consumers.py
import asyncio
import json
import threading
import time
from asgiref.sync import sync_to_async
# Debes importar el módulo de conexión:
from django.db import connection
from channels.generic.websocket import AsyncWebsocketConsumer
from rentapp.forms import MensajeForm
from rentapp.models import Amistad, Usertario
from . models import Mensaje

text_data = []
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
    # from asgiref.sync import async_to_sync, sync_to_async
    async def prueba(self):
        return 54
    # insertar los querys
    # async def insertar_mensaje(self):
    #     # mydato = threading.local()        
    #     # consulta = Amistad.objects.raw("SELECT * FROM chat_mensaje")
    #     # consulta = Amistad.objects.raw("INSERT INTO chat_mensaje(amistad_id, texto)VALUES(4, 'Hola mundolo')")
        
    #     # consulta_2 = list(consulta)
    #     # print(consulta_2)
        
    #     return consulta 
    # async def pueba_cursor(self):
    #     query = "SELECT * FROM chat_mensaje"
    #     # Obtienes el objeto cursor:
    #     cursor =  Mensaje.objects.raw(query)
    #     # Preparas la consulta SQL para luego reemplazar los datos que desees insertar:
    #     # prueba = [4, "fjdorgerhgiure"]
    #     # (amistad_id, texto) 
    #             # VALUES (%s, %s) 
    #     # Ejecutas la query. Aquí reemplazamos la variable que necesitamos para nuestro INSERT en forma de lista
    #     return  [ x async for x in cursor]
        # , [prueba]
# Puedes usar el commit como ya lo tienes
    async def receive(self, text_data): 
        ''' Cliente envia informacion y nosotros la recibimos '''
        text_data_json = json.loads(text_data)
        amistad_id = text_data_json["amistad"]
        texto = text_data_json["texto"]
        pub_date = text_data_json["pub_date"]

        query = f"INSERT INTO rentapp_mensaje(amistad_id,texto,tipo,pub_date)VALUES('{amistad_id}', '{texto}','rendatario','12/12/12')"
        mensaje = Mensaje.objects.raw(query)
        print(mensaje)
        # f = MensajeForm()
        # new_mensaje = Mensaje(
        # amistad =  Amistad.objects.get(id=amistad_id), #12
        # texto = texto,
        # pub_date =  time.strftime('%Y-%m-%d %I:%M'), )
        # new_mensaje.save()

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", 
                                   "amistad_id": amistad_id,
                                   "texto": texto,
                                   "pub_date": pub_date, }
            
        )
        return print([x async for x in mensaje]) 


    # Receive message from room group
    async def chat_message(self, event):
        amistad_id = event["amistad_id"]
        texto = event["texto"]
        pub_date = event["pub_date"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps(
            {
                'amistad_id': amistad_id,
                "texto": texto, 
                "pub_date": pub_date,       
            }
        )
    )

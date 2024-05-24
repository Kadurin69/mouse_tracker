import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from mouseover.models import MouseData
import cv2
import time
from channels.db import database_sync_to_async

class MouseConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		await self.accept()

		
	async def disconnect(self):
		pass

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		x = text_data_json['x']
		y = text_data_json['y']
		button_press = text_data_json['press']
		if button_press:
			cam = cv2.VideoCapture(0)
			result, snapshot = cam.read()
			if result:
				timestamp = time.strftime("%Y%m%d-%H%M%S")
				img_path = f"mouseover/images/{timestamp}.png"
				cv2.imwrite(img_path,snapshot)
				cam.release()
				await self.save_to_database(x_data=x,y_data=y,img_path=img_path)

	@database_sync_to_async
	def save_to_database(self,x_data,y_data,img_path):
		MouseData.objects.create(x=x_data,y=y_data,image_location=img_path)


		

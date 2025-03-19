from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event): # connection requestion
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print(event["text"])
        self.send({
            "type": "websocket.send",
            "text": "Hello I got hjsfbhjsbfjhsdb",
        })

    def websocket_disconnect(self,event):
        self.send({
            "type":"websocket.close",
            'code':1000,
        })
    
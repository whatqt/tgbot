from mongodb.connection import connection
import bson



class CacheSendMessTime:
    def __init__(self, id_user):
        self.id_user = id_user
        self.tgbot = connection["tgbot"]

    async def insert_user(self, time):
        old_notification = self.tgbot["old_notification"]
        document = await old_notification.insert_one(
            {
                "_id": self.id_user,
                "time": time
            }
        )
        return document
    
    async def find_user(self):
        old_notification = self.tgbot["old_notification"]
        info_at_notification = await old_notification.find_one(
            {"_id": self.id_user}
        )
        print(info_at_notification)
        return info_at_notification
    
    async def delete_user(self):
        old_notification = self.tgbot["old_notification"]
        info_at_notification = await old_notification.delete_one(
            {"_id": self.id_user}
        )
        print(info_at_notification)
        return info_at_notification

    async def all_active_notification(self):
        old_notification = self.tgbot["old_notification"]
        cursor = old_notification.find_raw_batches()
        async for batch in cursor:
            full_data = bson.decode_all(batch)
            return full_data                
            
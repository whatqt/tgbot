from pymongo import AsyncMongoClient
import asyncio


async def create_collection():
    connection = AsyncMongoClient("localhost", 27017)
    tgbot = connection["tgbot"]
    # old_notification = tgbot["old_notification"]
    old_notification = tgbot["test_old_notification"]
    # await old_notification.insert_one(
    #     {
    #         "_id": "test",
    #         "time": "19:17:00"
    #     }
    # )
    obj = await old_notification.find_one({"_id": "test"})

    print(obj["time"])

asyncio.run(create_collection())
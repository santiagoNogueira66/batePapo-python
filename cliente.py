import websockets
import asyncio

async def menssage():
    async with websockets.connect("ws://10.4.41.54:8750") as socket:
        msn = input("digite uma mensagem pro love: ")
        await socket.send(msn)
        print(await socket.recv())

while True:
    asyncio.get_event_loop().run_until_complete(menssage())
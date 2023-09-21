import websockets
import asyncio

#função quando um cliente se comunicar
async def reponse (websocket, path):
    msn = await websocket.recv()
    print(f"mensagem recebida:{msn}")
    resp = input("digite a resposta: ")
    await websocket.send("resp")
start_server = websockets.serve(reponse,'0.0.0.0',8750)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
import asyncio
import websockets as wsc
import json as js


async def exchange(location):
    async with wsc.connect(location) as websocket:
        a, g, p = 5, 10, 23
        Alice = g ** a % p  # публичный ключ Алисы
        params = js.dumps({
            "g": g,
            "p": p,
            "Alice": Alice
        })
        await websocket.send(params)
        Bob = int(await websocket.recv())  # получение публичного ключа Боба
        s = Bob**a % p
        print("Shared secret key", s)


asyncio.get_event_loop().run_until_complete(
    exchange('ws://localhost:1234')
)


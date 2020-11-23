import asyncio
import websockets as wsc
import json as js


async def exchange(wsc, path):
    bob_s_private_num = 5
    message = await wsc.recv()    # ожидание получения сообщения
    params = js.loads(message)  # для конвертирования json в python
    print("params:", params)
    g, p, Alice = params.values()
    Bob = g ** bob_s_private_num % p  # публичный ключ боба
    s = Alice ** bob_s_private_num % p  # закрытый ключ
    print('Secret key:', s)
    await wsc.send(str(Bob))


start_server = wsc.serve(exchange, "localhost", 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


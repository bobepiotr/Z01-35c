import asyncio
import json
import logging
import websockets

USERS = set()
host = 'localhost'
port = 6789


async def notify_users(message):
    if USERS:
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users('login')


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users('logout')


async def counter(websocket, path):
    await register(websocket)
    try:
        await websocket.send('hello')
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "logged_in":
                await notify_users('login')
            elif data["action"] == "registered":
                await notify_users('register')
            elif data["action"] == 'new_message':
                await notify_users('new_message')
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)


if __name__ == '__main__':
    start_server = websockets.serve(counter, host, port)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
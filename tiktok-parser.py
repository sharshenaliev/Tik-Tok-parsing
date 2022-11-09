import asyncio
from pyppeteer import launch, launcher
import json


username = input()

async def main():
    source = {'https://github.com/': 'Page not found · GitHub · GitHub',
              'https://career.habr.com/': 'Хабр Карьера - ошибка 404',
              'https://pikabu.ru/@': '404. Страница не найдена',
              'https://reddit.com/user/': 'Reddit - Dive into anything',
              'https://instagram.com/': 'Page not found • Instagram',
              'https://tiktok.com/@': " TikTok | Watch 's Newest TikTok Videos"
              }
    sites = []
    browser = await launch({"headless":True,"slowMo":1,"devtools":False})
    for key, value in source.items():
        url = key + username
        page = await browser.newPage()
        await page.goto(url)
        element = await page.querySelector('title')
        title = await page.evaluate('(element) => element.textContent', element)
        print(title)
        if value !=title and value != 'github.com':
            sites.append(url)
    diction = dict.fromkeys('1', sites)
    print(diction)
    with open ('my.json', 'w') as file:
        json.dump(diction, file, indent=1)
    await browser.close() 

asyncio.get_event_loop().run_until_complete(main())

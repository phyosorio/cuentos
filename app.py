# Aplicación principal
from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import async_timeout
import time
from pages.all_tales_page import AllTalesPage
from pages.all_epoc_page import AllEpocPage
import nest_asyncio



page_content = requests.get('https://editorialorsai.com/category/epocas/').content

page = AllEpocPage(page_content)

epoc = page.epoc

page_content = requests.get('https://editorialorsai.com/category/epocas/2004/').content

page = AllTalesPage(page_content)
nest_asyncio.apply()
loop = asyncio.get_event_loop()
tales = page.tales



async def fetch_page(session, url):
	page_start = time.time()
	async with async_timeout.timeout(10):
		async with session.get(url) as response:
			print(f'Page took {time.time()-page_start}')
			return await response.text()
        
async def get_multiple_pages(loop, *urls):
	tasks = []
	async with aiohttp.ClientSession(loop = loop) as session:
		for url in urls:
			tasks.append(fetch_page(session, url))
		grouped_tasks =  asyncio.gather(*tasks)
		return await grouped_tasks

urls = [f'https://editorialorsai.com/category/epocas/{page_num+1}/' for page_num in range(epoc[0].year,epoc[-1].year)]        

start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop,*urls))
print(f'Total page requests took {time.time()-start}')

for page_content in pages:
	page = AllTalesPage(page_content)
	tales.extend(page.tales)







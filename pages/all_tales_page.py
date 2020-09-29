# all_books_page

import re
from bs4 import BeautifulSoup
from locators.all_tales_page import AllTalesPageLocators
from parsers.tales_parser import TaleParser

class AllTalesPage:
	def __init__(self, page_content):
		

		self.soup = BeautifulSoup(page_content, 'html.parser')

	
	@property
	def tales(self):
		x =  [TaleParser(e) for e in self.soup.select(AllTalesPageLocators.TALES)]		
		return x

		

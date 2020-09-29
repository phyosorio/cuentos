# all_books_page

import re
from bs4 import BeautifulSoup
from locators.all_epoc_page import AllEpocPageLocators
from parsers.epoc_parser import EpocParser

class AllEpocPage:
	def __init__(self, page_content):
		self.soup = BeautifulSoup(page_content, 'html.parser')

	
	@property
	def epoc(self):
		x =  [EpocParser(e) for e in self.soup.select(AllEpocPageLocators.EPOC)]		
		return x

		

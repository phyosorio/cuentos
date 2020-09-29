# Book_parser

from locators.tales_locators import TaleLocator
import re

class TaleParser:
	def __init__(self, parent):
		self.parent = parent
    
	def __repr__(self):
		return f'Titulo: {self.name} \n {self.tale}>'
	
	@property
	def name(self):
		locator = TaleLocator.NAME_LOCATOR
		item_name = self.parent.select_one(locator).string
		return item_name

	@property
	def tale(self):
		locator = TaleLocator.TEXT_LOCATOR
		item_text = self.parent.select_one(locator).string
		return item_text

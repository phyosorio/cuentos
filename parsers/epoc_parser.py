# Book_parser

from locators.epoc_locators import EpocLocator
import re

class EpocParser:
	def __init__(self, parent):
		self.parent = parent
    
	def __repr__(self):
		return f'año: {self.year}>'
	
	@property
	def year(self):
		locator = EpocLocator.EPOC_LOCATOR
		item_name = self.parent.select_one(locator).string
		pattern = 'Año\s([0-9][0-9][0-9][0-9])'
		matcher = re.search(pattern, item_name)
		return int(matcher.group(1))

	

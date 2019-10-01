
from engage_scraper.scraper_logics.santamonica_scraper_logic import SantaMonicaScraper

import config


"""
Input: Soup, meeting id

"""
def parse_agenda_item(soup, meet_id):
	a = SantaMonicaScraper(committee="Santa Monica City Council")
	return a._process_agenda(soup, meet_id)

 
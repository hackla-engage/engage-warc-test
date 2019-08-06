
from engage_scraper.scraper_logics.santamonica_scraper_models import AgendaItem 
from engage_scraper.scraper_logics.santamonica_scraper_logic import SantaMonicaScraper

import config


"""
Input: Soup, meeting id

"""
def parse_agenda_item(soup, meet_id):
	return SantaMonicaScraper._process_agenda(soup, meet_id)
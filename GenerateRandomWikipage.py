import WikipediaScraper
import webbrowser as wb

url = "https://sv.wikipedia.org/wiki/Portal:Huvudsida"
domain = "https://sv.wikipedia.org"

new_link = WikipediaScraper.getRandomWikipediaPage( url, domain )
wb.open(new_link)
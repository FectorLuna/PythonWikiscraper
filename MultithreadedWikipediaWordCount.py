import WikipediaScraper as wikiscrap
import threading as thread
import concurrent.futures

url = "https://sv.wikipedia.org/wiki/Portal:Huvudsida"
domain = "https://sv.wikipedia.org"
decode = "utf-8"

word_to_count = "han"
frequency = 0
nbb_of_pages_searched = 0

limit = 1

# Fat conclusion: This was a shit idea and is not practical what so ever 


def wordCounter(html, word):
    curr_index = 0
    curr_html = str.upper(html) 
    frequence = 0

    while(curr_html.find(word) != -1):
        curr_index = curr_html.find(str.upper(word)) + len(word)
        frequence += 1
        curr_html = curr_html[curr_index: ]

    return frequence

def wordSearcher( word, url , recursive_steps, limit ):
    html = wikiscrap.openURL( url )

    nbr_of_words_found = wordCounter(html, word)

    if (recursive_steps < limit ):

        url_list = wikiscrap.gatherURL( html, ["we do not care"])
        threadPool = concurrent.futures.ThreadPoolExecutor(max_workers=len(url_list[0])-1)

        for l in url_list[0]:
            l = "https://sv.wikipedia.org" + l
            f_hold = threadPool.submit(wordSearcher, word, l, recursive_steps+1, limit )
            nbr_of_words_found += f_hold.result()

    else:
        return nbr_of_words_found
    return nbr_of_words_found

frequency = wordSearcher(word_to_count, url, 0, limit)
print(frequency)


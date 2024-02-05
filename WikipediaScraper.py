from urllib.request import urlopen
import random as r
import webbrowser as wb

decode = "utf-8"

# Opens url
# Returns: The entire HTML as string-format
#
def openURL(url):

    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    
    return html

# Takes HTML-link and returns array
# Return: [ url_list , nbr_of_url ]
# url_list: List of all URL contained in the website
# nbr_of_url: Total number of URL on the webpage
#
def gatherURL( html ,no_going_back ):

    index = 0
    i_prev = 0
    nbr_of_instances = 0

    forbidden_tags = ["wikimedia", "/Wikipedia", "wikie/Special", ".org", ".com", "=Portal",
                   "/Portal", "/Special:", "/Kategori", "<html ", ".jpg", ".png", "index.php?",
                   "cite_ref-", "cite_note-", "#", ".gif", ".svg", "/Mall:", ".JPG", ".PNG",
                   "Diskussion:", "_(enhet)", "Hj%C3%A4lp"]

    urlList = []

    while (i_prev <= index):

        i_prev = index
        start_index = html.find("<a href=\"" , index) + len("<a href=\"")
        stop_index = html.find("\"" , start_index) 
        index = stop_index

        curr_url = html[start_index: (stop_index) ]

        prohib_check = False

        for prohib in forbidden_tags:

            if ( curr_url.find(prohib) != -1 ):  
                prohib_check = True
                break

        for noback in no_going_back:
            
            if ( curr_url.find(noback) != -1 ):
                prohib_check = True
                break
        
        if ( prohib_check == False ):
            urlList.append( curr_url )
            nbr_of_instances += 1
        
    
    return [ urlList , nbr_of_instances]

# Selects random url in array and returns
# Input: [ domain, list_of_url ]
# Domain: Webside currently being scraped
# list_of_url: Array of currently found url
#
def selectRandomURL( domain, list_of_url ):

    new_url = list_of_url[0][ r.randint(1, list_of_url[1] - 1) ]

    new_url = domain + new_url

    return new_url

# Uses wikipedia to semi-randomly generate and returns this url
# Returns: Link pointing to wikipedia
#
#
#
def getRandomWikipediaPage( start_url, domain ):
    
    curr_url = start_url
    print("Generating link: Please wait a few seconds...")
    no_going_back = []

    for i in range( 5, 6 + r.randint(0,20) ):
        no_going_back.append( curr_url[24:] )
        html = openURL( curr_url )
        list_of_url = gatherURL( html , no_going_back )
        curr_url = selectRandomURL( domain, list_of_url )
        
    
    return curr_url

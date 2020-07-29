from bs4 import BeautifulSoup
import requests

def getix(url):
    document = {}
    try:
        print (url)
        keywords = []
        page2 = requests.get(url, "lxml" )
        print (page2.text)
        if "Es ist ein Fehler aufgetreten" in page2.text:
            return None
        if "An error has occurred" in page2.text:
            return None
        soup2 = BeautifulSoup(page2.text)
        trs = soup2.find_all('tr')
        # title
        tags = soup2.find_all('h3')
        for t in tags:
            if t.attrs['property'] == "name":
                document['title'] = t.text
        # other stuff
        for tr in soup2.find_all('tr'):
            for th in  tr.find('th'):
                #print ("..>"+th)
                if "Author" in th:
                    document['author'] = []
                    for td in tr.find('td'):
                        document['author'].append (td.text.strip())
                if "Published:" in th:
                    for td in tr.find('td'):
                        for span in tr.findAll('span', {"property":True}):
                            if "property" in span.attrs:
                                if span.attrs['property']=="location":
                                    document['location'] = span.text.strip()
                                if span.attrs['property']=="name":
                                    document['publisher-name'] = span.text.strip()
                                if span.attrs['property']=="datePublished":
                                    document['datePublished'] = span.text.strip()
        # Keyword
        for a in soup2.find_all('a', href=True):
            if a['href'].strip().endswith ('type=Subject'):
                keywords.append(a.text)
        document['keywords'] = keywords
    except Exception as e:
        if not options.verbose:
           print( "Exception in IXTheo:" +str(e))
    #print (str(document))
    return document

def getixuri(q):
    try:
        payload = {'lookfor': q, 'type': 'AllFields', 'limit':20}
        page_text = requests.get('https://ixtheo.de/Search/Results', params=payload)
        #print (" --> "+page_text.text)
        soup = BeautifulSoup(page_text.text)
        url = ''
        for a in soup.find_all('a', href=True):
            #print ("Found the URL:", a['href'])
            if a['href'].strip().startswith ('/Record'):
                url = a['href']
                return url
    except Exception as e:
        if not options.verbose:
            print( "Exception in IXTheo:" +str(e))
    return ""

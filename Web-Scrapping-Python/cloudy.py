from requests_html import HTMLSession

s = HTMLSession()

regions = ['Dakar', 'Diourbel', 'Fatick', 'Kaolack', 'Kolda', 'Louga', 'Matam', 'St Louis', 'Tambacounda', 'Thiès', 'Ziguinchor', 'Kaffrine', 'Kédougou', 'Sédhiou']

for region in regions:
    query = region
    url = f'https://www.google.com/search?q=weather+{query}'

    r = s.get(url, headers={'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})

    temp = r.html.find('span#wob_tm', first=True).text

    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text

    desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

    print(f"La température à {query} est de {temp}{unit} : {desc}")
    
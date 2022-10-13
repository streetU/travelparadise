from bs4 import BeautifulSoup as bs
from urllib import request
import re
import pandas as pd

print("Fetching Data of Different Airports...")

# # Adding top 100 airports in the world
# page = request.urlopen("https://gettocenter.com/airports/top-100-airports-in-world")
# soup = bs(page, features="html.parser")

column_names = ['city','airport','code','country']
df = pd.DataFrame(columns=column_names)

# tr = soup.body.find_all('tr')

# for r in tr:
#     d = r.find_all('td')
#     airport = d[1].text.strip()
#     code = d[2].text.strip().upper()
#     city = d[3].text.strip()
#     country = d[4].text.strip()
    
#     row = {
#         'city': city,
#         'airport': airport,
#         'code': code,
#         'country': country
#     }
#     df = df.append(row, ignore_index=True)


# Adding top 30 airports in india
pages = [ 
        request.urlopen("https://www.worlddata.info/europe/france/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/united-kingdom/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/germany/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/netherlands/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/switzerland/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/belgium/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/ireland/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/norway/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/denmark/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/finland/airports.php"),
        request.urlopen("https://www.worlddata.info/europe/sweden/airports.php")
        ]

for page in pages:
    print(page)
    soup = bs(page, features="html.parser")

    tr = soup.body.find_all('table')[0].find_all('tr')

    for r in tr[1:]:
        d = r.find_all('td')
        airport = d[1].text.strip()
        code = d[0].text.strip().upper()
        city = d[2].text.strip()
        country = 'India'
        
        row = {
            'city': city,
            'airport': airport,
            'code': code,
            'country': country
        }
        if len(df[df['code'] == code]):
            continue
        else:
            df = df.append(row, ignore_index=True)

print("Saving data in the file airports.csv")
df.to_csv("airports.csv", index=False)

print("DONE")

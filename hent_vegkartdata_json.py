import requests
import json
import pandas as pd
import csv

url = "https://nvdbapiles-v3.atlas.vegvesen.no/vegobjekter/915?segmentering=true&egenskap=(11278%3D19031)%20AND%20(11278%3D19031)%20AND%20(11276%3D19024%20OR%2011276%3D19025%20OR%2011276%3D19026)&kartutsnitt=-677309.17%2C6219847.976%2C2492617.17%2C8243724.024&inkluder=alle"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    rows = []
    for obj in data['objekter']:
        wkt = obj['geometri']['wkt']
        type_veg = obj['vegsegmenter'][0]['typeVeg_sosi']
        veg_kat = None
        veg_nummer = None
        for e in obj['egenskaper']:
            if e['id'] == 11276:  # Vegkategori
                veg_kat = e['verdi']
            elif e['id'] == 11277:  # Vegnummer
                veg_nummer = e['verdi']
        if veg_kat is not None and ('Europaveg' in veg_kat or 'Riksveg' in veg_kat or 'Fylkesveg' in veg_kat):
            rows.append((wkt, type_veg, veg_kat, veg_nummer))

    df = pd.DataFrame(rows, columns=['WKT', 'typeVeg', 'Kategori', 'Vegnummer'])
    df.to_csv('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_json.csv', index=False, quoting=csv.QUOTE_ALL, escapechar='\\')
else:
    print("Request failed with status code:", response.status_code)




































# import requests
# import json
# import pandas as pd
# import csv

# url = "https://nvdbapiles-v3.atlas.vegvesen.no/vegobjekter/915?segmentering=true&egenskap=(11278%3D19031)%20AND%20(11278%3D19031)%20AND%20(11276%3D19024%20OR%2011276%3D19025%20OR%2011276%3D19026)&kartutsnitt=-677309.17%2C6219847.976%2C2492617.17%2C8243724.024&inkluder=alle"

# response = requests.get(url)

# if response.status_code == 200:
#     data = json.loads(response.text)
#     rows = []
#     for obj in data['objekter']:
#         wkt = obj['geometri']['wkt']
#         type_veg = obj['vegsegmenter'][0]['typeVeg_sosi']
#         veg_kat = None
#         for e in obj['egenskaper']:
#             if e['id'] == 11276:  # Vegkategori
#                 veg_kat = e['verdi']
#                 break
#         if veg_kat is not None and ('Europaveg' in veg_kat or 'Riksveg' in veg_kat or 'Fylkesveg' in veg_kat):
#             rows.append((wkt, type_veg, veg_kat))

#     df = pd.DataFrame(rows, columns=['WKT', 'typeVeg', 'Kategori'])
#     df.to_csv('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/data_json.csv', index=False, quoting=csv.QUOTE_ALL, escapechar='\\')
# else:
#     print("Request failed with status code:", response.status_code)

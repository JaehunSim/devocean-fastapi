import requests
import warnings

warnings.filterwarnings("ignore")


def get_total_time(start_poi, end_poi, app_key):
    # app_key: https://openapi.sk.com/ 발급받으세요~
    url = f'https://apis.openapi.sk.com/tmap/routes?version=1&appKey={app_key}'
    data = {
        'startX': start_poi['longitude'],
        'startY': start_poi['latitude'],
        'endX': end_poi['longitude'],
        'endY': end_poi['latitude'] 
    }
    response = requests.post(url, json=data, verify=False)
    result = response.json()
    total_time = result['features'][0]['properties']['totalTime']
    return total_time

def get_poi_by_keyword(keyword, app_key):
    """
    poi: points of interest
    app_key: https://openapi.sk.com/ 발급받으세요~
    """
    url = f'https://apis.openapi.sk.com/tmap/pois?version=1&appKey={app_key}&searchKeyword={keyword}'
    response = requests.get(url, verify=False)
    result = response.json()
    first_poi = result['searchPoiInfo']['pois']['poi'][0]
    latitude = first_poi['noorLat']
    longitude = first_poi['noorLon']
    name = first_poi['name']
    poi = {
        'latitude': latitude,
        'longitude': longitude,
        'name': name
    }
    return poi

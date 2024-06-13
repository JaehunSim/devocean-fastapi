import requests
import warnings

warnings.filterwarnings("ignore")

APP_KEY = 'StB056m47i3XONHfeEYxV1K9il4l9AeW2xePEnjZ' # https://openapi.sk.com/ 발급받으세요~

def get_total_time(start_poi, end_poi):
    url = f'https://apis.openapi.sk.com/tmap/routes?version=1&appKey={APP_KEY}'
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

def get_poi_by_keyword(keyword):
    """
    poi: points of interest
    """
    url = f'https://apis.openapi.sk.com/tmap/pois?version=1&appKey={APP_KEY}&searchKeyword={keyword}'
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

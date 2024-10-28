import requests
import pandas as pd
import numpy as np
from appconfig import KAOHSIUNG_UBIKE_API_URL

def distance_calculate(x1=None, y1=None, x2=None, y2=None):
    try:
        if x1 is None or y1 is None or x2 is None or y2 is None:
            print("There aren't enough locational information~")
            return None
        else:
            absolute_distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2) * 100
            return absolute_distance
    except Exception as ex:
        print(f'!!! distance_calculate function error: {ex}')

def ubikeDataframe():
    try:
        # get ubike data

        response = requests.get(url=KAOHSIUNG_UBIKE_API_URL)
        result = response.json()
        df = pd.DataFrame(result['data']['retVal'])
        df = df[['scity', 'sarea', 'sna', 'ar', 'sbi', 'bemp', 'act', 'mday', 'lng', 'lat']]
        df = df[df['act'] == 1]

        # transform the longitude and latitude into float

        df[['lng', 'lat']] = df[['lng', 'lat']].astype(float)
        df[['sbi', 'bemp']] = df[['sbi', 'bemp']].astype(int)
        df['mday'] = pd.to_datetime(df['mday'], format='%Y%m%d%H%M%S')
        df['mday'] = df['mday'].astype(str)

        return df
    except Exception as ex:
        print(f'!!! ubikeDataframe function error: {ex}')

def ubikeLocation(df:pd.DataFrame, longitude, latitude):
    try:
        # calculate the distance and choose top 3 small values turn it to json

        df['distance'] = distance_calculate(df['lng'], df['lat'], longitude, latitude)
        complete_df = df.sort_values('distance', ascending=True).iloc[:3].reset_index(drop=True)
        complete_df = complete_df[['scity', 'sarea', 'sna', 'ar', 'sbi', 'bemp', 'lng', 'lat', 'mday']]
        json_file = complete_df.to_json(orient='records')
        return json_file
    except Exception as ex:
        print(f'!!! ubikeLocation function error: {ex}')

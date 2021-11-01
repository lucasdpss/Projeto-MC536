from geopy.geocoders import GoogleV3
from geopy.point import Point
from geopy.extra.rate_limiter import RateLimiter
from functools import partial
from tqdm import tqdm
import pandas as pd

tqdm.pandas()

df = pd.read_csv('postos_policiais.csv')
print(df)

geolocator = GoogleV3(user_agent='mc536-os-delegados', api_key='API_KEY')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=3)

df['location'] = df['endereco'].progress_apply(partial(geocode, exactly_one=True, bounds=(Point(-23.348593791977585, -46.974723751446525), Point(-23.783952348971198, -46.24460626887386))))
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)


df[['lat', 'lon', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)

df.to_csv('postos_policiais_geocoded.csv')

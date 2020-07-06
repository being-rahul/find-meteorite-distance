import requests
import math

m=requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
m_data=m.json()

def cal_dist(lat1,lon1,lat2,lon2):
	lat1=math.radians(lat1)
	lon1=math.radians(lon1)
	lat2=math.radians(lat2)
	lon2=math.radians(lon2)

	h=math.sin( (lat2-lat1) /2 )**2 + \
	math.cos(lat1)* \
	math.cos(lat2) * \
	math.sin( (lon2-lon1) /2)**2

	return 6372.8 *2 * math.asin(math.sqrt(h))

# 24.585380, 77.730897   my latitude and longitude
for i in m_data: 
	if not('reclat' in i and 'reclong' in i): continue 
        lat1=float(i['reclat']) 
   	    lon1=float(i['reclong']) 
        lat2=24.585380 
        lon2=77.730897 
        min_dist.append([cal_dist(lat1,lon1,lat2,lon2),i['name']])

min_dist.sort(key = lambda x:x[0])
print(min_dist)
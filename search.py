#Python
import requests
import re

from requests.models import Response




ER_TITULO_VIDEO : str = r'<title>.* - YouTube</title>'

ER_FECHA_SUBIDA : str = r'"dateText":\{"simpleText":".{12}"\}'

ER_NOMBRE_CANAL : str = r'<link itemprop="name" content="[^<]*>'
#&sp=CAM%253D



def search_videos(search_video : str, range_videos : int,top : str='') -> list:
    html : Response = requests.get(f"https://www.youtube.com/results?search_query={search_video}{top}")
    if html.status_code == 200:
        videos_ids : list = re.findall(r'watch\?v=(\S{11})',html.text)
        videos : list = []
        for i in range(range_videos):
            videos.append('https://www.youtube.com/watch?v='+videos_ids[i])
        return videos




def get_info_video(url : str,search_v : str) -> None:
    video : Response = requests.get(url)
    if video.status_code == 200:
        video_owner : str = re.findall(ER_NOMBRE_CANAL,video.text)[0]
        video_title : str = re.findall(ER_TITULO_VIDEO,video.text)[0]

        try:
            video_date : str = re.findall(ER_FECHA_SUBIDA,video.text)[0]
            video_date : str = re.sub('"dateText":{"simpleText":"','',video_date)
            video_date : str = re.sub('"}','',video_date)
        except IndexError:
            video_date : str = 'N/A'

        video_title : str = re.sub(r'<title>','',video_title)
        video_title : str = re.sub(r' - YouTube</title>','',video_title)

        video_owner : str = re.sub('<link itemprop="name" content="','',video_owner)
        video_owner : str = re.sub('">','',video_owner)

        info_video : str = f'{video_title}\n{url}\nDe: {video_owner} - Subido el {video_date}\n\n'
        with open(f'{search_v}.txt',mode='a',encoding='utf-8') as file:
            file.write(info_video)




def format_search(search_v) -> str:
    new_search : str = search_v.lower()
    new_search : str = new_search.replace(' ','+')
    return new_search




def start(title_video, range_videos) -> None:
    if re.match(r'[\s]+',title_video) or len(title_video) == 0:
        print('Está vacío')
    else:
        search_v : str = format_search(title_video)
        url_videos : list = search_videos(search_v, range_videos)
        for i in range(range_videos):
            get_info_video(url_videos[i],search_v)
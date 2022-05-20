import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def video_id(url):
    pattern_watch = 'https://www.youtube.com/watch?'
    pattern_short = 'https://youtu.be/'

    if re.match(pattern_watch, url):
        yturl_qs = urlparse(url).query
        vid = parse_qs(yturl_qs)['v'][0]
    elif re.match(pattern_short, url):
        vid = url[17:28]
    else:
        print('error:\n URL is\"https://www.youtube.com/watch?\"Or')
        print('  \"https://youtu.be/\"Please specify the URL that starts with.')
        print(f'Item:{url}')
        vid = ''
    return vid


def video_subtitles(video_id):
    transcript_lst = YouTubeTranscriptApi.get_transcript(video_id)
    texts = ''
    for trans_dict in transcript_lst:
        texts += trans_dict['text'] + ' '
    return texts


def custom_subtitles(video_id):
    subtitle_lst = YouTubeTranscriptApi.get_transcript(video_id)
    for subtitle in subtitle_lst:
        time = subtitle['start']
        if time >= 60.0:
            minutes = round(time / 60, 2)
            min, sec = str(minutes).split('.')
            sec = int(sec)
            min = int(min)
            if sec >= 60:
                sec = sec - 60
                min += 1
        else:
            seconds = str(round(time))
            min, sec = '0', seconds
        start_time = f'{str(min).zfill(2)}:{str(sec).zfill(2)}'
        subtitle['start'] = start_time
    return subtitle_lst

    


if __name__ == '__main__':
    url = 'https://youtu.be/SW14tOda_kI'
    id = video_id(url)
    # print(video_subtitles(id))
    print(video_subtitles(id))

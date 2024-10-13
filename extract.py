import os
import csv
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import isodate


api_key = "AIzaSyAYAQ0nFjYdovNMylXuLc5QzYsxtut1leA" # here replace with your api key
youtube = build("youtube", "v3", developerKey=api_key)


def get_video_ids_from_channel(channel_id):
    video_ids = []
    next_page_token = None

    while True:
        try:
            request = youtube.search().list(
                part="id",
                channelId=channel_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()

            
            for item in response['items']:
                if item['id']['kind'] == 'youtube#video':
                    video_ids.append(item['id']['videoId'])

            
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        except HttpError as err:
            print(f"An error occurred: {err}")
            break

    return video_ids


def get_video_details(video_ids):
    video_details = []

    for i in range(0, len(video_ids), 50):
        batch_video_ids = video_ids[i:i+50]
        try:
            request = youtube.videos().list(
                part="snippet,statistics,contentDetails",
                id=','.join(batch_video_ids)
            )
            response = request.execute()

            
            for item in response['items']:
                video_info = {
                    'title': item['snippet']['title'],
                    'video_id': item['id'],
                    'views': item['statistics'].get('viewCount', 0),
                    'likes': item['statistics'].get('likeCount', 0),
                    'dislikes': item['statistics'].get('dislikeCount', 0),
                    'duration': item['contentDetails']['duration'],
                }

                
                video_info['duration_seconds'] = isodate.parse_duration(video_info['duration']).total_seconds()

                video_details.append(video_info)

        except HttpError as err:
            print(f"An error occurred: {err}")
            continue

    return video_details


def display_video_details(video_details):
    for video in video_details:
        print(f"Title: {video['title']}")
        print(f"Video ID: {video['video_id']}")
        print(f"Views: {video['views']}")
        print(f"Likes: {video['likes']}")
        print(f"Dislikes: {video['dislikes']}")
        print(f"Duration (in seconds): {video['duration_seconds']}")
        print("-" * 50)


def save_to_csv(video_details, filename="video_details.csv"):
    headers = ['title', 'video_id', 'views', 'likes', 'dislikes', 'duration_seconds', 'duration']  

    try:
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(video_details)
        print(f"Data has been saved to {file_path}")
    except Exception as e:
        print(f"Error saving CSV: {e}")


def save_to_json(video_details, filename="video_details.json"):
    try:
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(video_details, file, indent=4)
        print(f"Data has been saved to {file_path}")
    except Exception as e:
        print(f"Error saving JSON: {e}")


def main(channel_id):
    video_ids = get_video_ids_from_channel(channel_id)
    print(f"Found {len(video_ids)} videos.")

    video_details = get_video_details(video_ids)
    display_video_details(video_details)

    save_to_csv(video_details)
    save_to_json(video_details)

channel_id = "UCh9nVJoWXmFb7sLApWGcLPQ" # give the channel id of the youtube channel you want to analyse or extract data 
main(channel_id)

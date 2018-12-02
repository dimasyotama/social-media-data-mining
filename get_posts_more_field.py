#important to know that this file only mining your post not your friend post !!!!!!!!


import os
import json
import facebook
import requests
if __name__ == '__main__':
    token = os.environ.get('#FACEBOOK TOKEN API') #to get a facebook TOKEN API
    graph = facebook.GraphAPI(token)
    all_fields = [
                    'message',
                    'created_time',
                    'description',
                    'caption',
                    'link',
                    'place',
                    'status_type'
                    ]  # to create json with some of field on your post
    all_fields = ','.join(all_fields)
    #to combine all of the field into a json file
    posts = graph.get_connections('me', 'posts', fields=all_fields) #to get connections from your post
    while True: # keep paginating
        try:
            with open('my_posts.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                    # get next page
                    posts = requests.get(posts['paging']['next']).json()
        except KeyError:
        # no more pages, break the loop
            break

#This file to visualize data from json into a bar chart


import json
from argparse import ArgumentParser
import dateutil.parser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--file','-f',required=True,help='The .jsonl file with all the posts') #open json file with some argument on your terminal
    return parser
if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    with open(args.file) as f:
        posts = []
        for line in f:
            post = json.loads(line)
            created_time = dateutil.parser.parse(post['created_time'])
            posts.append(created_time.strftime('%H:%M:%S'))
        ones = np.ones(len(posts))
        idx = pd.DatetimeIndex(posts)
        # the actual series (a series of 1s for the moment)
        my_series = pd.Series(ones, index=idx)
        # Resampling into 1-hour buckets
        per_hour = my_series.resample('1H', how='sum').fillna(0) #set data visualization per 1 hour
        # Plotting
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.set_title("My Post Account Frequencies")
        width = 0.8
        ind = np.arange(len(per_hour))
        plt.bar(ind, per_hour)
        tick_pos = ind + width / 2
        labels = []
        for i in range(24): #Date time recognition
            d = datetime.now().replace(hour=i, minute=0)
            labels.append(d.strftime('%H:%M'))
        plt.xticks(tick_pos, labels, rotation=90)
        plt.savefig('posts_per_hour1.png') #save the data visualization
import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    video_data = []
    with open('USvideos.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                video_data.append(vid_dict)
    return video_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


def my_max(dictionary, quantity):
    my_top = {quantity: 0, 'channel': None}

    for k, v in dictionary.items():
        if int(v) > my_top[quantity]:
            my_top['channel'] = k
            my_top[quantity] = int(v)
    return my_top


def my_min(dictionary):
    my_bottom = {'num_views': float('Inf'), 'channel': None}

    for k, v in dictionary.items():
        if int(v) < my_bottom['num_views']:
            my_bottom['channel'] = k
            my_bottom['num_views'] = int(v)
    return my_bottom


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': None,
                                              'least_pop_num_views': None}

    channels = {}

    for item in data[1:]:

        channels.setdefault(item['channel_title'], 0)
        channels[item['channel_title']] += int(item['views'])

    most_popular_channel = my_max(channels, 'num_views')
    least_popular_channel = my_min(channels)

    most_popular_and_least_popular_channel['most_popular_channel'] = most_popular_channel['channel']
    most_popular_and_least_popular_channel['least_popular_channel'] = least_popular_channel['channel']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_popular_channel['num_views']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_popular_channel['num_views']

    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}
    channels = {}
    for item in data[1:]:
        channels.setdefault(item['channel_title'], 0)
        channels[item['channel_title']] += int(item['likes'])
        channels[item['channel_title']] += int(item['dislikes'])

    liked_channel = my_max(channels, 'likes')
    disliked_channel = my_max(channels, 'dislikes')

    most_liked_and_disliked_channel['most_liked_channel'] = liked_channel['channel']
    most_liked_and_disliked_channel['num_likes'] = liked_channel['likes']
    most_liked_and_disliked_channel['most_disliked_channel'] = disliked_channel['channel']
    most_liked_and_disliked_channel['num_dislikes'] = disliked_channel['dislikes']

    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    #print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))

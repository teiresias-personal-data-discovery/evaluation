import pandas as pd
import numpy as np
import json
import re

np.random.seed(84)
number_of_items = 5000

def get_df_via_json(json_path):
    with open(json_path) as file:
        data = json.load(file)
        df = pd.DataFrame(data)
        return df


def store_df_as_csv(df, path, **kwargs):
    suppress_meta = kwargs.get("suppress_meta", False)
    if suppress_meta:
        df.to_csv(path, header=False, index=False)
    else:
        df.to_csv(path)


def get_twitter_names(csv_path):
    with open(csv_path, "rt") as file:
        text = file.read()
        screen_names = re.findall(r"\n\"\d+\", ?\"([^,\n]+?)\"", text)
        return pd.DataFrame({"twitter_name": screen_names}).sample(n=number_of_items)


def get_full_names(df):
    df['full_name'] = df[['firstName', 'lastName']].agg(' '.join, axis=1)
    return df['full_name']


def get_noise_with_labels(labels: list, number_of_entities):
    noise = np.random.randint(123, 99999999, (number_of_entities, len(labels)))
    df = pd.DataFrame(noise, range(number_of_entities), labels)
    return df.applymap(str)


data = {
    "twitter_name":
    lambda twitter_friends: get_twitter_names(twitter_friends),
    "full_name":
    lambda mock_users: get_full_names(get_df_via_json(mock_users)),
    "ipv4":
    lambda mock_users: get_df_via_json(mock_users)['ipv4'],
    "labeled_noise":
    lambda number_of_entities: get_noise_with_labels(['user_name', 'email', 'address', 'ip'], number_of_entities)
}

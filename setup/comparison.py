from utils.preprocess_data import data, store_df_as_csv
from utils.handle_db import create_table_from_df

# ____fill PostgreSQL information
database = ""
user = ""
password = ""
host = ""
port = ""

# generated with ./source_data/mock_user_generator/scr/index.js (utilizing https://github.com/danibram/mocker-data-generator)
mock_users = './source_data/mock_users.json'
# download https://www.kaggle.com/hwassner/TwitterFriends (visited on 2021-08-14)
twitter_friends = './source_data/twitter_friends.csv'


def deploy_experimental_dataset(dataset, table_name):
    return create_table_from_df(f'postgresql://{user}:{password}@{host}:{port}/{database}', table_name, dataset)

def deploy_ipv4_experiment():
    ipv4_dataset = data.get("ipv4")(mock_users)
    ipv4_result = deploy_experimental_dataset(ipv4_dataset, "test1")
    print(f"{ipv4_result = }")
    store_df_as_csv(ipv4_dataset, "datasets/test1.csv")


def deploy_twitter_name_experiment():
    twitter_name_dataset = data.get("twitter_name")(twitter_friends)
    twitter_name_result = deploy_experimental_dataset(twitter_name_dataset, "test2")
    print(f" {twitter_name_result = }")
    store_df_as_csv(twitter_name_dataset, "datasets/test2.csv")


def deploy_full_name_experiment():
    full_name_dataset = data.get("full_name")(mock_users)
    full_name_result = deploy_experimental_dataset(full_name_dataset, "test3")
    print(f"{full_name_result = }")
    store_df_as_csv(full_name_dataset, "datasets/test3.csv")


def deploy_labeled_noise_experiment():
    labeled_noise_dataset = data.get("labeled_noise")(5000)
    labeled_noise_result = deploy_experimental_dataset(labeled_noise_dataset, "test4")
    print(f"{labeled_noise_result = }")
    store_df_as_csv(labeled_noise_dataset, "datasets/test4.csv")


# ____deploy one table per experiment iteration
deploy_ipv4_experiment()
deploy_twitter_name_experiment()
deploy_full_name_experiment()
deploy_labeled_noise_experiment()
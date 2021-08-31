
from utils.preprocess_data import data
from utils.handle_db import create_table_from_df

# ____fill PostgreSQL information
database = ""
user = ""
password = ""
host = ""
port = ""

def deploy_experimental_dataset(dataset, table_name):
    return create_table_from_df(f'postgresql://{user}:{password}@{host}:{port}/{database}', table_name, dataset)

# ____deploy one table per experiment iteration

# labeled_noise_500000_result = deploy_experimental_dataset(data.get("labeled_noise")(500000), "z")
# print(f"{labeled_noise_500000_result = }")

# labeled_noise_50000_result = deploy_experimental_dataset(data.get("labeled_noise")(50000), "y")
# print(f"{labeled_noise_50000_result = }")

# labeled_noise_5000_result = deploy_experimental_dataset(data.get("labeled_noise")(5000), "x")
# print(f"{labeled_noise_5000_result = }")

# labeled_noise_500_result = deploy_experimental_dataset(data.get("labeled_noise")(500), "w")
# print(f"{labeled_noise_500_result = }")
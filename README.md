# Teiresias Evaluation

## Results

## Redeploy Experimental Setups

### ▶ preprocessing of source data

- Twitter Friends Dataset (https://www.kaggle.com/hwassner/TwitterFriends) is too large to be committed.
  - Download it to `setup/source_data/twitter_friends.csv` in order to process it accordingly
- `setup/source_data/mock_users.json` have been generated via Node package _mocker-data-generator_:

  ```
  $ cd setup/source_data/mock_user_generator/
  $ npm i
  $ node ./setup/source_data/mock_user_generator/src/index.js
  ```

### ▶ Prerequisite to the following experiments

- add PostgreSQL storage information to respective python file
- install requirements from requirements.txt

### ▶ Prepare Datasets for Evaluation

```
# stores CSV files and writes data to PostgreSQL tables
$ cd setup
$ python3 comparison.py
```

### ▶ Prepare Datasets for Performance tests

```
# writes data to PostgreSQL tables
$ cd setup
$ python3 performance.py
```

### ▶ Troubleshooting

- symptom: Pandas.df.to_sql() is not terminating
  - reason: firewall is blocking (function has got no handler)

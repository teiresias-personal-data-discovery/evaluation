# Teiresias Evaluation

## Results

- Comparison of the discovery capabilities of _Teiresias_, _AWS Macie_, _Google Cloud Data Loss Prevention_ on 4 datasets. Whereas for _AWS Macie_ and _Google Cloud Data Loss Prevention_ the datasets have been stored as CSV files (`./setup/datasets`) in buckets within their cloud, for _Teiresias_ they have been deployed to tables of a PostgreSQL database.

- Logs, printed during 3 iterations of performance tests of Teiresias - with 500 to 500,000 entities - have been used to calculate the mean duration of the metadata and data analysis.

```
.
├── comparison
│   ├── CloudDataLossPrevention_results
│   ├── Macie_results
│   └── Teiresias_results
└── performance
    ├── 500000_logs.txt
    ├── 50000_logs.txt
    ├── 5000_logs.txt
    └── 500_logs.txt
```

## Redeploy Experimental Setups

### ▶ preprocessing of source data

- Twitter Friends Dataset (https://www.kaggle.com/hwassner/TwitterFriends) is too large to be committed.
  - Download it to `setup/source_data/twitter_friends.csv` in order to process it accordingly
- `setup/source_data/mock_users.json` has been generated via Node package _mocker-data-generator_:

  ```
  $ cd setup/source_data/mock_user_generator/
  $ npm i
  $ node ./setup/source_data/mock_user_generator/src/index.js
  ```

### ▶ Prerequisite to the following experiments

- add PostgreSQL storage information to respective python file
- install Python requirements

### ▶ Prepare Datasets for Evaluation

```
$ cd setup
# uncomment function calls
$ python3 comparison.py
```

### ▶ Prepare Datasets for Performance tests

```
$ cd setup
# uncomment function calls
$ python3 performance.py
```

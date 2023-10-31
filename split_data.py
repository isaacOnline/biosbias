import pickle

import pandas as pd
import numpy as np

with open('BIOS.pkl', 'rb') as f:
    df = pickle.load(f)

df = pd.DataFrame(df)


# Here's their description:
# Because some occupations have a high gender imbalance, our validation and testing splits must be large enough that every gender and occupation are sufficiently represented. We therefore used stratified-by-occupation splits, with 65% of the biographies (258,370) designated for training, 10% (39,635 biographies) designated for validation, and 25% (99,335 biographies) designated for testing.

# I interpreted this as meaning stratifying by occupation, then balancing by gender in the test/val sets. Some
# occupations had gender balances where selecting all of the males (or females) would not result in 10 + 25 = 35% of the
# occupation, in these cases I took the entirety of the smaller gender group for test/val, and sampled the same number
# of the larger gender group to keep the balance.
# I'm a bit confused how De Arteaga et al. did their sampling, since they got a nearly perfect 10/25/65 split, and
# ours is closer to 9/22/69

np.random.seed(701479)
trains, tests, vals = [], [], []
for i, occ_df in df.groupby('title'):
    num_test_val = min(int(len(occ_df) * 0.35), occ_df['gender'].value_counts().min())

    test_val = occ_df.groupby('gender').sample(n = num_test_val // 2, replace=False)
    train = occ_df[~occ_df.index.isin(test_val.index)]

    num_test = int(num_test_val * 0.25 / 0.35)
    test = test_val.groupby('gender').sample(n = num_test // 2, replace=False)
    val = test_val[~test_val.index.isin(test.index)]

    trains.append(train)
    tests.append(test)
    vals.append(val)

train = pd.concat(trains)
test = pd.concat(tests)
val = pd.concat(vals)


train[['start_pos','title',	'URI', 'bio']].to_csv('train.csv', sep='\t', index=False)
test[['start_pos','title',	'URI', 'bio']].to_csv('test.csv', sep='\t', index=False)
val[['start_pos','title',	'URI', 'bio']].to_csv('val.csv', sep='\t', index=False)

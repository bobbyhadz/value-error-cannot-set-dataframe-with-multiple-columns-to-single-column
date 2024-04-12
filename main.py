# Cannot set a DataFrame with multiple columns to single column

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
    'date': ['2023-01-05', '2023-03-25', '2021-01-24']
})

#     name  salary
# 0  Alice   175.1
# 1  Bobby   180.2
# 2   Carl   190.3
print(df[['name', 'salary']])
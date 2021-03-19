import pandas as pd
import sys

assert len(sys.argv) > 1

df = pd.read_csv(sys.argv[1])
print(df)
(df + 1).to_csv('output' + sys.argv[1], index=False)
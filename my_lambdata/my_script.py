
# my_lambdata/my_script.py

import pandas

from my_lambdata.my_mod import enlarge
from my_lambdata.class2 import convert_names

print("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())


print(enlarge(9))



df3 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
full_df3 = convert_names(df3)
print(full_df3.head())

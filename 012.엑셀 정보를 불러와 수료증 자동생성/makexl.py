import pandas as pd
import os

df = pd.DataFrame([["학생1","1990.01.01","0001"],
["학생2","1990.02.02","0002"],
["학생3","1993.01.01","0003"],
["학생4","1994.01.01","0004"]])

print(df)
df.to_excel(r'12.엑셀 정보를 불러와 수료증 자동생성/studentList.xlsx', index=False, header =False)


import pandas as pd
data = {
    '이름':['유정','유나','민지','은지'],
    '나이':[32,28,31,29],
    '생일':['1991.5.2','1993.4.6','1990.9.12','1992.7.19']
    }
df1 = pd.DataFrame(data)
#print(df1)

print(df1.loc[[0,1]])
df1['키'] = [163,180,165,170]
print(df1)
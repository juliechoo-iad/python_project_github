#must remove 'UAE' from line 6 & 15 as the new excel sheet does not have
import pandas as pd
df = pd.read_excel('IMVA.xlsx', sheet_name='IMVA')
df.columns

df2 = df[['Periods', ' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]

new = df2['Periods'].str.split(' ', n = 2, expand = True)
df2= df2.assign(Year=new[1]) # assign a new column named Year with the Year in Periods
df2['Year'] = pd.to_numeric(df2['Year'])
#df3 = df2[(df2['Year'] >= 1988) & (df2['Year'] <= 1997)]
#df3 = df2[(df2['Year'] >= 1998) & (df2['Year'] <= 2007)]
df3 = df2[(df2['Year'] >= 2008) & (df2['Year'] <= 2017)]
df4 = df3[[' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']]
ps = df4.sum().sort_values(ascending=False)
top3countries = ps.head(3)
print(top3countries)
top3countries.index

#plot the figure
import matplotlib.pyplot as plt
import numpy as np
index = np.arange(len(top3countries.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3countries.index, fontsize=6, rotation=30)

#plt.title('Top 3 Asia Countries from (Period:1988-1997)')
#plt.title('Top 3 Asia Countries from (Period:1998-2007)')
plt.title('Top 3 Asia Countries from (Period:2008-2017)')
plt.bar(top3countries.index, top3countries.values/1000)

#plt.savefig("Top3Asia-1988-1997.png")
#plt.savefig("Top3Asia-1998-2007.png")
plt.savefig("Top3Asia-2008-2017.png")
plt.show()
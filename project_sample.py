import pandas as pd

df = pd.read_excel("IMVATransposedT.xlsx", thousands=',' ,skiprows=1)   #remove ',' in thousand
#print(df.dtypes)
#print(df.columns.tolist())  # contain whitespaces in column's name
df.columns = df.columns.str.strip() # remove whitespaces
print('* df.columns:\n',df.columns.tolist())
df2 = df[['Periods', 'Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand',
    'Vietnam', 'Myanmar', 'Japan', 'Hong Kong SAR', 'China', 'Taiwan', 'South Korea', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka',
    'Saudi Arabia', 'Kuwait', 'United Arab Emirates']]
print('* df2 :\n', df2)

new = df2['Periods'].str.split(' ', n = 2, expand = True)#split year and month
print('* new :\n', new)
df2= df2.assign(Year=new[0]) # assign a new column named Year with the Year in Periods
df2['Year'] = pd.to_numeric(df2['Year'])
#print('* df2["Year"] :\n', df2['Year'])

df3 = df2[ (df2['Year'] >=2008) & (df2['Year'] <=2017)]
print('* df3 :\n', df3)

df4 = df3[['Japan', 'Hong Kong SAR', 'China', 'Taiwan', 'South Korea', 'India', 'Pakistan', 'Sri Lanka',
    'Saudi Arabia', 'Kuwait', 'United Arab Emirates']]
print('* df4 :\n', df4)

ps = df4.sum().sort_values(ascending=False)

print('* ps :\n', ps)
ps.index
sum=df4.sum()
print("Total no. of visitors is ", sum)
#plot the figure
import matplotlib.pyplot as plt
import numpy as np
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=8, rotation=20, ha='right')
plt.title('Total Travellers from Countries (Period:2008 - 2007)')
plt.grid()
plt.bar(ps.index, ps.values/1000)
plt.show()
plt.savefig("name.png")
import pandas as pd
import plotly.express as px

df2 = pd.read_csv("CMPSCCapstone/CSV Files/Diversity2.csv")

df2 = df2.groupby(['School','Black'], as_index=False)[['School']].sum()
# df = df.groupby(['School','White']).sum().plot(kind='bar')

df2['Black']=df2['Black'].astype(float)

# df2.plot(kind='bar', x='School', y='Black', figsize=(20,10))
barchart2 = px.bar(
    data_frame=df2,
    x="School",
    y="Black",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')

barchart2.show()
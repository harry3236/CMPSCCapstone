
import pandas as pd
import plotly.express as px

df = pd.read_csv("Diversity2.csv")
df = df.groupby(['School','American Indian'], as_index=False)[['School']].sum()
# df = df.groupby(['School','White']).sum().plot(kind='bar')

df['American Indian']=df['American Indian'].astype(float)

# df.plot(kind='bar', x='School', y='White', figsize=(20,10))
barchart = px.bar(
    data_frame=df,
    x="School",
    y="American Indian",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')


barchart
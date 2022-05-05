
import pandas as pd
import plotly.express as px

df = pd.read_csv("CMPSCCapstone/CSV Files/Diversity2.csv")
df = df.groupby(['School','Hispanic/Latino'], as_index=False)[['School']].sum()
# df = df.groupby(['School','White']).sum().plot(kind='bar')

df['Hispanic/Latino']=df['Hispanic/Latino'].astype(float)

# df.plot(kind='bar', x='School', y='White', figsize=(20,10))
barchart = px.bar(
    data_frame=df,
    x="School",
    y="Hispanic/Latino",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')


barchart.show()
import base64
from PIL import Image
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


OverNormal = 'CMPSCCapstone/DashApp/assets/OverNormalLincolnMap.png'
OverSchool = 'CMPSCCapstone/DashApp/assets/SchoolDistrictOverlay.png'

OverNormalPillng = Image.open(OverNormal)
OverSchoolPilling = Image.open(OverSchool)

resizedSchool = OverSchoolPilling.resize((round(OverSchoolPilling.size[0]*0.25), round(OverSchoolPilling.size[1]*0.25)))
resizedNormal = OverNormalPillng.resize((round(OverNormalPillng.size[0]*0.25), round(OverNormalPillng.size[1]*0.25)))

df = pd.read_csv("CMPSCCapstone/CSV Files/Diversity2.csv")

#Asian Grouping 
dfA = df.groupby(['School','Asian'], as_index=False)[['School']].sum()
dfA['Asian']=dfA['Asian'].astype(float)
barchartA = px.bar(
    data_frame=dfA,
    x="School",
    y="Asian",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')
#Black Grouping
dfB = df.groupby(['School','Black'], as_index=False)[['School']].sum()
dfB['Black']=dfB['Black'].astype(float)
barchartB = px.bar(
    data_frame=dfB,
    x="School",
    y="Black",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')
#American Indian Grouping
dfAI = df.groupby(['School','American Indian'], as_index=False)[['School']].sum()
dfAI['American Indian']=dfAI['American Indian'].astype(float)
barchartAI = px.bar(
    data_frame=dfAI,
    x="School",
    y="American Indian",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')
#Hispanic Grouping
dfH = df.groupby(['School','Hispanic/Latino'], as_index=False)[['School']].sum()
dfH['Hispanic/Latino']=dfH['Hispanic/Latino'].astype(float)
barchartH = px.bar(
    data_frame=dfH,
    x="School",
    y="Hispanic/Latino",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')
#Mixed Grouping 
dfM = df.groupby(['School','Two or More'], as_index=False)[['School']].sum()
dfM['Two or More']=dfM['Two or More'].astype(float)
barchartM = px.bar(
    data_frame=dfM,
    x="School",
    y="Two or More",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')
#Native Hawaiian Grouping
dfNH = df.groupby(['School','Native Hawaiian'], as_index=False)[['School']].sum()
dfNH['Native Hawaiian']=dfNH['Native Hawaiian'].astype(float)
barchartNH = px.bar(
    data_frame=dfNH,
    x="School",
    y="Native Hawaiian",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')
#White Gruping
dfW = df.groupby(['School','White'], as_index=False)[['School']].sum()
dfW['White']=dfW['White'].astype(float)
barchartW = px.bar(
    data_frame=dfW,
    x="School",
    y="White",
    color="School",
    opacity=0.9,
    orientation="v",
    barmode='overlay')





app = Dash(__name__)



app.layout = html.Div([       

html.Div([
    dcc.Dropdown(
        id='dropdown1',
        options=[{'label': 'White', 'value': 'W'} ,
                 {'label': 'American Indian','value': 'AI'}],
        value='W',
        
    ),
  
],
style={'width': '90%', 'display': 'inline-block'}
),

html.Div(id='tablecontainer1'),
html.Div(
    dcc.Graph(
        id='graph1',
        className='dropgraph',
        style={'width':'600px','height':'450px'}
    ),
    style={'display':'inline-block'}
)

],
style={'width': '41%', 'display': 'inline-block'}
)



@app.callback(
Output('graph1', 'figure'), 
[Input('dropdown1', 'value')]
)
#graph plot and styling
def update_graph(value):
    if value=='W':
        data = barchartW
    if value=='AI':
        data = barchartAI
    if value == 'B':
        data = barchartB
    if value == 'A':
        data = barchartA
    if value == 'M':
        data = barchartM
    if value == "NH":
        data = barchartNH
    if value == "H":
        data = barchartH
    return {"data":data}





if __name__ == '__main__':
    app.run_server(debug=True)
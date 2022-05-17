import pandas as pd
import plotly.graph_objects as go
import numpy as np
acceptance_df = pd.read_csv('CollegeAcceptanceScraped.csv', dtype=str)
acceptance_df = acceptance_df.replace('*', 0)
acceptance_df['PercentAcceptance'] = pd.to_numeric(acceptance_df['PercentAcceptance'].str.strip('%'))
acceptance_df = acceptance_df.replace(np.nan, 0)
acceptance_df = acceptance_df.astype({'NumberAcceptance': 'int64', 'ClassYear': 'int64'})

acceptance2017 = acceptance_df.groupby(acceptance_df.ClassYear).get_group(2017)
aa_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('Black or African American')
asian_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('Asian')
native_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('American Indian or Native Alaskan')
white_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('White')
pacific_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('Native Hawaiian or Pacific Islander')
two_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('Two or more races')
latino_acceptance_2017 =acceptance2017.groupby(acceptance2017.Ethnicity).get_group('Hispanic/Latino')

fig2017 = go.Figure(data = [go.Bar(name='Black or African American', 
x = aa_acceptance_2017['SchoolName'], 
y = aa_acceptance_2017['PercentAcceptance']), 
go.Bar(name='Asian', 
x = asian_acceptance_2017['SchoolName'], 
y = asian_acceptance_2017['PercentAcceptance']),
go.Bar(name='American Indian or Native Alaskan', 
x = native_acceptance_2017['SchoolName'], 
y = native_acceptance_2017['PercentAcceptance']), 
go.Bar(name='White', 
x = white_acceptance_2017['SchoolName'], 
y = white_acceptance_2017['PercentAcceptance']),
go.Bar(name='Native Hawaiian or Pacific Islander', 
x = pacific_acceptance_2017['SchoolName'], 
y = pacific_acceptance_2017['PercentAcceptance']),
go.Bar(name='Two or more races', 
x = two_acceptance_2017['SchoolName'], 
y = two_acceptance_2017['PercentAcceptance']),
go.Bar(name='Hispanic/Latino', 
x = latino_acceptance_2017['SchoolName'], 
y = latino_acceptance_2017['PercentAcceptance'])])
fig2017.update_layout(barmode='group', yaxis_range=[0,100], title='2016 College Attendance by Percent', yaxis_title='Percent Attendance')
fig2017.write_html('CollegeAttendance2017.html')
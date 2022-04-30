library(rvest)
library(robotstxt)
library(readr)
library(dplyr)

zipdata<-"http://zipatlas.com/us/ne/lincoln/zip-code-comparison/median-household-income.htm"

lincolndata<-read_html(zipdata)

lincolndata%>%
  html_node("zipcode")%>%
  html_text()

#Now we use the Selector Gadget add-on in Chrome to find nodes for 
#titles, ratings and descriptions

zipcode<-lincolndata%>% 
  html_nodes(".report_data:nth-child(2)")%>%
  html_text()

population<-lincolndata%>%
  html_nodes(".report_data:nth-child(5)")%>%
  html_text()

average_income<-lincolndata%>%
  html_nodes(".report_data:nth-child(6)")%>%
  html_text()

datatable<-data.frame(zipcode,population,average_income,stringsAsFactors = FALSE)
View(datatable)

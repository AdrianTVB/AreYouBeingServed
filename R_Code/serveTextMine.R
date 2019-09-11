# Generate word counts from minutes
source("wordCloud.R")
url <- "http://napier.infocouncil.biz/Open/2019/07/CO_20190711_MIN_398_WEB.htm"

rquery.wordcloud(x=url, type="url")
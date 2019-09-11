# R U Being Served?

[Demonstration Video](https://youtu.be/cOiZJe-g67Y)


[Finished Webpage](https://areyouservingus.azurewebsites.net)

## Problem 
Every few years billboards appear saying “Vote for Me” and representatives for councils and health boards are voted into office, but do they represent us?

How do we know what they are discussing, or even if they attend meetings?

Are they discussing the important emerging topics
- The climate emergency  
- Mental health  
- Water quality and supply  
- Energy availability  

What are they doing to address these?

We could go to a meeting, watch it streamed online, read the minutes, or rely on the news to tell us, but is there a way that technology can help?

## Solution Overview

Meeting schedules and minutes for 2019 were scraped to produce tables of meetings and councillor attendances. The meeting text was also analysed to produce word counts for a set of meetings.

The attendance information was visualised for each organisation, and the word counts turned into word clouds and used for trend analysis of words found in the minutes over time.

Mapping layers from stats have been used to provide the initial landing page and navigation, and councillor photos are used in the attendance visualisation.

## Finished Prototype

Landing Page - select the authority area
![Landing Page](https://github.com/AdrianTVB/arewebeingserved/blob/master/Website%20Snapshots/Landing%20Page(map).PNG)

Attendance visualisation - how many meetings were attended by each councillor
![Attendance Visualisation](https://github.com/AdrianTVB/arewebeingserved/blob/master/Website%20Snapshots/Official%20Attendance.PNG)

Word Cloud - what has been discussed in 2019
![Word Cloud](https://github.com/AdrianTVB/arewebeingserved/blob/master/Website%20Snapshots/napierwordcloud.png)

Interactivie Dashboards - PowerBI Interactive dashboards of the attendance (Note:  Bug with embedded PowerBI iFrame may prevent this showing on the website.

All Napier Council Meetings
![Interactive Dashboards](https://github.com/AdrianTVB/arewebeingserved/blob/master/Website%20Snapshots/BI_Napier_AllCommittees.png)

Audit and Risk Comittee Meeting Attendance
![Interactive Dashboards](https://github.com/AdrianTVB/arewebeingserved/blob/master/Website%20Snapshots/BI_Napier_AuditAndRiskCommittee.png)

Hastings District Council Wastewater Committee
![Interactive Dashboards](https://github.com/AdrianTVB/arewebeingserved/blob/master/Website%20Snapshots/BI_Hastings_WastewaterCommittee.png)

## Outcome

We now have a much better way to get transparency out of those asking for our vote, and the councillors also have a great communication tool for advocating their diligence and reducing distrust.  
The application provides insightful snapshots, allows greater public engagement and understanding, is a resource for journalists, and increases accountability of elected officials.

## Extensions - Not Implemented

Word Count Dashboard - what are the hot topics
![Word Cloud Dashboard](https://github.com/AdrianTVB/arewebeingserved/blob/master/Team%20Planning/HotTopics.png)  
![Word Cloud Dashboard](https://github.com/AdrianTVB/arewebeingserved/blob/master/Team%20Planning/Dashboard.png)  
![Word Cloud Dashboard](https://github.com/AdrianTVB/arewebeingserved/blob/master/Team%20Planning/TimeTrends.png)  

## Further Improvements

Next steps would ideally see us 
- Automating parts of our backend to allow easier onboarding of additional regions and authorities.  
- Natural language processing to allow deeper context and meaning to be derived instead purely of words used. 
- Automated transcripting to improve resolution and reliability of source data.  
- Partnering with interested parties to allow better collection and dissemination of information.  
- Include social issue completion rate to allow evaluation of council effectiveness.  

## Technology Used

The overview of the architecture / data flow is shown in the diagram below.

![Architecture Diagram](https://raw.githubusercontent.com/AdrianTVB/arewebeingserved/master/Team%20Planning/Architecture%20Diagram.png)

Initially Python scraping of the meetings and minutes was investigated, but we reverted to manual scraping and cleaning of the data due to the lack of standardisation of the raw forms, and lack of time.  Csv files were used as an interim step, powerBI was used as a prototyping tool to check the concept.  The full stack was developed in parallel, using an Azure stack consisting of C# ETL from csv into an Azure SQL database which feeds the user interface via a C# Webapp. 

For the concept static Word Clouds were generated using a free online tool and linked to the Webapp.
A PowerBI dashboard has also been linked, and further functionality has been shown using screenshots of a prototype powerBI dashboard. 

## Data Sources

| Name | Description | Url |
| ------------- | ------------- | ------------- |
| NCC Meeting Minutes | Minutes of all Napier City Council meetings. Of particular interest to us is the attendees list of the councillors, and the contents of the full council meetings. | http://napier.infocouncil.biz/ |
| HDC Meeting Minutes | Minutes of all Hastings City Council meetings. Of particular interest to us is the attendees list of the councillors, and the contents of the full council meetings. | http://hastings.infocouncil.biz/ |
| TODO: HBRC Meeting Minutes | Minutes of all Hawkes Bay Regional Council meetings. Of particular interest to us is the attendees list of the councillors. | http://hawkesbay.infocouncil.biz/ |
| TODO: DHB Minutes | Minutes of all District Health Board meetings. Of particular interest to us is the attendees list of the councillors. | |
| Stats NZ Local Authority Boundary Data | The bounding box of area that each local council serves.  | https://datafinder.stats.govt.nz/layer/98755-territorial-authority-2019-generalised/ |
| Stats NZ Regional Council Boundary Data | The bounding box of area that the regional council serves. | https://datafinder.stats.govt.nz/layer/98763-regional-council-2019-generalised/ | 
| Health Board Boundary Data | Not used in this version | |

## Award Categories Entered

### National

 - Innovate New Zealand
 - Combating the Climate Emergency
 - Best Creative Use Of Technology
 - Most Artistic use of data (outside the box)
 - Best Way to Promote Positive Mental Health
 
 ### International

 - Reducing CBD Traffic Congestion
 - Optimise energy and water resource planning
 
## The Transparency Ninja's 
  Team Lead: Jeff Cooke
  
  Team Members: 
  
   - Himalaya Patel
   - Sean Heemeyer
   - Adrian Teding van Berkhout
   - Gabe Ward
   - Kamaljit Singh
   


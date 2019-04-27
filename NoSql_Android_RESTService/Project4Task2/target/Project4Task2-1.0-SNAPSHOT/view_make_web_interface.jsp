<%@page import="edu.cmu.andrew.vaibhavb.model.database.SortStringInt"%>
<%@page import="java.util.Map.Entry"%>
<%@page import="java.util.Iterator"%>
<%@page import="java.util.Date"%>
<%@page import="java.util.TreeSet"%>
<%@page import="java.util.Map"%>
<%@page import="java.util.SortedSet"%>
<%@page import="java.util.SortedSet"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.util.List"%>
<%@page import="edu.cmu.andrew.vaibhavb.model.database.MongoDB"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <style>
            .loggingTable>div:first-child, .topCities>div:first-child{font-weight:bold;}
            .loggingTable>div>div, .topCities>div>div{display:inline-block;vertical-align: middle;width:220px;}
            .loggingTable>div>div:nth-child(2){width:150px;}
            .loggingTable>div>div:nth-child(3){width:80px;}
            .loggingTable>div>div:nth-child(1){width:125px;}
        </style>
        <title>BeerIt</title>
    </head>
    <body>
        <h1>BeerIt Web Interface</h1>
        <%
            //Access the model data returned from the model
            List<MongoDB> listRecords = (ArrayList) request.getAttribute("listRecords");
            List<SortStringInt> sortedSetTopCities  = (ArrayList<SortStringInt>) request.getAttribute("sortedSetTopCities");
            String averageTimeDel = (String) request.getAttribute("averageTimeDel") + " milliseconds";
            String averageTimeAPI = (String) request.getAttribute("averageTimeAPI") + " milliseconds";
            String averageNumOutlets = (String) request.getAttribute("averageNumOutlets");
            String percentSuccessAPI = (String) request.getAttribute("percentSuccessAPI") + "%";
            
            
            //Analytics
            //Top Searched Cities
            StringBuilder topCitiesHtml = new StringBuilder();
            topCitiesHtml.append("<div class=topCities><div><div>City</div><div># times searched</div></div>");
            
            
            String city;
            Integer freq;
            int maxTop = 5;
            int count = sortedSetTopCities.size();
            
            
            for(int i=0; i<Math.min(count, maxTop); i++)
            {                                
                topCitiesHtml.append("<div><div>"
                        + sortedSetTopCities.get(i).key.toString().replaceAll("%20", " ")
                        + "</div><div>"
                        + sortedSetTopCities.get(i).Value
                        + "</div></div>");                
            }
            
            topCitiesHtml.append("</div>");
            
            //Logging
            
            //Create HTML for the records, i.e., logging data
            StringBuilder loggingHtml = new StringBuilder();
            int size = listRecords.size();
            
            loggingHtml.append("<div class=loggingTable>");
            
            //Append the header
            loggingHtml.append("<div>"
                     + "<div>"
                            + "City Queried"
                    + "</div>"
                    + "<div>"
                            + "HTTP Status Code"
                    + "</div>"
                    + "<div>"
                        + "# Outlets"
                    + "</div>"
                    + "<div>"
                        + "Time of Application Used"
                    + "</div>"
                    + "<div>"
                            + "TimeStamp of API Request"
                    + "</div>"
                    + "<div>"
                            + "TimeStamp of API Response"
                    + "</div>"
                    + "<div>"
                            + "Time of Response Dispatch"
                    + "</div>"
                    + "</div>");
            
            //Append the Records
            for(int i = 0; i<size; i++)
            {
                loggingHtml.append("<div>"
                        + "<div>"
                            + listRecords.get(i).getCity().replaceAll("%20", " ")
                        + "</div>"
                        + "<div>"
                            + listRecords.get(i).getHttpStatusCode()
                        + "</div>"
                        + "<div>"
                            + listRecords.get(i).getNumberOfOutlets()
                        + "</div>"
                        + "<div>"
                            + new Date(Long.parseLong(listRecords.get(i).getTimeStampWebServiceHit()))
                        + "</div>"
                        + "<div>"
                            + new Date(Long.parseLong(listRecords.get(i).getTimeStampBeerMappingRequest()))
                        + "</div>"
                        + "<div>"
                            + new Date(Long.parseLong(listRecords.get(i).getTimeStampBeerMappingResponse()))
                        + "</div>"
                        + "<div>"
                            + new Date(Long.parseLong(listRecords.get(i).getTimeStampWebServiceEnd()))
                        + "</div>"
                            + "</div>");
            }

            loggingHtml.append("</div>");
            


            
            
            


        %>
        
        <h2>Analytics</h2>
            <h3>Top Cities Searched (Max = 5)</h3>
            <%=topCitiesHtml.toString()%>
            <hr>
            <h3>Average Time taken to process request</h3>
            <%=averageTimeDel%>
            <hr>
            <h3>Average Time taken by BeerMapping API</h3>
            <%=averageTimeAPI%>
            <hr>
            <h3>Average Number of Outlets Returned by BeerMapping API</h3>
            <%=averageNumOutlets%>
            <hr>
            <h3>Percentage Web Service Hits Successful (HTTP Code = 200)</h3>
            <%=percentSuccessAPI%>
            
            
            
        <!-- Print Logs -->
        <h2>Logs</h2>
        <%=loggingHtml%>
        
        
        
        
    </body>
</html>

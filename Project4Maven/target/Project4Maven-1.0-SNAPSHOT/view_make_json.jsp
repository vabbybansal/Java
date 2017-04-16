<%@page import="edu.cmu.andrew.vaibhavb.model.database.MongoDB"%>
<%@page import="edu.cmu.andrew.vaibhavb.model.database.MongoTemplate"%>
<%@page import="org.json.simple.JSONArray"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.util.List"%>
<%@page import="edu.cmu.andrew.vaibhavb.model.BeerOutlet"%>
<%@page contentType="application/json" pageEncoding="UTF-8"%>
<%!
    //Helper method to stick startIndex to endIndex json objects in a JSON Array
    public JSONArray reJSONifyForOutput(List<BeerOutlet> listOfBeerOutlets) {

        int jsonArraySize = listOfBeerOutlets.size();
        
        //Populate the JSONArray
        JSONArray jsonArrayToSend = new JSONArray();
        for(int i=0; i < jsonArraySize; i++)
        {            
            jsonArrayToSend.add(listOfBeerOutlets.get(i).beerOutletJSONObject);            
        }

        return jsonArrayToSend;
    }

%>
<%

    //Access the requestParameters
    List<BeerOutlet> listOfBeerOutlets = (ArrayList) request.getAttribute("listOfBeerOutlets");
    MongoDB databaseProxyObject = (MongoDB) request.getAttribute("databaseProxyObject");
    
    //JSONify the data list sent from the model
    JSONArray finalJSONArray = reJSONifyForOutput(listOfBeerOutlets);
    String finalJSONOutput = finalJSONArray.toJSONString();

    //Log End of Service
        //Store the HTTP Status                
        databaseProxyObject.setTimeStampWebServiceEnd(Long.toString(System.currentTimeMillis()));


        //Store the database object in the mongoDB
        MongoTemplate.logThisHit(databaseProxyObject);


%>
<%= finalJSONOutput%>

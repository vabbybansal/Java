/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.cmu.andrew.vaibhavb.project4maven;

import edu.cmu.andrew.vaibhavb.model.BeerOutlet;
import edu.cmu.andrew.vaibhavb.model.BeerOutletBusinessLogic;
import edu.cmu.andrew.vaibhavb.model.database.MongoDB;
import edu.cmu.andrew.vaibhavb.model.database.MongoTemplate;
import edu.cmu.andrew.vaibhavb.model.database.SortStringInt;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.SortedSet;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author vabby
 */
@WebServlet(name = "Project4Task2Service", urlPatterns = {"/Project4Task2Service/*", "/Project4Task2Service"})
public class Project4Task2Service extends HttpServlet {
    
    public static MongoDB databaseProxyObject = new MongoDB();
    public static boolean storeInfo = false;
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        
        
        //set the time when this webservice was hit        
        databaseProxyObject.setTimeStampWebServiceHit(System.currentTimeMillis());

        //Initialize storing data as false
        storeInfo = false;
        
        String getQuery = (request.getPathInfo());
        
        boolean getBeerMappingData = true;
        
        //Handle empty query
        if(getQuery == null)
        {
            getBeerMappingData = false;
        }
        else if(getQuery.indexOf("city=") < 0)
        {
            getBeerMappingData = false;
        }
        
        
        if(!getBeerMappingData) //Not a request from the android client (for beer response), therefore request from the interface client
        {
            //Function to do the processing for the display of web analytics dashboard
            requestTypeWebDashboard(request, response);
            
        }
        else //Request from the android client for beer data
        {
            storeInfo = true;
            //Function to fo the processing for returning back the beer data from beermapping API
            requestTypeFetchData(request, response);
            
        }
        
        
    }
    
    private static void requestTypeFetchData(HttpServletRequest request, HttpServletResponse response){
        
        String getQuery = (request.getPathInfo());
//        int indexOfCity = getQuery.indexOf("city=");
        
        //Check if this is a fetch data request or web interface request
        String cityName = getQuery.substring(getQuery.indexOf("city=") + 5); ///////////// UPDATE IN SERVICE 1
        
        
        
        int indexOfSpace;
        //handle spaces in the city name
        if((indexOfSpace = cityName.indexOf(" ")) >=0)
        {
            cityName = cityName.replaceAll(" ", "%20");
        }
        
        //If query is empty
        if(cityName.length() == 0)
            cityName = "";
        
        //Set the cityname for which the webservice was hit
        if(storeInfo)       
            databaseProxyObject.setCity(cityName);
        
        //Set the timeStamp when the beermapping webservice was requested
        if(storeInfo)       
            databaseProxyObject.setTimeStampBeerMappingRequest(System.currentTimeMillis());
        
        //Fetch outlets by the city name
        String beerMappingResponse = BeerOutletBusinessLogic.fetchOutletsByCityName(cityName);

        //Set the timeStamp when the beermapping webservice responded with the data        
        if(storeInfo)                   
            databaseProxyObject.setTimeStampBeerMappingResponse(System.currentTimeMillis());
        
        //Reformat the String API response
        beerMappingResponse = BeerOutletBusinessLogic.reFormatAPIResponse(beerMappingResponse);
        
        //Form a JSON from the API response
        List listOfBeerOutlets = BeerOutletBusinessLogic.objectifyJson(beerMappingResponse);
        
        //Sort the list according to the overall rating in the descending order
        Collections.sort(listOfBeerOutlets);
                              
        //Choose the view in this section
        //Right now we have just one view for the service. It gets the top 10 beer outlets
        //Uses model's subsetBeerOutletsList function for this
        List<BeerOutlet> listOfBeerOutletsFinal = BeerOutlet.subsetBeerOutletsList(listOfBeerOutlets, 0, BeerOutlet.MAX_BEER_OUTLETS);
        
        //Store the # of results from the beermapping API
        if(storeInfo)                   
            databaseProxyObject.setNumberOfOutlets(listOfBeerOutlets.size());
        
        
        
        //Set Response Type
        response.setContentType("application/json;charset=UTF-8");
        
        int status;
        //HTTP Status Codes
        if(listOfBeerOutletsFinal.size() == 0)
        {
            status = 503;        
        }
        else
        {
            status = 200;                         
        }
        response.setStatus(status);

        
        
        //Store the HTTP Status
        if(storeInfo)                   
            databaseProxyObject.setHttpStatusCode(Integer.toString(status));
        
        
        
        //Route to setViewAsJson for sending the model data to JSON, and then send it
        setViewAsJson(request, response, listOfBeerOutletsFinal);

    }
    
    //Set view as JSON (data from external API)
    private static void setViewAsJson(HttpServletRequest request, HttpServletResponse response, List<BeerOutlet> listOfBeerOutlets) {
        
        try {

        //set the request parameters to the jsp
        request.setAttribute("listOfBeerOutlets", listOfBeerOutlets);
        request.setAttribute("databaseProxyObject", databaseProxyObject);

        //Dispatch to the response page
        request.getRequestDispatcher("/view_make_json.jsp").forward(request, response);
        
        } catch (ServletException ex) {
            Logger.getLogger(Project4Task2Service.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Project4Task2Service.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    
    @Override
    public String getServletInfo() {
        
        return "Short description";
    }

    private void requestTypeWebDashboard(HttpServletRequest request, HttpServletResponse response) {
        
        //Calculate the analytics and logging from the model
        List<MongoDB> listRecords = MongoTemplate.fetchDatabase();
        List<SortStringInt> sortedSetTopCities = MongoTemplate.getTopSearchedCities(listRecords);
        long averageTimeDel = MongoTemplate.findAvgTimeWebRequest(listRecords);
        long averageTimeAPI = MongoTemplate.findAvgTimeAPIRequest(listRecords);
        double averageNumOutlets = MongoTemplate.findAvgNumOutlets(listRecords);
        double percentSuccessAPI = MongoTemplate.findPercentageAPISuccess(listRecords);
        
        
        //set the request parameters to the jsp
        request.setAttribute("listRecords", listRecords);
        request.setAttribute("averageTimeDel", Long.toString(averageTimeDel));
        request.setAttribute("averageTimeAPI", Long.toString(averageTimeAPI));
        request.setAttribute("sortedSetTopCities", sortedSetTopCities);        
        request.setAttribute("averageNumOutlets", Double.toString(averageNumOutlets));        
        request.setAttribute("percentSuccessAPI", Double.toString(percentSuccessAPI));        
        
        //Set View
        setViewAsWebInterface(request, response);
        
    }

    
    //Set view as web dashboard
    private void setViewAsWebInterface(HttpServletRequest request, HttpServletResponse response) {
        try {        

        //Dispatch to the response page
        request.getRequestDispatcher("/view_make_web_interface.jsp").forward(request, response);
        
        } catch (ServletException ex) {
            Logger.getLogger(Project4Task2Service.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Project4Task2Service.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    
    


}


package edu.cmu.andrew.vaibhavb;

import edu.cmu.andrew.vaibhavb.model.BeerOutlet;
import edu.cmu.andrew.vaibhavb.model.BeerOutletBusinessLogic;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


@WebServlet(name = "RESTBeerOutletsService", urlPatterns = {"/RESTBeerOutletsService/*"})
public class RESTBeerOutletsService extends HttpServlet {

    

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        
        String getQuery = (request.getPathInfo());
        
        
        String cityName = getQuery.substring(getQuery.indexOf("=")+1);
        
        int indexOfSpace;
        //handle spaces in the city name
        if((indexOfSpace = cityName.indexOf(" ")) >=0)
        {
            cityName = cityName.replaceAll(" ", "%20");
        }
        
        
        
        
        //If query is empty
        if(cityName.length() == 0)
            cityName = "Pittsburgh";
        
        //Fetch outlets by the city name
        String beerMappingResponse = BeerOutletBusinessLogic.fetchOutletsByCityName(cityName);

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
        
        //Set Response Type
        response.setContentType("application/json;charset=UTF-8");
        
        //HTTP Status Codes
        if(listOfBeerOutletsFinal.size() == 0)
        {
            response.setStatus(503);
        }
        else
        {
            response.setStatus(200); 
        }
        
        //Route to setViewAsJson for sending the model data to JSON, and then send it
        setViewAsJson(request, response, listOfBeerOutletsFinal);

    }
    
    
    private static void setViewAsJson(HttpServletRequest request, HttpServletResponse response, List<BeerOutlet> listOfBeerOutlets) {
        
        try {

        //set the request parameters to the jsp
        request.setAttribute("listOfBeerOutlets", listOfBeerOutlets);

        //Dispatch to the response page
        request.getRequestDispatcher("/view_make_json.jsp").forward(request, response);
        
        } catch (ServletException ex) {
            Logger.getLogger(RESTBeerOutletsService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(RESTBeerOutletsService.class.getName()).log(Level.SEVERE, null, ex);
        }

    }

    
    @Override
    public String getServletInfo() {
        
        return "Short description";
    }

    
    

}

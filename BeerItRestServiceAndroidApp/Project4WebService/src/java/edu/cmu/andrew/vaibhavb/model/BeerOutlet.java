
package edu.cmu.andrew.vaibhavb.model;

import java.util.ArrayList;
import java.util.List;
import org.json.simple.JSONObject;

public class BeerOutlet implements Comparable{

    //Declare the number of beer outlets to be sent to the client application. Could be found out using some business logic too
    public static final int MAX_BEER_OUTLETS = 10;
    
    public JSONObject beerOutletJSONObject;

    public BeerOutlet(JSONObject beerOutletJSONObject, String overallRating) {
        this.beerOutletJSONObject = beerOutletJSONObject;
        this.overallRating = overallRating;
    }
    String overallRating;


    @Override
    public int compareTo(Object o) {
        BeerOutlet obj = (BeerOutlet) o;
        double compared = (Double.parseDouble(obj.overallRating) - Double.parseDouble(this.overallRating) );
        if(compared > 0.0)        
            return 1;
        else
            return -1;
    }
    
    //method to subset the arraylist of beeroutlets from any startIndex to any endIndexExclude
    public static List<BeerOutlet> subsetBeerOutletsList(List<BeerOutlet> listOfBeerOutlets, int startIndex, int endIndexExclude){
        
        
        
        List<BeerOutlet> listOfFinalBeerOutlets = new ArrayList<BeerOutlet>();
        
        //Validate the indices
        int beerOutletLen = listOfBeerOutlets.size();
        if(endIndexExclude >= beerOutletLen)
        {
            endIndexExclude = beerOutletLen;
        }
        if(startIndex >= beerOutletLen || startIndex > endIndexExclude)
        {
            startIndex = 0;
            endIndexExclude = 0;
        }
        
        //Iterate and populate
        for(int i=startIndex; i < endIndexExclude; i++)
        {            
            listOfFinalBeerOutlets.add(listOfBeerOutlets.get(i));
        }
        
        return listOfFinalBeerOutlets;
    }
    
}

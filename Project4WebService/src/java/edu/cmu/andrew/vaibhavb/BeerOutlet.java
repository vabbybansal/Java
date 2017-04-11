
package edu.cmu.andrew.vaibhavb;

import org.json.simple.JSONObject;

public class BeerOutlet implements Comparable{

//    String id;
//    String zip;
//    String name;
//    String status;
//    String street;
//    String city;
//    String state;    
//    String country;
//    String phone;
    
    JSONObject beerOutletJSONObject;

    public BeerOutlet(JSONObject beerOutletJSONObject, String overallRating) {
        this.beerOutletJSONObject = beerOutletJSONObject;
        this.overallRating = overallRating;
    }
    String overallRating;
//    String imageCount;
//    String reviewLink;
//    String blogMap;

//    public BeerOutlet(String id, String zip, String name, String status, String street, String city, String state, String country, String phone, String overallRating, String imageCount, String reviewLink, String blogMap) {
//        this.id = id;
//        this.name = name;
//        this.zip = zip;
//        this.status = status;
//        this.street = street;
//        this.city = city;
//        this.state = state;
//        this.country = country;
//        this.phone = phone;
//        this.overallRating = overallRating;
//        this.imageCount = imageCount;
//        this.reviewLink = reviewLink;
//        this.blogMap = blogMap;
//    }
//
//    @Override
//    public String toString() {
//        return "BeerOutlet{" + "id=" + id + ", zip=" + zip + ", name=" + name + ", status=" + status + ", street=" + street + ", city=" + city + ", state=" + state + ", country=" + country + ", phone=" + phone + ", overallRating=" + overallRating + ", imageCount=" + imageCount + ", reviewLink=" + reviewLink + ", blogMap=" + blogMap + '}';
//    }

    @Override
    public int compareTo(Object o) {
        BeerOutlet obj = (BeerOutlet) o;
        double compared = (Double.parseDouble(obj.overallRating) - Double.parseDouble(this.overallRating) );
        if(compared > 0.0)        
            return 1;
        else
            return -1;
    }
    
    
    
}

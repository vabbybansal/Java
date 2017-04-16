/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.cmu.andrew.vaibhavb.model.database;
import java.util.ArrayList;
import java.util.List;
    

 
public class MongoDB {
    
    String timeStampBeerMappingRequest;
    String timeStampBeerMappingResponse;
    String timeStampWebServiceHit;
    String city;
    String httpStatusCode;
    String timeStampWebServiceEnd;
    String numberOfOutlets;

    
    
    

    public MongoDB(String timeStampBeerMappingRequest, String timeStampBeerMappingResponse, String timeStampWebServiceHit, String city, String numberOfOutlets, String httpStatusCode, String timeStampWebServiceEnd) {
        this.timeStampBeerMappingRequest = timeStampBeerMappingRequest;
        this.timeStampBeerMappingResponse = timeStampBeerMappingResponse;
        this.timeStampWebServiceHit = timeStampWebServiceHit;
        this.city = city;        
        this.numberOfOutlets = numberOfOutlets;
        this.httpStatusCode = httpStatusCode;
        this.timeStampWebServiceEnd = timeStampWebServiceEnd;
    }

    
    
    public MongoDB(long timeStampBeerMappingRequest, long timeStampBeerMappingResponse, long timeStampWebServiceHit, String city, int numberOfOutlets, int httpStatusCode, long timeStampWebServiceEnd) {
        this.timeStampBeerMappingRequest = Long.toString(timeStampBeerMappingRequest);
        this.timeStampBeerMappingResponse = Long.toString(timeStampBeerMappingResponse);
        this.timeStampWebServiceHit = Long.toString(timeStampWebServiceHit);
        this.city = city;
        this.httpStatusCode = Integer.toString(httpStatusCode);
        this.timeStampWebServiceEnd = Long.toString(timeStampWebServiceEnd);
        this.numberOfOutlets = Integer.toString(numberOfOutlets);
    }

    @Override
    public String toString() {
        return "MongoDB{" + "timeStampBeerMappingRequest=" + timeStampBeerMappingRequest + ", timeStampBeerMappingResponse=" + timeStampBeerMappingResponse + ", timeStampWebServiceHit=" + timeStampWebServiceHit + ", city=" + city + ", httpStatusCode=" + httpStatusCode + ", timeStampWebServiceEnd=" + timeStampWebServiceEnd + ", numberOfOutlets=" + numberOfOutlets + '}';
    }

    public MongoDB() {
    }
    
    
    
    public String getTimeStampBeerMappingRequest() {
        return timeStampBeerMappingRequest;
    }

    public void setTimeStampBeerMappingRequest(long timeStampBeerMappingRequest) {
        this.timeStampBeerMappingRequest = Long.toString(timeStampBeerMappingRequest);
    }

    public String getTimeStampBeerMappingResponse() {
        return timeStampBeerMappingResponse;
    }

    public void setTimeStampBeerMappingResponse(long timeStampBeerMappingResponse) {
        this.timeStampBeerMappingResponse = Long.toString(timeStampBeerMappingResponse);
    }

    public String getTimeStampWebServiceHit() {
        return timeStampWebServiceHit;
    }

    public void setTimeStampWebServiceHit(long timeStampWebServiceHit) {
        this.timeStampWebServiceHit = Long.toString(timeStampWebServiceHit);
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getHttpStatusCode() {
        return httpStatusCode;
    }

    public void setHttpStatusCode(String httpStatusCode) {
        this.httpStatusCode = httpStatusCode;
    }

    public String getTimeStampWebServiceEnd() {
        return timeStampWebServiceEnd;
    }

    public void setTimeStampWebServiceEnd(String timeStampWebServiceEnd) {
        this.timeStampWebServiceEnd = timeStampWebServiceEnd;
    }

    public String getNumberOfOutlets() {
        return numberOfOutlets;
    }

    public void setNumberOfOutlets(int numberOfOutlets) {
        this.numberOfOutlets = Integer.toString(numberOfOutlets);
    }
    
    
    
    
}

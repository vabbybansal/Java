/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.cmu.andrew.vaibhavb.model.database;
    
    


public class MongoDB {
    
    long timeStampBeerMappingRequest;
    long timeStampBeerMappingResponse;
    long timeStampWebServiceHit;
    String city;
    String mobileManufacturer;
    String mobileModel;
    int numberOfOutlets;

    public long getTimeStampBeerMappingRequest() {
        return timeStampBeerMappingRequest;
    }

    public void setTimeStampBeerMappingRequest(long timeStampBeerMappingRequest) {
        this.timeStampBeerMappingRequest = timeStampBeerMappingRequest;
    }

    public long getTimeStampBeerMappingResponse() {
        return timeStampBeerMappingResponse;
    }

    public void setTimeStampBeerMappingResponse(long timeStampBeerMappingResponse) {
        this.timeStampBeerMappingResponse = timeStampBeerMappingResponse;
    }

    public long getTimeStampWebServiceHit() {
        return timeStampWebServiceHit;
    }

    public void setTimeStampWebServiceHit(long timeStampWebServiceHit) {
        this.timeStampWebServiceHit = timeStampWebServiceHit;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getMobileManufacturer() {
        return mobileManufacturer;
    }

    public void setMobileManufacturer(String mobileManufacturer) {
        this.mobileManufacturer = mobileManufacturer;
    }

    public String getMobileModel() {
        return mobileModel;
    }

    public void setMobileModel(String mobileModel) {
        this.mobileModel = mobileModel;
    }

    public int getNumberOfOutlets() {
        return numberOfOutlets;
    }

    public void setNumberOfOutlets(int numberOfOutlets) {
        this.numberOfOutlets = numberOfOutlets;
    }
    
    
    
    
}

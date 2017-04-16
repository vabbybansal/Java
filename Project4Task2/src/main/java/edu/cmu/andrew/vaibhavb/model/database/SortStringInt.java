/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.cmu.andrew.vaibhavb.model.database;

/**
 *
 * @author vabby
 */
public class SortStringInt implements Comparable{
    
    public String key;
    public Integer Value;

    public SortStringInt(){
        
    }
    
    public SortStringInt(String key, Integer Value) {
        this.key = key;
        this.Value = Value;
    }

    @Override
    public int compareTo(Object o) {
        SortStringInt obj = (SortStringInt) o;
        return obj.Value - this.Value;
    }
    
}

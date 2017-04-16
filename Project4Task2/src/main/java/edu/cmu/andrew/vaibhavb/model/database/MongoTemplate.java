
package edu.cmu.andrew.vaibhavb.model.database;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;
import org.bson.Document;

public class MongoTemplate {
    
    public static void connectToMongo(){
        

//        mongodb://vaibhavbansal:beerit@ds159670.mlab.com:59670/beerit
        MongoClientURI uri  = new MongoClientURI("mongodb://vaibhavbansal:beerit@ds159670.mlab.com:59670/beerit"); 
        MongoClient client = new MongoClient(uri);
        MongoDatabase db = client.getDatabase(uri.getDatabase());
        
        List<Document> seedData = new ArrayList<Document>();

        seedData.add(new Document("decade", "1970s")
            .append("artist", "Debby Boone")
            .append("song", "You Light Up My Life")
            .append("weeksAtOne", 10)
        );


        
        //Fetch the collection
        MongoCollection<Document> songs = db.getCollection("");
        songs.insertMany(seedData);
     
        
        
        client.close();
        
    }

    public static void logThisHit(MongoDB databaseProxyObject) {

//                mongodb://vaibhavbansal:beerit@ds159670.mlab.com:59670/beerit
        MongoClientURI uri  = new MongoClientURI("mongodb://vaibhavbansal:beerit@ds159670.mlab.com:59670/beerit"); 
        MongoClient client = new MongoClient(uri);
        MongoDatabase db = client.getDatabase(uri.getDatabase());
        
        List<Document> seedData = new ArrayList<Document>();

        seedData.add(
            new Document("city", databaseProxyObject.city)
            .append("numberOfOutlets", databaseProxyObject.numberOfOutlets)
            .append("timeStampBeerMappingRequest", databaseProxyObject.timeStampBeerMappingRequest)
            .append("timeStampBeerMappingResponse", databaseProxyObject.timeStampBeerMappingResponse)
            .append("timeStampWebServiceHit", databaseProxyObject.timeStampWebServiceHit)
            .append("timeStampWebServiceEnd", databaseProxyObject.timeStampWebServiceEnd)
            .append("httpStatusCode", databaseProxyObject.httpStatusCode)
        );

        
        //Fetch the collection
        MongoCollection<Document> songs = db.getCollection("interactionlog");
        songs.insertMany(seedData);
     
        
        
        client.close();
        

        
    }
    
    public static List<MongoDB> fetchDatabase(){
        
        List<MongoDB> listReadDB = new ArrayList<MongoDB>();
        
        MongoClientURI uri  = new MongoClientURI("mongodb://vaibhavbansal:beerit@ds159670.mlab.com:59670/beerit"); 
        MongoClient client = new MongoClient(uri);
        MongoDatabase db = client.getDatabase(uri.getDatabase());
        
        //Fetch the collection
        MongoCollection<Document> collection = db.getCollection("interactionlog");
        
        //Inititate the MondoDB constructors and push all the records in the arrayList
        MongoDB readMongoDBRecord;
        Document iterDoc = new Document();
        
//        System.out.println("Printing all records");
        
        //find iterator of the cursor of records associated with this collection (table)
        MongoCursor<Document> cursor = collection.find().iterator();
        try {
            while (cursor.hasNext()) {
                iterDoc = cursor.next();
                String timeStampBeerMappingRequest = iterDoc.get("timeStampBeerMappingRequest").toString();
                String timeStampBeerMappingResponse = iterDoc.get("timeStampBeerMappingResponse").toString();
                String timeStampWebServiceHit = iterDoc.get("timeStampWebServiceHit").toString();
                String city = iterDoc.get("city").toString();
                String numberOfOutlets = iterDoc.get("numberOfOutlets").toString();                
                String httpStatusCode = iterDoc.get("httpStatusCode").toString(); 
                String timeStampWebServiceEnd = iterDoc.get("timeStampWebServiceEnd").toString();
                
                readMongoDBRecord = new MongoDB(timeStampBeerMappingRequest, timeStampBeerMappingResponse, timeStampWebServiceHit, city, numberOfOutlets, httpStatusCode, timeStampWebServiceEnd);
//                System.out.println(readMongoDBRecord);
                listReadDB.add(readMongoDBRecord);
            }
        } finally {
            cursor.close();
        }
     
        return listReadDB;
    }
    
    public static List<SortStringInt> getTopSearchedCities(List<MongoDB> listRecords){
        
        Map<String, Integer> topSearchedCities = new HashMap<String, Integer>();
        int i = 0;
        int size = listRecords.size();
        String city;
        
        for(i = 0; i<size; i++)
        {
            city = listRecords.get(i).city;
            if(topSearchedCities.containsKey(city))
                topSearchedCities.put(city, topSearchedCities.get(city) + 1);
            else
                topSearchedCities.put(city, 1);
        }
        
        List<SortStringInt> listSort = new ArrayList<SortStringInt>();
        SortStringInt tempRec = new SortStringInt();
        //Create List for sorting
//        List<String, Integer> sortedList = new ArrayList<String, Integer>();
        Iterator it = topSearchedCities.entrySet().iterator();
            while (it.hasNext()) {
                Entry<String, Integer> pair = (Entry<String, Integer>) it.next();
                tempRec = new SortStringInt(pair.getKey(), pair.getValue());                
                listSort.add(tempRec);
            }
            Collections.sort(listSort);
        
        
//        SortedSet<Map.Entry<String, Integer>> sortedSet= fetchSortedSetByValDescend(topSearchedCities);
        return listSort;
        
    }


    
    public static long findAvgTimeWebRequest(List<MongoDB> listRecords){
        
        int size = listRecords.size();
        
        //Calculate the total timedelay
        long timeDel = 0;
        for(int i=0; i<size; i++)
        {
            timeDel += Long.parseLong(listRecords.get(i).timeStampWebServiceEnd) - Long.parseLong(listRecords.get(i).timeStampWebServiceHit);
        }
        
        //Calculate average
        timeDel /= size;
        
        return timeDel;
    }
    
    public static long findAvgTimeAPIRequest(List<MongoDB> listRecords){
        
        int size = listRecords.size();
        
        //Calculate the total timedelay
        long timeDel = 0;
        for(int i=0; i<size; i++)
        {
            timeDel += Long.parseLong(listRecords.get(i).timeStampBeerMappingResponse) - Long.parseLong(listRecords.get(i).timeStampBeerMappingRequest);
        }
        
        //Calculate average
        timeDel /= size;
        
        return timeDel;
    }
    
        public static double findAvgNumOutlets(List<MongoDB> listRecords){
        
            int size = listRecords.size();

            //Calculate the total timedelay
            int avgOut = 0;
            for(int i=0; i<size; i++)
            {
                avgOut += Integer.parseInt(listRecords.get(i).numberOfOutlets);
            }

            //Calculate average            
            return ((double) avgOut/size);
        }
        
        
        
        public static double findPercentageAPISuccess(List<MongoDB> listRecords){
        
            int size = listRecords.size();

            //Calculate the total timedelay
            int count = 0;
            for(int i=0; i<size; i++)
            {
                if(Integer.parseInt(listRecords.get(i).httpStatusCode) == 200)
                {
                    count++;
                }
            }

            //Calculate average            
            return ((double) count/size*100);
        }
        
    
}




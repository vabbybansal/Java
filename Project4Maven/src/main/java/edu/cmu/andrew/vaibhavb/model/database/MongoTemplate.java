
package edu.cmu.andrew.vaibhavb.model.database;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import java.util.ArrayList;
import java.util.List;
import org.bson.Document;

public class MongoTemplate {
    
    public static void connectToMongo(){
        
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
        MongoCollection<Document> songs = db.getCollection("interactionlog");
        songs.insertMany(seedData);
     
        
        
        client.close();
        
    }
    
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.cmu.heinz.ds.queuelistener;

import javax.ejb.ActivationConfigProperty;
import javax.ejb.MessageDriven;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageListener;
import javax.jms.TextMessage;

/**
 *
 * @author vabby
 */
@MessageDriven(activationConfig = {
    @ActivationConfigProperty(propertyName = "destinationLookup", propertyValue = "jms/myQueue")
    ,
        @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue")
})
public class MyQueueListener1 implements MessageListener {
    
    public MyQueueListener1() {
    }
    
    @Override
    public void onMessage(Message message) {
        try {
            /*
             * There can be different types of Messages, 
             * so make sure this is the right type.
             */
            if (message instanceof TextMessage) {
                // Cast it to the right type of message
                TextMessage tm = (TextMessage) message;
                // Get the text from the received message
                String tmt = tm.getText();
                System.out.println("MyQueueListener received: " + tmt);
            } else {
                System.out.println("I don't handle messages of this type");
            }
        } catch (JMSException e) {
            System.out.println("JMS Exception thrown" + e);
        } catch (Throwable e) {
            System.out.println("Throwable thrown" + e);
        }
    }
    
}

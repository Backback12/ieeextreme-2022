// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class MyTreat {
	public static void main (String[] args) throws java.lang.Exception {
	    // positive when bought dinner
	    // negative when pay for other dinner
	    
	    Scanner in = new Scanner(System.in);
		HashMap<String, Integer> payments;
		
		int testCases = in.nextInt();
        int temp;
		
		// for each test case
		for(int tests = 0;tests<testCases;tests++){
            payments = new HashMap<String, Integer>();
		    int events = in.nextInt();

		    // for each events
		    for(int event=0;event<events;event++){
    		    String payee = in.next();

    		    if(!payments.containsKey(payee)){ payments.put(payee, Integer.valueOf(0)); }
    		    int paid = in.nextInt();
    		    
                // update payee in payments
                temp = Integer.valueOf(payments.get(payee).intValue() - paid);
                payments.remove(payee);
    		    payments.put(payee, Integer.valueOf(temp));
    		    
    		    // for each person paid for
		        for (int people=0;people<paid;people++){
                    String thePerson = in.next();
		            if(!payments.containsKey(thePerson)){ payments.put(thePerson, Integer.valueOf(0)); }

                    // update person in payments
                    temp = Integer.valueOf(payments.get(thePerson).intValue() + 1);
                    payments.remove(thePerson);
		            payments.put(thePerson, Integer.valueOf(temp));
		        }
		    }
		    
		    // find dinners Needed and days Needed
		    int dinnersNeeded = 0;
		    int daysNeeded = 0;
		    for ( String key : payments.keySet() ) {
		        // if negative, add to dinners needed
                if (payments.get(key).intValue() > 0){
                    dinnersNeeded = dinnersNeeded + payments.get(key).intValue();
                }
                if (payments.get(key).intValue() < daysNeeded){
                    daysNeeded = payments.get(key).intValue();
                }
            }
            
            System.out.println(dinnersNeeded+" "+Math.abs(daysNeeded));
            
            
            
            int i;
		}
		
	}
}
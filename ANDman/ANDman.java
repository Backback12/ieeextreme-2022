// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class ANDman {
	public static void main (String[] args) throws java.lang.Exception {
	    class Node {
            int weight;
            int index;
            ArrayList<Node> branch;
            Node prev;
            
            public Node(int i){
                this.index = i;
                this.branch = new ArrayList<Node>();
            }
        }
	    
	    Scanner in = new Scanner(System.in);
		int testCases = in.nextInt();
		int numNodes;
		ArrayList<Node> allNodes = new ArrayList<Node>();
		
		for(int i=1;i<=testCases;i++){
		    numNodes = in.nextInt();
		    
		    // init all Nodes in allNode arraylist
		    for (int j=1;j<=numNodes;j++){
		        allNodes.add(new Node(j));
		    }
		    
		    // init all Node weights
		    for (int j=0;j<numNodes;j++){
		        allNodes.get(j).weight = in.nextInt();
		    }
		    
		    // init all branches
		    for (int j=0;j<numNodes-1;j++){
		        int nodeA = in.nextInt();
		        int nodeB = in.nextInt();
		        allNodes.get(nodeA - 1).branch.add(allNodes.get(nodeB-1));
		        allNodes.get(nodeB - 1).branch.add(allNodes.get(nodeA-1));
		    }
		    
		    int numInstructions = in.nextInt();
		    int type, u, v;
		    // run instructions
		    for(int j=0;j<numInstructions;j++){
		        type = in.nextInt();
		        u = in.nextInt();
		        v = in.nextInt();
		        
		        if (type == 1){
		            allNodes.get(u-1).weight = v;
		        }
		        else{
		            Node start = allNodes.get(u-1);
		            Node end = allNodes.get(v-1);
		            
		            ArrayList<Node> found, localFound, newLocalFound;
	    
            	    found = new ArrayList<Node>();
            	    localFound = new ArrayList<Node>();
            	    newLocalFound = new ArrayList<Node>();
            	    
            	    int weight = 1;
            	    Node curNode;
            	    
            	    found.add(start);
            	    localFound.add(start);
            	    
            	    while(!found.contains(end)){
            	        // for all nodes found in this net
            	        for(int k=0;k<localFound.size();k++){
            	            // for all connected branches to this node
            	            for(int l=0;l<localFound.get(k).branch.size();l++){
            	                // if it branches to a new node
            	                if (!found.contains(localFound.get(k).branch.get(l))){
            	                    localFound.get(k).branch.get(l).prev = localFound.get(k);
            	                    newLocalFound.add(localFound.get(k).branch.get(l));
            	                    found.add(localFound.get(k).branch.get(l));
            	                }
            	            }
            	            
            	            localFound = newLocalFound;
            	            newLocalFound = new ArrayList<Node>();
            	        }
            	    }
            	    // all prevs are set to connect end to start
            	    curNode = end;
            	    while(curNode != start){
            	        weight = weight*curNode.weight;
            	        weight = weight % 1000000007;
            	        curNode = curNode.prev;
            	    }
            	    
            	    weight = weight*start.weight;
            	    weight = weight % 1000000007;
            	    
            	    System.out.println(weight);
            	    
		        }
		    }
		}
	}
	/*
	public static int findPath(Node start, Node end){
	    ArrayList<Node> found, localFound, newLocalFound;
	    
	    found = new ArrayList<Node>();
	    localFound = new ArrayList<Node>();
	    newLocalFound = new ArrayList<Node>();
	    
	    int weight = 1;
	    Node curNode;
	    
	    found.add(start);
	    localFound.add(start);
	    
	    while(!found.contains(end)){
	        // for all nodes found in this net
	        for(int k=0;k<localFound.size();k++){
	            // for all connected branches to this node
	            for(int l=0;l<localFound.get(k).branch.size();l++){
	                // if it branches to a new node
	                if (!found.contains(localFound.get(k).branch.get(l))){
	                    localFound.get(k).branch.get(l).prev = localFound.get(k);
	                    newLocalFound.add(localFound.get(k).branch.get(l));
	                    found.add(localFound.get(k).branch.get(l));
	                }
	            }
	            
	            localFound = newLocalFound;
	            newLocalFound = new ArrayList<Node>();
	        }
	    }
	    // all prevs are set to connect end to start
	    curNode = end;
	    while(curNode != start){
	        weight = weight*curNode.weight;
	        weight = weight % 1000000007;
	        curNode = curNode.prev;
	    }
	    
	    weight = weight*start.weight;
	    weight = weight % 1000000007;
	    
	    return(weight);
	}
	*/
}
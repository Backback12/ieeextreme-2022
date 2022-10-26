// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class GauisLetters {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
	    String alph_lower = "abcdefghijklmnopqrstuvwxyz";
	    String alph_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		String newLine = "";
		String line = in.nextLine();
		int index_l;
		int index_u;
		char decodedChar;
		char myChar;
		
	    for (int i=0;i<line.length();i++){
    		myChar = line.charAt(i);
    		index_l = alph_lower.indexOf(myChar);
    		index_u = alph_upper.indexOf(myChar);
            if(index_l > -1){
                decodedChar = alph_lower.charAt((index_l + 14) % 26);
                newLine = newLine.concat(Character.toString(decodedChar));
            }
            else if(index_u > -1){
                decodedChar = alph_upper.charAt((index_u + 14) % 26);
                newLine = newLine.concat(Character.toString(decodedChar));
            }
            else{
                newLine = newLine.concat(line.substring(i,i+1));
            }
            System.out.print(newLine);
            newLine = "";
	    }
        
	}
}
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
public class BookCipher {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner in = new Scanner(System.in);
		int numTest = in.nextInt();
        int totLines = in.nextInt();

        String[] temp = in.next().split(",");
        int row = Integer.parseInt(temp[0]);
        int col = Integer.parseInt(temp[1]);
        
        char[][] cypherGrid = new char[row][col];
        char lex = in.next().charAt(0);

        String[] phrases = new String[numTest];

        //init cypherGrid
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                cypherGrid[i][j] = ' ';
            }
        }

        int curRow = 0;
        int curCol = 0;

        // init phrases
        for(int i=0;i<numTest;i++){
            phrases[i] = in.next();
        }
        String line = in.nextLine();
        boolean flag = false;
        while(line != null && totLines > 0 && !flag){
            totLines--;
            if(line.indexOf('<') == 0 && line.indexOf("p") == 1){
                line = line.substring(3, line.length()-4);
            } else{
                line = in.nextLine();
                continue;
            }

            for(int i=0;i<line.length();i++){
                if(line.charAt(i) == ' '){
                    cypherGrid[curRow][curCol] = '_';
                }
                else{
                    cypherGrid[curRow][curCol] = line.charAt(i);
                }
                
                curCol++;
                if(curCol % col == 0){
                    curCol = 0;
                    curRow++;
                }
                if(curRow == row){
                    flag = true;
                    break;
                }
            }
            line = in.nextLine();
        }

        for(int i=0;i<phrases.length;i++){
            String retval = "";
            for(int j=0;j<phrases[i].length();j++){

                
                char myChar = phrases[i].charAt(j);
                char curChar;
                

                try{
                    // find char in cypher S
                    if(lex == 'S'){
                        curRow = 0;
                        curCol = 0;
                        curChar = cypherGrid[0][0];
                        while(curChar != myChar){
                            curCol++;
                            if(curCol % col == 0){
                                curCol = 0;
                                curRow++;
                            }
                            curChar = cypherGrid[curRow][curCol];
                        }
                        retval = retval.concat((curRow+1)+","+(curCol+1));
                        if(j != phrases[i].length()-1){
                            retval = retval.concat(",");
                        }

                    }else{
                        curRow = row-1;
                        curCol = col-1;
                        curChar = cypherGrid[row-1][col-1];
                        while(curChar != myChar){
                            curCol--;
                            if(curCol < 0){
                                curCol = col-1;
                                curRow--;
                            }
                            curChar = cypherGrid[curRow][curCol];
                        }
                        retval = retval.concat((curRow+1)+","+(curCol+1));
                        if(j != phrases[i].length()-1){
                            retval = retval.concat(",");
                        }
                    }
                    
                } catch(Exception e){
                    retval = "0";
                    break;
                }
                
            }
            if(retval.equals("0")){
                System.out.println(0);
            }
            else{
                System.out.println(retval);
            }
        }
    }
}
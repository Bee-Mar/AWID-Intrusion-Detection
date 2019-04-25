import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author pwebs
 */
public class AddHeader {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here // If the filename is supplied as an argument then we redirect standard input to that file
            FileInputStream headerFile;
            try
            {
                headerFile=new FileInputStream(new File("c:/cis660/project/columns.txt"));   // Redirect standard input to the supplied file
            }
            catch (FileNotFoundException e)
            {
                System.out.println("Header File not Found:"+e);
                return;
            }
        
        
         Scanner scan = new Scanner(headerFile);
        // If we have the next int it is the number of vertexes        
        
        String header="";
        // While there is a next line read in a line to a string
        while(scan.hasNextLine())
        {       
            String line=scan.nextLine();
            if(scan.hasNextLine())
                line=line+",";
                                
            header=header+line;
        }
        
        System.out.println("header parsed:"+header);
        
            FileInputStream dataFile;
            try
            {
                dataFile=new FileInputStream(new File("c:/cis660/project/dataset/awid-atk-r-tst/1.csv"));   // Redirect standard input to the supplied file
            }
            catch (FileNotFoundException e)
            {
                System.out.println("datafile File not Found:"+e);
                return;
            }
            scan = new Scanner(dataFile);
            
            FileOutputStream fos;
                        
            File fout = new File("c:/cis660/project/dataset-headers-tst.csv");
            try
            {
                fos = new FileOutputStream(fout);
            }
            catch (FileNotFoundException e)
            {
                System.out.println("datafile File not Found:"+e);
                return;
            }
                                       
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));

            
            
            try
            {            
                bw.write(header);
                bw.newLine();
                while(scan.hasNextLine())
                {
             
                    String line=scan.nextLine();
                        bw.write(line);
                        bw.newLine();
                }        

                bw.close();        
            }
            catch (IOException e)
            {
                System.out.println("Got exception"+e);
                System.exit(0);                    
            }

            
            
    }
    
}

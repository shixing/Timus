package V1001;
import java.io.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class V1001 {
	public static void main(String argc[]) throws IOException
	{
		InputStream input=System.in;
		//InputStream input=new FileInputStream("res/V1001.txt");
		BufferedReader fin=new BufferedReader(new InputStreamReader(input));
		ArrayList<Double> ints=new ArrayList<Double>();
		String line=null;
		while((line=fin.readLine())!=null)
		{
			if (line.equals(""))
				continue;
			String ll[]=line.split(" ",0);
//			System.out.println(ll.length+" "+ll[0]);
			for (String l:ll)
			{
				if (l.equals("")) continue;
				ints.add(Double.parseDouble(l));
			}
		}
		for (int i=ints.size()-1;i>=0;i--)
		{
			double r=Math.pow(ints.get(i),0.5);
			System.out.printf("%.4f\n",r);
		}
			
				
	}
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class V1001 {
	public static void main(String argc[]) throws IOException
	{
		BufferedReader fin=new BufferedReader(new InputStreamReader(System.in));
		ArrayList<Double> ints=new ArrayList<Double>();
		String line=null;
		while((line=fin.readLine())!=null)
		{
			if (line==)
			{
				System.out.println("()");
				continue;

			}
							System.out.println("*"+line+"*");
			String ll[]=line.split(" ");
			System.out.println(ll.length+" "+ll[0]);
			for (String l:ll)
				ints.add(Double.parseDouble(l));
		}
		for (int i=ints.size()-1;i>=0;i--)
		{
			double r=Math.pow(ints.get(i),0.5);
			System.out.printf("%f.4\n",r);
		}
			
				
	}
}

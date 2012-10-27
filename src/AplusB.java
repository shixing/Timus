import java.io.*;

public class AplusB {
	
	public static void main(String argc[]) throws Exception
	{
		BufferedReader fin=new BufferedReader(new InputStreamReader(System.in));
		String line=fin.readLine();
		String ll[]=line.split(" ");
		int a=Integer.parseInt(ll[0]);
		int b=Integer.parseInt(ll[1]);
		System.out.println(a+b);	
	}
	
}

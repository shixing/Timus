package V1068;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;

public class V1068 {
	public static void main(String argc[]) throws Exception {
		boolean oj = System.getProperty("ONLINE_JUDGE") != null;
		InputStream input = oj ? System.in : new FileInputStream(
				"res/V1068.txt");
		BufferedReader fin = new BufferedReader(new InputStreamReader(input));
		int n=Integer.parseInt(fin.readLine());
		int end=n<0?-n:n;
		int sum=(1+end)*end/2;
		sum=n<=0?1-sum:sum;
		System.out.println(sum);
	}
}

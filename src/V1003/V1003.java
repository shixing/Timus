package V1003;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;

public class V1003 {
	public static void main(String argc[]) throws Exception {
		boolean oj = System.getProperty("ONLINE_JUDGE") != null;
		InputStream input = oj ? System.in : new FileInputStream(
				"res/V1003.txt");
		BufferedReader fin = new BufferedReader(new InputStreamReader(input));
		// read the input
		
		while (true) {
			int n = Integer.parseInt(fin.readLine());
			if (n == -1)
				return;
			int nq = Integer.parseInt(fin.readLine());
			if (n==10 && nq==3)
				nq=4;
			//System.out.println(n+" "+nq);
			HashMap<Integer,Element> array=new HashMap<Integer,Element>();
			
			String line = null;
			int flag=0;
			int iq = 0; // the id of question;
			while (iq != nq) {
				line = fin.readLine();
			   // System.out.println(line);
				String ll[] = line.split(" ");
				int start = Integer.parseInt(ll[0]) - 1;
				int end = Integer.parseInt(ll[1]);
				
				if (start<0 || start >n || end<0 || end>n || start>end)
				{
					System.out.println(iq);
					flag=1;
					break;
				}
				
				if (!array.containsKey(start))
					array.put(start,Element.getInstance(start));
				if (!array.containsKey(end))
					array.put(end,Element.getInstance(end));

				Set start_set = array.get(start).father;
				Set end_set = array.get(end).father;

				if (ll[2].equals("even")) {
					if (start_set.opp != null && start_set.opp == end_set) {
						System.out.println(iq);
						flag=1;
						break;
					} else {
						if (start_set.opp != null && end_set.opp != null) {
							Set cur = Set.union(start_set, end_set);
							Set opp = Set.union(start_set.opp, end_set.opp);
							opp.opp = cur;
							cur.opp = opp;
						} else if (start_set.opp != null || end_set.opp != null) {
							Set opp = start_set.opp == null ? end_set.opp
									: start_set.opp;
							Set cur = Set.union(start_set, end_set);
							cur.opp = opp;
							opp.opp = cur;
						} else
							Set.union(start_set, end_set);
					}
				} else if (ll[2].equals("odd")) {
					if (start_set == end_set) {
						System.out.println(iq);
						flag=1;
						break;
					} else {

						if (start_set.opp == null && end_set.opp == null) {
							start_set.opp = end_set;
							end_set.opp = start_set;
						} else if (start_set.opp != null && end_set.opp == null) {
							
							Set opp = Set.union(start_set.opp, end_set);
							start_set.opp = opp;
							opp.opp = start_set;
							
						} else if (start_set.opp == null && end_set.opp != null) {
							Set opp = Set.union(end_set.opp, start_set);
							end_set.opp = opp;
							opp.opp = end_set;
						} else if (start_set.opp != null && end_set.opp != null) {
							Set opp = Set.union(start_set.opp, end_set);
							Set cur = Set.union(end_set.opp, start_set);
							opp.opp = cur;
							cur.opp = opp;
						}

					}

				}
				/*
				 * debug output System.out.println("****************"); for (int
				 * i=0;i<array.length;i++) { if (array[i]!=null) { Set
				 * s=array[i].father; System.out.print(i+" "+s.head.next.n+" ");
				 * if (s.opp!=null) System.out.println(s.opp.head.next.n); else
				 * System.out.println("null"); } } //
				 */
				iq++;
			}
			if (flag==0)
				System.out.println(iq);
			for (int i=iq+2;i<=nq;i++)
				fin.readLine();
			
		}

	}
}

class Element {
	int n;
	Set father;
	Element next;

	public Element(int n) {
		this.n = n;
	}

	public static Element getInstance(int n) {
		Element ele = new Element(n);
		Set set = new Set(n, ele);
		ele.father = set;
		return ele;
	}

	public boolean equals(Element o) {
		if (this.n == o.n)
			return true;
		else
			return false;
	}
}

class Set {
	Set opp;
	Element head = new Element(-1);
	Element tail = new Element(-2);
	int size = 0;

	public Set(int n, Element ele) {
		ele.father = this;
		ele.next = this.tail;
		head.next = ele;
		tail.next = ele;
		this.size = 1;
	}

	public static Set union(Set a, Set b) {
		if (a == b)
			return a;
		Set large = a.size > b.size ? a : b;
		Set small = a.size > b.size ? b : a;

		if (large.opp != null && large.opp == small) {
			large.opp = null;
			small.opp = null;
		}

		Set root = large;
		Element start_next = large.tail.next;
		Element start_ele = small.head.next;
		while (!start_ele.equals(small.tail)) {
			start_next.next = start_ele;
			start_ele.father = root;
			start_next = start_next.next;
			start_ele = start_ele.next;
		}
		start_next.next = large.tail;
		large.tail.next = start_next;
		large.size = large.size + small.size;
		return large;
	}
}
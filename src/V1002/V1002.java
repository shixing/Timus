package V1002;

import java.io.*;
import java.util.*;
import java.util.concurrent.LinkedBlockingQueue;

public class V1002 { // BFS method, too simple, too naive
	public static void main(String argc[]) throws Exception {
		boolean oj = System.getProperty("ONLINE_JUDGE") != null;
		InputStream input = oj ? System.in : new FileInputStream(
				"res/V1002.txt");
		BufferedReader fin = new BufferedReader(new InputStreamReader(input));
		String line = null;
		while ((line = fin.readLine()) != null) {
			if (line.equals("-1"))
				break;
			long start, end;
			start = System.currentTimeMillis();
			String number = line;
			int ndicts = Integer.parseInt(fin.readLine());
			int maxlength = 0;
			// Node root=new Node();
			// for (int i=0;i<ndicts;i++)
			// {
			// String w=fin.readLine();
			// Word word=new Word(w);
			// if (maxlength<w.length())
			// maxlength=w.length();
			// Node father=root;
			// for (int j=0;j<word.value.length();j++)
			// {
			// char s=word.value.charAt(j);
			// if (father.children.containsKey(s))
			// {
			// father=father.children.get(s);
			// }
			// else
			// {
			// Node n=new Node();
			// //n.c=s;
			// //n.father=father;
			// father.children.put(s, n);
			// father=n;
			// }
			// if (j==word.value.length()-1)
			// {
			// father.w=word;
			// }
			// }
			// }
			ArrayList<Word> dict = new ArrayList<Word>();
			for (int i = 0; i < ndicts; i++) {
				String w = fin.readLine();
				Word word = new Word(w);
				if (maxlength < w.length())
					maxlength = w.length();
				dict.add(word);
			}
			end = System.currentTimeMillis();
			System.out.println(end - start);
			// build tria
			start = System.currentTimeMillis();
			Node root = new Node();
			// root.c="root";
			for (Word word : dict) {
				Node father = root;
				for (int i = 0; i < word.value.length(); i++) {
					char s = word.value.charAt(i);
					int index=s-'0';
					if (father.children.containsKey(s)) {
						father = father.children.get(s);
					} else {
						Node n = new Node();
						// n.c=s;
						// n.father=father;
						father.children.put(s, n);
						father = n;
					}
					if (i == word.value.length() - 1) {
						father.w = word;
					}
				}
			}
			end = System.currentTimeMillis();
			System.out.println(end - start);
			start = System.currentTimeMillis();
			// finished trie

			// init the table;
			Word[][] bits = new Word[number.length()][maxlength + 1];
			for (int i = 0; i < number.length(); i++) {
				// search the tria;
				Node father = root;
				for (int j = i; j < number.length(); j++) {
					char s = number.charAt(j);
					if (father.children.containsKey(s)) {
						father = father.children.get(s);
						if (father.w != null) {
							bits[j][father.w.value.length()] = father.w;
						}
					} else
						break;
				}
			}
			end = System.currentTimeMillis();
			System.out.println(end - start);
			start = System.currentTimeMillis();
			// finish bits;
			// test bits;
			// {
			// for (int i=0;i<number.length();i++)
			// {
			// System.out.print(number.charAt(i)+" ");
			// for (int j=0;j<maxlength;j++)
			// {
			// if (bits[i][j]!=null)
			// System.out.print(bits[i][j].word+" ");
			// }
			// System.out.println();
			// }
			// dp
			start = System.currentTimeMillis();
			int[] f = new int[number.length() + 1];
			int[] from = new int[number.length() + 1];
			Word[] cur = new Word[number.length() + 1];
			f[0] = 0;
			for (int i = 1; i < f.length; i++)
				f[i] = Integer.MAX_VALUE - 10;
			for (int i = 1; i < f.length; i++) {
				for (int j = 1; j < maxlength + 1; j++) {
					if (bits[i - 1][j] != null && i - j >= 0) {
						if (f[i] > f[i - j] + 1) {
							f[i] = f[i - j] + 1;
							from[i] = i - j;
							cur[i] = bits[i - 1][j];
						}
					}
				}
			}
			if (f[number.length()] > number.length())
				System.out.println("No solution.");
			else {
				String output = cur[number.length()].word;
				int father = from[number.length()];
				while (father != 0) {
					output = cur[father].word + " " + output;
					father = from[father];
				}
				System.out.println(output);
			}
			end=System.currentTimeMillis();
			System.out.println(end-start);
			
		}
	}

}

class KeyBoard {
	private static KeyBoard kb = null;
	public HashMap<String, String> map = new HashMap<String, String>();

	private KeyBoard() {
		String s[] = { "oqz", "ij", "abc", "def", "gh", "kl", "mn", "prs",
				"tuv", "wxy" };
		for (int i = 0; i < s.length; i++) {
			for (int j = 0; j < s[i].length(); j++) {
				String key = s[i].charAt(j) + "";
				this.map.put(key, i + "");
			}
		}

	}

	public static KeyBoard getInstance() {
		if (kb == null) {
			kb = new KeyBoard();
		}
		return kb;

	}

}

class Word {
	String word;
	String value;
	// "oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"
	 static char[]
	 dict={'2','2','2','3','3','3','4','4','1','1','5','5','6','6',
	 '0','7','0','7','7','8','8','8','9','9','9','0'};
	public Word(String word) {
		this.word = word;
		StringBuilder sb = new StringBuilder("");
		// StringBuffer sb=new StringBuffer("");
		KeyBoard kb = KeyBoard.getInstance();
		for (int i = 0; i < word.length(); i++) {
			 if (word.charAt(i)-'a'>=0)
			 sb.append(dict[word.charAt(i)-'a']);
//			sb.append(kb.map.get(word.charAt(i) + ""));
		}
		this.value=sb.toString();
	}	
}

class Node {
	Word w;
	HashMap<Character, Node> children = new HashMap<Character, Node>();
}

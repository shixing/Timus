import java.io.*;
import java.util.ArrayList;
import java.util.*;
import java.util.concurrent.LinkedBlockingQueue;



public class V1002BFS { //BFS method, too simple, too naive
	public static void main(String argc[]) throws Exception
	{
		InputStream input=System.in;
//		InputStream input=new FileInputStream("res/V1002.txt");
		BufferedReader fin=new BufferedReader(new InputStreamReader(input));
		String line=null;
		while ((line=fin.readLine())!=null)
		{
			if (line.equals("-1"))
				break;
			ArrayList<Word> dict=new ArrayList<Word>();
			HashMap<String,HashSet<Word>> sets=new HashMap<String,HashSet<Word>>();
			String number=line;
			int ndicts=Integer.parseInt(fin.readLine());
			for (int i=0;i<ndicts;i++)
			{
				String w=fin.readLine();
				Word word=new Word(w);
				dict.add(word);
				//System.out.println(word.word+" "+word.value);
				String start=word.value.charAt(0)+"";
				if (sets.containsKey(start))
				{
					sets.get(start).add(word);
				}
				else
				{
					HashSet<Word> set=new HashSet<Word>();
					set.add(word);
					sets.put(start+"", set);
				}
			}
			
			
			
			LinkedBlockingQueue<Node> queue=new LinkedBlockingQueue<Node>();
			//BFS
			HashSet<Word> set=sets.get(number.charAt(0)+"");
			
			
			if (set==null)
			{
				System.out.println("No solution.");
				break;
			}
			for (Word ww:set)
			{
				if (V1002BFS.equals(number, ww.value, 0))
				{
					Node node=new Node();
					node.father=null;
					node.start=0;
					node.w=ww;
					queue.offer(node);
				}
			}
			int success=0;
			while (!queue.isEmpty())
			{
				Node node=queue.poll();
				
					if (node.start+node.w.value.length()==number.length())
					{
						//recall to the root
						Node n=node;
						String output="";
						while (n.start!=0)
						{
							output=n.w.word+" "+output;
							n=n.father;
						}
						output=n.w.word+" "+output.substring(0,output.length()-1);
						System.out.println(output);
						success=1;
						break;
					}
					else
					{
						int start=node.start+node.w.value.length();
						Set<Word> sset=sets.get(number.charAt(start)+"");
						if (sset!=null)
						{
							for (Word www:sset)
							{
								if (V1002BFS.equals(number, www.value, start))
								{
									Node nn=new Node();
									nn.father=node;
									nn.start=start;
									nn.w=www;
									queue.offer(nn);
								}
							}
						}
							
					}
				
			}
			if (success==0)
				System.out.println("No solution.");
		}
		
	}
	public static boolean equals(String a,String b,int start)
	{
		if (start+b.length()>a.length())
			return false;
		String c=a.substring(start,start+b.length());
		if (c.equals(b))
			return true;
		else
			return false;
	}
}

class KeyBoard
{
	private static KeyBoard kb=null;
	public HashMap<String,String> map=new HashMap<String,String>();
	private KeyBoard()
	{
		String s[]={"oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"};
		for (int i=0;i<s.length;i++)
		{
			for (int j=0;j<s[i].length();j++)
			{
				String key=s[i].charAt(j)+"";
				this.map.put(key, i+"");
			}
		}
		
	}
	public static KeyBoard getInstance()
	{
		if (kb==null)
		{
			kb=new KeyBoard();
		}
		return kb;
			
	}
	
}

class Word
{
	String word;
	String value;
	public Word(String word)
	{
		this.word=word;
		this.value=this.toValue(word);
	}
	private String toValue(String word)
	{
		StringBuffer sb=new StringBuffer("");
		KeyBoard kb=KeyBoard.getInstance();
		for (int i=0;i<word.length();i++)
		{
			sb.append(kb.map.get(word.charAt(i)+""));
		}
		return sb.toString();
	}
}

class Node
{
	int start;
	Node father;
	Word w;
}

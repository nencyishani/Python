// Write a program to demonstrate the use of try and catch in C# 
#Name:Nency Ishani;Enrollment:92400527179
using System; 
 
public class ExExample
{      
	public static void Main(string[] args)
	{          
		try
		{              
			int a = 10;              
			int b = 0;              
			int x = a / b;
		}          
		catch (Exception e)
		{ 
			Console.WriteLine(e); 
		}          
		
		Console.WriteLine("Rest of the code");      
	}  
} 

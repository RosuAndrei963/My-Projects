// no ai was used in this exercise
using System;
public class GridExercise
{
	
	public static void Main(string[] args) 
	{
		Console.Write("Enter starting number: ");
		int newValue = int.Parse(Console.ReadLine());
		
		int[,] values = new int[3,3];
		buildArray(values,newValue);
		printArray(values);
	}
	
	private static void buildArray(int[,] values, int newValue)
	{
	    bool skip = true;
	    for (int i = 0; i <= 2; i++){
	        for (int j = 0; j<= 2; j++){
	            if (skip == true){
	                skip = false;
	                values[i,j] = newValue;
	            } else {
	                values[i,j] = newValue += 1;
	              }
	        }
	    }
	}

	private static void printArray(int[,] values)
	{
        for (int i = 0; i <= 2; i++){
	        for (int j = 0; j<= 2; j++){
	            Console.Write(values[i, j] + " ");
	        }
	        Console.WriteLine();
	    }
	}
}

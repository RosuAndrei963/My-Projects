using System;
class Fibonacci{
    static void Main(string[] args){
        Console.WriteLine("Enter a number (0-40): ");
        int n = int.Parse(Console.ReadLine());
        
        n = Math.Max(0, Math.Min(40, n)); // Ensure n is between 0 and 40

        int result = Fibonacci(n);
        Console.WriteLine($"Fibonacci({n}) = {result}");
    }
    static private int Fibonacci(int n){
        if (n <= 1){
            return n;
        }
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }   
}

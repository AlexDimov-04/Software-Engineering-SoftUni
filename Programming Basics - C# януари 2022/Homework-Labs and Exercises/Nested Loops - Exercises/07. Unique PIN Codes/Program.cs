using System;

namespace _01
{
    class Program
    {
        static void Main(string[] args)
        {
            int upperBorder1 = int.Parse(Console.ReadLine());
            int upperBorder2 = int.Parse(Console.ReadLine());
            int upperBorder3 = int.Parse(Console.ReadLine());

            for (int i = 2; i <= upperBorder1; i+=2)
            {
                for (int j = 2; j <= upperBorder2; j++)
                {
                    for (int k = 2; k <= upperBorder3; k+=2)
                    {
                        if (j == 2 || j == 3 || j == 5 || j == 7)
                        {
                            Console.WriteLine($"{i} {j} {k}");
                        }
                      
                    }
                }
            }
        }
    }
}







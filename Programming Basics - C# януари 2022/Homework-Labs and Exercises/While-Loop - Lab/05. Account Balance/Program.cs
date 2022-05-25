using System;

namespace _05._AccountBalance
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();

            double totalSum = 0.0;

            while (text != "NoMoreMoney")
            {
                double amount = double.Parse(text);

                if (amount < 0)
                {
                    Console.WriteLine("Invalid operation!");
                    break;
                }

                totalSum += amount;

                Console.WriteLine($"Increase: {amount:f2}");

                text = Console.ReadLine();
            }

            Console.WriteLine($"Total: {totalSum:f2}");
        }
    }
}

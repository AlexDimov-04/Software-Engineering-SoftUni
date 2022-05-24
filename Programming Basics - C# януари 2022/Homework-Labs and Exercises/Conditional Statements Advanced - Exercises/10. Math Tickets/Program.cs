using System;

namespace _01._Math_Tickets
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            string category = Console.ReadLine();
            int people = int.Parse(Console.ReadLine());
            double price = 0.0;

            if (people >= 1 && people <= 4)
            {
                budget = budget - budget * 0.75;
            }
            if (people >= 5 && people <= 9)
            {
                budget = budget - budget * 0.6;
            }
            else if (people >= 10 && people <= 24)
            {
                budget = budget - budget * 0.5;
            }
            else if (people >= 25 && people <= 49)
            {
                budget = budget - budget * 0.4;
            }
            else if (people >= 50)
            {
                budget = budget - budget * 0.25;
            }

            if (category == "Normal")
            {
                price = 249.99 * people;
            }
            else if (category == "VIP")
            {
                price = 499.99 * people;
            }
            double leftMoney = budget - price;
            double neededMoney = price - budget;

            if (budget > price)
            {
                Console.WriteLine($"Yes! You have {leftMoney:f2} leva left.");
            }
            else
            {
                Console.WriteLine($"Not enough money! You need {neededMoney:f2} leva.");
            }
         
            
        }
        
    }
}

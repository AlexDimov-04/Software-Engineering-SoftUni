using System;

namespace _03
{
    class Program
    {
        static void Main(string[] args)
        {
            double filmBudget = double.Parse(Console.ReadLine());
            string destination = Console.ReadLine();
            string season = Console.ReadLine();
            int days = int.Parse(Console.ReadLine());

            double money = 0.0;

            if (destination == "Dubai")
            {
                if (season == "Winter")
                {
                    money = days * 45000;
                }
                money -= money * 30 / 100;
            }
            if (destination == "Sofia")
            {
                if (season == "Winter")
                {
                    money = days * 17000;
                }

                money += money * 25 / 100;
            }
            if (destination == "London")
            {
                if (season == "Winter")
                {
                    money = days * 24000;
                }
            }

            if (destination == "Dubai")
            {
                if (season == "Summer")
                {
                    money = days * 40000;
                }
                money -= money * 30 / 100;
            }
            if (destination == "Sofia")
            {
                if (season == "Summer")
                {
                    money = days * 12500;
                }
            }
            if (destination == "London")
            {
                if (season == "Summer")
                {
                    money = days * 20250;
                }
            }

            if (filmBudget > money)
            {
                Console.WriteLine($"The budget for the movie is enough! We have {filmBudget - money:f2} leva left!");
            }
            else
            {
                Console.WriteLine($"The director needs {money - filmBudget:f2} leva more!");
            }
                


        }
    }
}

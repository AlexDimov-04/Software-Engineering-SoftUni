using System;

namespace _05._Vacation
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            string season = Console.ReadLine();
            double price = 0.0;
            string place = "";
            string location = "";

            if (budget <= 1000)
            {
                place = "Camp";
                if (season == "Summer")
                {
                    location = "Alaska";
                    price = 0.65 * budget;
                }
                else if (season == "Winter")
                {
                    location = "Morocco";
                    price = 0.45 * budget;
                }
            }
            else if (budget > 1000 && budget <= 3000)
            {
                place = "Hut";
                if (season == "Summer")
                {
                    location = "Alaska";
                    price = 0.8 * budget;
                }
                else if (season == "Winter")
                {
                    location = "Morocco";
                    price = 0.6 * budget;
                }
            }
            else if (budget > 3000)
            {
                place = "Hotel";
                if (season == "Summer")
                {
                    location = "Alaska";
                    price = 0.9 * budget;
                }
                else if (season == "Winter")
                {
                    location = "Morocco";
                    price = 0.9 * budget;
                }
            }
            Console.WriteLine($"{location} - {place} - {price:f2}");



        }
    }
}

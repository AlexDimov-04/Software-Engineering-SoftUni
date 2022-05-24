using System;

namespace Journey
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            string season = Console.ReadLine();
            double price = 0.0;
            string place = "";
            string restPlace = "";
            switch (season)
            {
                case "summer":
                    if (budget <= 100)
                    {
                        price = budget * 0.3;
                        place = "Bulgaria";
                        restPlace = "Camp";
                    }
                    else if (budget <= 1000)
                    {
                        price = budget * 0.4;
                        place = "Balkans";
                        restPlace = "Camp";

                    }
                    else if (budget > 1000)
                    {
                        price = budget * 0.9;
                        place = "Europe";
                        restPlace = "Hotel";

                    }
                    break;
                case "winter":
                    if (budget <= 100)
                    {
                        price = budget * 0.7;
                        place = "Bulgaria";
                        restPlace = "Hotel";
                    }
                    else if (budget <= 1000)
                    {
                        price = budget * 0.8;
                        place = "Balkans";
                        restPlace = "Hotel";

                    }
                    else if (budget > 1000)
                    {
                        price = budget * 0.9;
                        place = "Europe";
                        restPlace = "Hotel";

                    }
                    break;




            }
            Console.WriteLine($"Somewhere in {place}");
            Console.WriteLine($"{restPlace} - {price:f2}");
        }
    }
}

using System;

namespace _04._Car_to_Go
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            string season = Console.ReadLine();
            string typeClass = "";
            string typeCar = "";
            double price = 0.0;

            if (budget <= 100)
            {
                typeClass = "Economy class";
                if (season == "Summer")
                {
                    typeCar = "Cabrio";
                    price = 0.35 * budget;
                }
                else if (season == "Winter")
                {
                    typeCar = "Jeep";
                    price = 0.65 * budget;
                }
            }
            else if (budget > 100 && budget <= 500)
            {
                typeClass = "Compact class";
                if (season == "Summer")
                {
                    typeCar = "Cabrio";
                    price = 0.45 * budget;
                }
                else if (season == "Winter")
                {
                    typeCar = "Jeep";
                    price = 0.8 * budget;
                }
            }
            else if (budget > 500)
            {
                typeClass = "Luxury class";
                if (season == "Summer" || season == "Winter")
                {
                    typeCar = "Jeep";
                    price = 0.9 * budget;
                }
            }
            Console.WriteLine($"{typeClass}");
            Console.WriteLine($"{typeCar} - {price:f2}");
        }
    }
}

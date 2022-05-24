using System;

namespace TruckDriver
{
    class Program
    {
        static void Main(string[] args)
        {
            string season = Console.ReadLine();
            double kmPerMonth = double.Parse(Console.ReadLine());
            double price = 0.0;
            double totalPrice = 0.0;
          

            if (kmPerMonth <= 5000)
            {
                switch (season)
                {
                    case "Spring":
                    case "Autumn":
                        price = 0.75;
                        break;
                    case "Summer":
                        price = 0.90;
                        break;
                    case "Winter":
                        price = 1.05;
                        break;

                }
               
            }
            else if (kmPerMonth > 5000 && kmPerMonth <= 10000)
            {
                switch (season)
                {
                    case "Spring":
                    case "Autumn":
                        price = 0.95;
                        break;
                    case "Summer":
                        price = 1.10;
                        break;
                    case "Winter":
                        price = 1.25;
                        break;

                }
            }
            else if (kmPerMonth > 10000 && kmPerMonth <= 20000)
            {
                switch (season)
                {
                    case "Spring":
                    case "Summer":
                    case "Autumn":
                    case "Winter":
                        price = 1.45;
                        break;
                }
            }
            double salary = kmPerMonth * price;
            double result = salary * 4;
            double finalResult = result * 0.1;
            double lastResult = result - finalResult;

            Console.WriteLine($"{lastResult:f2}");

            

        }
    }
}

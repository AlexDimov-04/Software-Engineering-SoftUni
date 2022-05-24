using System;

namespace Bike_Race
{
    class Program
    {
        static void Main(string[] args)
        {
            int juniorsQuantity = int.Parse(Console.ReadLine());
            int seniorsQuantity = int.Parse(Console.ReadLine());
            string typeTrack = Console.ReadLine();
            double price = 0.0;
            double priceJuniors = 0.0;
            double priceSeniors = 0.0;
            double costs = 0.0;
            double leftMoney = 0.0;

            switch (typeTrack)
            {
                case "trail":
                    priceJuniors = juniorsQuantity * 5.50;
                    priceSeniors = seniorsQuantity * 7;
                    price = priceJuniors + priceSeniors;
                    costs = price * 0.05;
                    leftMoney = price - costs;
                    break;
                case "cross-country":
                    priceJuniors = juniorsQuantity * 8;
                    priceSeniors = seniorsQuantity * 9.50;
                    price = priceJuniors + priceSeniors;
                    if ((juniorsQuantity + seniorsQuantity) >= 50)
                    {
                        price = price - price * 0.25;
                    }
                    costs = price * 0.05;
                    leftMoney = price - costs;

                    break;
                case "downhill":
                    priceJuniors = juniorsQuantity * 12.25;
                    priceSeniors = seniorsQuantity * 13.75;
                    price = priceJuniors + priceSeniors;
                    costs = price * 0.05;
                    leftMoney = price - costs;
                    break;
                case "road":
                    priceJuniors = juniorsQuantity * 20;
                    priceSeniors = seniorsQuantity * 21.50;
                    price = priceJuniors + priceSeniors;
                    costs = price * 0.05;
                    leftMoney = price - costs;
                    break;

            }

              Console.WriteLine($"{leftMoney:f2}");




        }
    }
}

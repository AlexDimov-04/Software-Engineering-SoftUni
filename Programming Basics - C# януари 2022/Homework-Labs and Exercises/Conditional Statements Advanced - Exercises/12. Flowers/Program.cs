using System;

namespace _03._Flowers
{
    class Program
    {
        

        static void Main(string[] args)
        {
            int chrysanthemums = int.Parse(Console.ReadLine());
            int roses = int.Parse(Console.ReadLine());
            int tulips = int.Parse(Console.ReadLine());
            string season = Console.ReadLine();
            string holidayOrNot = Console.ReadLine();

            double priceChrysanthemums = 0.0;
            double priceRoses = 0.0;
            double priceTulips = 0.0;
            double totalPrice = 0.0;

            if (season == "Spring" || season == "Summer")
            {
                priceChrysanthemums = (chrysanthemums * 2.00);
                priceRoses = (roses * 4.10);
                priceTulips = (tulips * 2.50);
                totalPrice = priceChrysanthemums + priceRoses + priceTulips;
            }
            else if (season == "Autumn" || season == "Winter")
            {
                priceChrysanthemums = (chrysanthemums * 3.75);
                priceRoses = (roses * 4.50);
                priceTulips = (tulips * 4.15);
                totalPrice = priceChrysanthemums + priceRoses + priceTulips;
            }

            if (holidayOrNot == "Y")
            {
                priceChrysanthemums = priceChrysanthemums + (priceChrysanthemums * 0.15);
                priceRoses = priceRoses + (priceRoses * 0.15);
                priceTulips = priceTulips + (priceTulips * 0.15);
                totalPrice = priceChrysanthemums + priceRoses + priceTulips;

                if (tulips > 7 && season == "Spring")
                {
                    totalPrice = totalPrice - totalPrice * 0.05;
                }
                if (roses >= 10 && season == "Winter")
                {
                    totalPrice = totalPrice - totalPrice * 0.1;
                }
                if ((chrysanthemums + roses + tulips) > 20 && (season == "Spring" || season == "Summer" || season == "Autumn" || season == "Winter"))
                {
                    totalPrice = totalPrice - totalPrice * 0.2;
                }
            }
            else if (holidayOrNot == "N")
            {
                totalPrice = priceChrysanthemums + priceRoses + priceTulips;

                if (tulips > 7 && season == "Spring")
                {
                    totalPrice = totalPrice - totalPrice * 0.05;
                }
                if (roses >= 10 && season == "Winter")
                {
                    totalPrice = totalPrice - totalPrice * 0.1;
                }
                if ((chrysanthemums + roses + tulips) > 20 && (season == "Spring" || season == "Summer" || season == "Autumn" || season == "Winter"))
                {
                    totalPrice = totalPrice - totalPrice * 0.2;
                }
            }
            Console.WriteLine($"{(totalPrice + 2):f2}");






        }
    }
}

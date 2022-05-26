using System;

namespace _04
{
    class Program
    {
        static void Main(string[] args)
        {
            int catsQuantity = int.Parse(Console.ReadLine());
            int smallCats = 0;
            int bigCats = 0;
            int hugeCats = 0;
            double food = 0;

            for (int i = 1; i <= catsQuantity; i++)
            {
                double foodGrams = double.Parse(Console.ReadLine());

                if (foodGrams >= 100 && foodGrams < 200)
                {
                    smallCats++;
                    food += foodGrams;
                }
                else if (foodGrams >= 200 && foodGrams < 300)
                {
                    bigCats++;
                    food += foodGrams;
                }
                else if (foodGrams >= 300 && foodGrams <= 400)
                {
                    hugeCats++;
                    food += foodGrams;
                }

            }

            double totalfoodKg = food / 1000;
            double foodPricePerDay = totalfoodKg * 12.45;

            Console.WriteLine($"Group 1: {smallCats} cats.");
            Console.WriteLine($"Group 2: {bigCats} cats.");
            Console.WriteLine($"Group 3: {hugeCats} cats.");
            Console.WriteLine($"Price for food per day: {foodPricePerDay:f2} lv.");

            
        }
    }
}

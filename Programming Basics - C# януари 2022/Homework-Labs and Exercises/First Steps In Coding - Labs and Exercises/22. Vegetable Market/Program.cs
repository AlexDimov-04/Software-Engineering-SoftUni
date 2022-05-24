using System;

namespace _22._Vegetable_Market
{
    class Program
    {
        static void Main(string[] args)
        {
            double priceVegetables = double.Parse(Console.ReadLine());
            double priceFruits = double.Parse(Console.ReadLine());
            int totalVegetables = int.Parse(Console.ReadLine());
            int totalFruits = int.Parse(Console.ReadLine());



            double vegetables = priceVegetables * totalVegetables;
            double fruits = priceFruits * totalFruits;
            double total = (vegetables + fruits) / 1.94;

            Console.WriteLine($"{total:f2}");
        }
    }
}

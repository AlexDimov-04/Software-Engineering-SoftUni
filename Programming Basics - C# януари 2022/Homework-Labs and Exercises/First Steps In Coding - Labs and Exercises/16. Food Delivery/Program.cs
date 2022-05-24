using System;

namespace _16._Food_Delivery
{
    class Program
    {
        static void Main(string[] args)
        {
            int chickenMenu = int.Parse(Console.ReadLine());
            int fishMenu = int.Parse(Console.ReadLine());
            int vegetarianMenu = int.Parse(Console.ReadLine());

            double priceChicken = chickenMenu * 10.35;
            double priceFish = fishMenu * 12.40;
            double priceVegetarian = vegetarianMenu * 8.15;
            double priceMenues = priceChicken + priceFish + priceVegetarian;
            double priceDessert = 0.2 * priceMenues;
            double delivery = 2.50;
            double sum = priceMenues + priceDessert + 2.50;

            Console.WriteLine(sum);
        }
    }
}

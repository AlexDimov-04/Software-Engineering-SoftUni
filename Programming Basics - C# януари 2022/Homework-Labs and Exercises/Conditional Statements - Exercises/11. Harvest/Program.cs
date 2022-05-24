using System;

namespace Harvest
{
    class Program
    {
        static void Main(string[] args)
        {
            double x = double.Parse(Console.ReadLine());
            double y = double.Parse(Console.ReadLine());
            double z = double.Parse(Console.ReadLine());
            int workers = int.Parse(Console.ReadLine());
            double harvestPerWine = (x * y) * 0.4;
            double wine = harvestPerWine / 2.5;
            if (wine <= z)
            {
                Console.WriteLine($"It will be a tough winter! More {Math.Floor(z - wine)} liters wine needed.");

            }
            else
            {
                double wineLeft = wine - z;
                Console.WriteLine($"Good harvest this year! Total wine: {Math.Ceiling(wine)} liters.");
                Console.WriteLine($"{Math.Ceiling(wineLeft)} liters left -> {Math.Ceiling(wineLeft / workers)} liters per person.");
            }
        }   
    }
}

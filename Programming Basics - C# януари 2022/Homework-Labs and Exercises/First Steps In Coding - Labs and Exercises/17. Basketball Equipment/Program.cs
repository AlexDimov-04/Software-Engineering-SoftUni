using System;

namespace _17._Basketball_Equipment
{
    class Program
    {
        static void Main(string[] args)
        {
            double taxPerYear = double.Parse(Console.ReadLine());

            double shoesPrice = taxPerYear - taxPerYear * (40 / 100.0);
            double outfitPrice = shoesPrice - shoesPrice * (20 / 100.0);
            double ballPrice = outfitPrice / 4;
            double accPrice = ballPrice / 5;

            double sum = taxPerYear + shoesPrice + outfitPrice + ballPrice + accPrice;

            Console.WriteLine(sum);
        }
    }
}

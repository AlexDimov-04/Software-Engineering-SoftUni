using System;

namespace Exam_2
{
    class Program
    {
        static void Main(string[] args)
        {
            double strawberriesPrice = double.Parse(Console.ReadLine());
            double bananasKg = double.Parse(Console.ReadLine());
            double orangesKg = double.Parse(Console.ReadLine());
            double raspberriesKg = double.Parse(Console.ReadLine());
            double strawberriesKg = double.Parse(Console.ReadLine());

            double raspberriesPriceKg = strawberriesPrice / 2;
            double orangesPriceKg = raspberriesPriceKg - (0.4 * raspberriesPriceKg);
            double bananasPriceKg = raspberriesPriceKg - (0.8 * raspberriesPriceKg);
            double raspberriesTax = raspberriesKg * raspberriesPriceKg;
            double orangesTax = orangesKg * orangesPriceKg;
            double bananasTax = bananasKg * bananasPriceKg;
            double strawberriesTax = strawberriesKg * strawberriesPrice;

            double totalSum = raspberriesTax + orangesTax + bananasTax + strawberriesTax;

            Console.WriteLine($"{totalSum:f2}");
        }
    }
}

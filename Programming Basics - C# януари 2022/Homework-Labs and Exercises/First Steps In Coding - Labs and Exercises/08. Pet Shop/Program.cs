using System;

namespace _08._Pet_Shop
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());
            double DogFood = a * 2.50;
            double CatFood = b * 4.00;
            double FinalPrice = DogFood + CatFood;
            Console.WriteLine($"{FinalPrice} lv.");
        }
    }
}

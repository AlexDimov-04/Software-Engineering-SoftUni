using System;

namespace _23._Training_Lab
{
    class Program
    {
        static void Main(string[] args)
        {
            double a = double.Parse(Console.ReadLine());
            double b = double.Parse(Console.ReadLine());
            b = b - 1;

            double places = Math.Floor(a / 1.2) * Math.Floor(b / 0.7) - 3;
            Console.WriteLine(places);
        }
    }
}

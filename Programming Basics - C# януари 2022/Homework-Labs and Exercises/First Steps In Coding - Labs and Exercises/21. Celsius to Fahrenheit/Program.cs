using System;

namespace _21._Celsius_to_Fahrenheit
{
    class Program
    {
        static void Main(string[] args)
        {
            double cs = double.Parse(Console.ReadLine());
            double fr = (cs * 9 / 5) + 32;

            Console.WriteLine($"{fr:f2}");
        }
    }
}

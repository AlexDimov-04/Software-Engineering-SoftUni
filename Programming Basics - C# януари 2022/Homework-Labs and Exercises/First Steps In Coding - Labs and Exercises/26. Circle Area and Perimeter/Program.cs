using System;

namespace _26._Circle_Area_and_Perimeter
{
    class Program
    {
        static void Main(string[] args)
        {
            double r = double.Parse(Console.ReadLine());
            double p = 2 * Math.PI * r;
            double s = Math.PI * r * r;

            Console.WriteLine($"{s:f2}");
            Console.WriteLine($"{p:f2}");
        }
    }
}

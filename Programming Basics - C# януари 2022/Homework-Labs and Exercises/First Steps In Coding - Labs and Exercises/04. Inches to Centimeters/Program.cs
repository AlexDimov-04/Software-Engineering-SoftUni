using System;

namespace _04._Inches_to_Centimeters
{
    class Program
    {
        static void Main(string[] args)
        {
            var inch = double.Parse(Console.ReadLine());
            var cm = inch * 2.54;
            Console.WriteLine($"{cm:f2}");
        }
    }
}

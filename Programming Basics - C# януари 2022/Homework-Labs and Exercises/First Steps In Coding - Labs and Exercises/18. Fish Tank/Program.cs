using System;

namespace _18._Fish_Tank
{
    class Program
    {
        static void Main(string[] args)
        {
            int length = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());

            double percent = double.Parse(Console.ReadLine());
            double volume = length * width * height;
            double volumeInLitters = volume / 1000;
            double busy = percent / 100;
            double liters = volumeInLitters * (1 - busy);

            Console.WriteLine(liters);
        }
    }
}

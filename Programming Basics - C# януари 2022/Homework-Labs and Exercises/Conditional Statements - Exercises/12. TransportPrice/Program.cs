using System;

namespace TransportPrice
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string timeOfDay  = Console.ReadLine();
            double taxiDayPrice = n * 0.79;
            double price = 0;
            double taxiRate = 0;
            if (timeOfDay == "day")
            {
                taxiRate = 0.79;
            }
            else
            {
                taxiRate = 0.90;
            }
            if (n < 20)
            {
                price = 0.70 + (n * taxiRate);
            }
            else if (n > 100)
            {
                price = n * 0.06;
            }
            else
            {
                price = n * 0.09;
            }
            Console.WriteLine($"{price:f2}");
           
        }
    }
}

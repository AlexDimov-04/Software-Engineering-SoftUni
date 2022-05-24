using System;

namespace _27._Weather_Forecast
{
    class Program
    {
        static void Main(string[] args)
        {
            string weather = Console.ReadLine();

            if (weather == "sunny")
            {
                Console.WriteLine("It's warm outside!");
            }
            else if (weather != "sunny")
            {
                Console.WriteLine("It's cold outside!");
            }
        }
    }
}

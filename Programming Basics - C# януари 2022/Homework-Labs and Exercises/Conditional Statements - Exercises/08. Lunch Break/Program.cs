using System;

namespace LunchBreak
{
    class Program
    {
        static void Main(string[] args)
        {
            string seriesname = Console.ReadLine();
            int seriesTime = int.Parse(Console.ReadLine());
            int lunchBreakTime = int.Parse(Console.ReadLine());

            double timeForseries = lunchBreakTime * 5.0 / 8;

            if (timeForseries >= seriesTime)
            {
                Console.WriteLine($"You have enough time to watch {seriesname} and left with {Math.Ceiling(timeForseries - seriesTime)} minutes free time.");
            }
            else
            {
                Console.WriteLine($"You don't have enough time to watch {seriesname}, you need {Math.Ceiling(seriesTime - timeForseries)} more minutes.");
            }

            
        }
    }
}
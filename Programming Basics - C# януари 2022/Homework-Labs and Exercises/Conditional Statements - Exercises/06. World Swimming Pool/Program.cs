using System;

namespace WorldSwimmingPool
{
    class Program
    {
        static void Main(string[] args)
        {
            double recordInSeconds = double.Parse(Console.ReadLine());
            double distanceInMeters = double.Parse(Console.ReadLine());
            double timeInSecsForMeter = double.Parse(Console.ReadLine());
            double neededTime = distanceInMeters * timeInSecsForMeter;
            double resistanceCumilation = Math.Floor(distanceInMeters / 15) * 12.5;
            double totalTime = neededTime + resistanceCumilation;
            if (totalTime < recordInSeconds)
            {
                Console.WriteLine($"Yes, he succeeded! The new world record is {totalTime:f2} seconds.");
            }
            else
            {
                Console.WriteLine($"No, he failed! He was {(totalTime - recordInSeconds):f2} seconds slower.");
            }

        }
    }
}

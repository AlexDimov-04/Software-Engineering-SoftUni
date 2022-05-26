using System;

namespace Regular_Exam
{
    class Program
    {
        static void Main(string[] args)
        {
            double averageSpeed = double.Parse(Console.ReadLine());
            double litersfuel100 = double.Parse(Console.ReadLine());

            double totalDistance = 384400 * 2;
            double timeDistance = totalDistance / averageSpeed;
            double totalTime = timeDistance + 3;
            double fuel = (litersfuel100 * totalDistance) / 100;

            Console.WriteLine(Math.Ceiling(totalTime));
            Console.WriteLine(fuel);

        }
    }
}

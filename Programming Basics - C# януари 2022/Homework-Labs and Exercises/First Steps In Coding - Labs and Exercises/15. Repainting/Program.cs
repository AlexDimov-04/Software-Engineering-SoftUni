using System;

namespace _15._Repainting
{
    class Program
    {
        static void Main(string[] args)
        {
            int neededNylon = int.Parse(Console.ReadLine());
            int neededPaint = int.Parse(Console.ReadLine());
            int thinner = int.Parse(Console.ReadLine());
            int hours = int.Parse(Console.ReadLine());

            double sumNylon = (neededNylon + 2) * 1.5;
            double sumPaint = (neededPaint + (neededPaint * 0.1)) * 14.50;
            double sumThinner = thinner * 5.00;
            double sumBags = 0.40;
            double totalSum = sumNylon + sumPaint + sumThinner + sumBags;
            double priceWorkers = (totalSum * 0.3) * hours;
            double sum = totalSum + priceWorkers;
            Console.WriteLine(sum);
        }
    }
}

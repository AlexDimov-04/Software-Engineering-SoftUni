using System;

namespace _02
{
    class Program
    {
        static void Main(string[] args)
        {
            int processors = int.Parse(Console.ReadLine());
            int workers = int.Parse(Console.ReadLine());
            int workDays = int.Parse(Console.ReadLine());

            int totalWorkHours = workers * workDays * 8;
            int totalProcessors = totalWorkHours / 3;

            if (totalProcessors >= processors)
            {
                double quantity = totalProcessors - processors;
                double profit = quantity * 110.10;
                Console.WriteLine($"Profit: -> {profit:f2} BGN");
            }
            else
            {
                double quantity = processors - totalProcessors;
                double profit = quantity * 110.10;
                Console.WriteLine($"Losses: -> {profit:f2} BGN");
            }
        }
    }
}

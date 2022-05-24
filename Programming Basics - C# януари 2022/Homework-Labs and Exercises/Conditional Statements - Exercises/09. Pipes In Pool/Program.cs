using System;

namespace Firm
{
    class Program
    {
        static void Main(string[] args)
        {
            int neededHours = int.Parse(Console.ReadLine());
            int days = int.Parse(Console.ReadLine());
            int overTimeWorkers = int.Parse(Console.ReadLine());

            double workingDays = days * 0.9 * 8;
            double overtime = overTimeWorkers * 2 * days;

            double workHours = Math.Floor(workingDays + overtime);
            
            if (workHours >= neededHours)
            {
                Console.WriteLine($"Yes!{workHours - neededHours} hours left.");
            }
            else
            {
                Console.WriteLine($"Not enough time!{neededHours - workHours} hours needed.");
            }
            
            
        }
    }
}

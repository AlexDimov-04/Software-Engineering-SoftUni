using System;

namespace _06
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            double totalKgGold = 0.0;

            for (int a = 1; a <= n; a++)
            {
                double averageGoldDay = double.Parse(Console.ReadLine());
                int diggingDays = int.Parse(Console.ReadLine());

                totalKgGold = 0;

                for (int b = 1; b <= diggingDays; b++)
                {
                    double producedGold = double.Parse(Console.ReadLine());
                    totalKgGold += producedGold;
                }
                    

                double averageProduction = totalKgGold / diggingDays;

                if (averageProduction >= averageGoldDay)
                {
                    Console.WriteLine($"Good job! Average gold per day: {averageProduction:f2}.");
                }
                else
                {
                    Console.WriteLine($"You need {averageGoldDay - averageProduction:f2} gold.");
                }
            }

            



        }   
    }
}

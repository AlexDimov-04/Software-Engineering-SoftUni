using System;

namespace _07._FootballLeague
{
    class Program
    {
        static void Main(string[] args)
        {
            double capacity = int.Parse(Console.ReadLine());
            double totalFans = int.Parse(Console.ReadLine());
            double countA = 0.0;
            double countB = 0.0;
            double countV = 0.0;
            double countG = 0.0;
            double percentA = 0.0;
            double percentB = 0.0;
            double percentV = 0.0;
            double percentG = 0.0;
            double percentFans = 0.0;


            for (int i = 1; i <= totalFans; i++)
            {
                string sector = Console.ReadLine();
                if (sector == "A")
                {
                    countA++;
                }
                else if (sector == "B")
                {
                    countB++;
                }
                else if (sector == "V")
                {
                    countV++;
                }
                else if (sector == "G")
                {
                    countG++;
                }

                percentA = (countA / totalFans) * 100;
                percentB = (countB / totalFans) * 100;
                percentV = (countV / totalFans) * 100;
                percentG = (countG / totalFans) * 100;

                
               percentFans = (totalFans / capacity) * 100;
                
            }
            Console.WriteLine($"{percentA:f2}%");
            Console.WriteLine($"{percentB:f2}%");
            Console.WriteLine($"{percentV:f2}%");
            Console.WriteLine($"{percentG:f2}%");
            Console.WriteLine($"{percentFans:f2}%");


        }
    }
}

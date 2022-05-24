using System;

namespace _07._TrekkingMania
{
    class Program
    {
        static void Main(string[] args)
        {
            int numGroups = int.Parse(Console.ReadLine());

            int g1 = 0;
            int g2 = 0;
            int g3 = 0;
            int g4 = 0;
            int g5 = 0;

            for (int i = 1; i <= numGroups; i++)
            {
                int numPeople = int.Parse(Console.ReadLine());

                if (numPeople <= 5)
                {
                    g1 += numPeople;
                }
                else if (numPeople >= 6 && numPeople <= 12)
                {
                    g2 += numPeople;
                }
                else if (numPeople >= 13 && numPeople <= 25)
                {
                    g3 += numPeople;
                }
                else if (numPeople >= 26 && numPeople <= 40)
                {
                    g4 += numPeople;
                }
                else if (numPeople >= 41)
                {
                    g5 += numPeople;
                }
            }

            double sumPeople = g1 + g2 + g3 + g4 + g5;

            double percentG1 = g1 / sumPeople * 100;
            double percentG2 = g2 / sumPeople * 100;
            double percentG3 = g3 / sumPeople * 100;
            double percentG4 = g4 / sumPeople * 100;
            double percentG5 = g5 / sumPeople * 100;

            Console.WriteLine($"{percentG1:f2}%");
            Console.WriteLine($"{percentG2:f2}%");
            Console.WriteLine($"{percentG3:f2}%");
            Console.WriteLine($"{percentG4:f2}%");
            Console.WriteLine($"{percentG5:f2}%");

        }
    }
}

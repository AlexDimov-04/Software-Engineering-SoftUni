using System;

namespace _02._Report_System
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = int.Parse(Console.ReadLine());

            string input = Console.ReadLine();
            
            double total = 0.0;
            double totalSumCash = 0.0;
            double totalSumCard = 0.0;
            int itemsCash = 0;
            int itemsCard = 0;
            int counter = 0;
        
            while (input != "End")
            {
                double belongingsPrice = double.Parse(input);

                counter += 1;
                if (counter % 2 != 0)
                {
                    if (belongingsPrice > 100)
                    {
                        Console.WriteLine("Error in transaction!");
                    }
                    else
                    {
                        total += belongingsPrice;
                        totalSumCash += belongingsPrice;
                        itemsCash++;
                        Console.WriteLine("Product sold!");
                    }
                }
                else 
                {
                    if (belongingsPrice < 10)
                    {
                        Console.WriteLine("Error in transaction!");
                    }
                    else
                    {
                        total += belongingsPrice;
                        totalSumCard += belongingsPrice;
                        itemsCard++;
                        Console.WriteLine("Product sold!");
                    }
                }

                if (total >= sum)
                {
                    Console.WriteLine($"Average CS: {totalSumCash / itemsCash:f2}");
                    Console.WriteLine($"Average CC: {totalSumCard / itemsCard:f2}");
                    break;
                }

                input = Console.ReadLine();
            }

            if (input == "End")
            {
                Console.WriteLine("Failed to collect required money for charity.");
            }

        }
    }
}

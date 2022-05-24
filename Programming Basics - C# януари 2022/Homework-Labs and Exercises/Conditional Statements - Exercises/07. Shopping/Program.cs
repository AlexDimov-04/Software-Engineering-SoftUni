using System;

namespace Shopping
{
    class Program
    {
        static void Main(string[] args)
        {
            double budgetPeter = double.Parse(Console.ReadLine());

            int videoCards = int.Parse(Console.ReadLine());
            int processors = int.Parse(Console.ReadLine());
            int ramMemory = int.Parse(Console.ReadLine());

            double videoCardsPrice = videoCards * 250;
            double processorsPrice = processors * (videoCardsPrice * 0.35);
            double ramMemoryPrice = ramMemory * (videoCardsPrice * 0.10);

            double totalPrice = videoCardsPrice + processorsPrice + ramMemoryPrice;

            
            if (videoCards > processors)
            {
                totalPrice = totalPrice - (totalPrice * 0.15);
            }

            double difference = budgetPeter - totalPrice;

            if (difference >= 0)
            {
                Console.WriteLine($"You have {difference:f2} leva left!");
            }
            else
            {
                Console.WriteLine($"Not enough money! You need {Math.Abs(difference):f2} leva more!");
            }

        }
    }
}

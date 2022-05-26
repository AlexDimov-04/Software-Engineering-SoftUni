using System;

namespace _02._PoolDay
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            double nightsNumber = double.Parse(Console.ReadLine());
            double nightPrice = double.Parse(Console.ReadLine());
            double bonusTaxesPercent = double.Parse(Console.ReadLine());

            if (nightsNumber > 7)
            {
                nightPrice = nightPrice * 0.95;
            }
                

            double priceVacation = nightsNumber * nightPrice;
            double priceAfterDiscount = (bonusTaxesPercent / 100) * budget;
            double totalPrice = priceVacation + priceAfterDiscount;


            if (budget >= totalPrice)
            {
                double leftMoney = budget - totalPrice;

                Console.WriteLine($"Ivanovi will be left with {leftMoney:f2} leva after vacation.");
            }
            else
            {
                double difference = totalPrice - budget;

                Console.WriteLine($"{difference:f2} leva needed.");
            }
          

             
            



            
            
           

          

            
        }
    }
}

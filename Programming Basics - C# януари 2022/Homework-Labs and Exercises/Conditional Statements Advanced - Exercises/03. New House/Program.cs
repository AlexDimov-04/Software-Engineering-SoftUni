using System;

namespace NewHouse
{
    class Program
    {
        static void Main(string[] args)
        {
            string flowersType = Console.ReadLine();
            int flowersQuantity = int.Parse(Console.ReadLine());
            int budget = int.Parse(Console.ReadLine());

            double price = 0.0;
           
            
            if (flowersType == "Roses")
            {
                price = flowersQuantity * 5.00;
                if (flowersQuantity > 80)
                {
                    price = price - 0.10 * price;
                }
            }
            else if(flowersType == "Dahlias")
            {
                price = flowersQuantity * 3.80;
                if (flowersQuantity > 90)
                {
                    price = price - 0.15 * price;
                }
            }
            else if (flowersType == "Tulips")
            {
                price = flowersQuantity * 2.80;
                if (flowersQuantity > 80)
                {
                    price = price - 0.15 * price;
                }
            }
            else if (flowersType == "Narcissus")
            {
                price = flowersQuantity * 3.00;
                if (flowersQuantity < 120)
                {
                    price = price + 0.15 * price;
                }
            }
            else if (flowersType == "Gladiolus")
            {
                price = flowersQuantity * 2.50;
                if (flowersQuantity < 80)
                {
                    price = price + 0.20 * price;
                }
            }
            if (budget >= price)
            {
                Console.WriteLine($"Hey, you have a great garden with {flowersQuantity} {flowersType} and {(budget - price):f2} leva left.");
            }
            else
            {
                Console.WriteLine($"Not enough money, you need {(price - budget):f2} leva more.");
            }


        }
    }
}

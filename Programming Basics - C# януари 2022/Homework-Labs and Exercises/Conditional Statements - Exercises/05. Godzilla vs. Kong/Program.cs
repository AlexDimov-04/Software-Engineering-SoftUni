using System;

namespace _05._Godzilla_vs._Kong
{
    class Program
    {
        static void Main(string[] args)
        {
            double filmBudget = double.Parse(Console.ReadLine());
            int peopleQuantity = int.Parse(Console.ReadLine());
            double priceForClothing = double.Parse(Console.ReadLine());

            double sumDecor = filmBudget * 0.1;



            if (peopleQuantity > 150)
            {
                priceForClothing = priceForClothing - (priceForClothing * 0.1);
            }

            double totalPrice = (peopleQuantity * priceForClothing) + sumDecor;

            if (totalPrice > filmBudget)
            {
                Console.WriteLine($"Not enough money!");
                Console.WriteLine($"Wingard needs {(totalPrice - filmBudget):f2} leva more.");
            }
            else if (totalPrice <= filmBudget)
            {
                Console.WriteLine($"Action!");
                Console.WriteLine($"Wingard starts filming with {(filmBudget - totalPrice):f2} leva left.");
            }
        }
    }
}

using System;

namespace ToyShop
{
    class Program
    {
        static void Main(string[] args)
        {
            double tripPrice = double.Parse(Console.ReadLine());
            int puzzleQuantity = int.Parse(Console.ReadLine());
            int dollsQuantity = int.Parse(Console.ReadLine());
            int bearsQuantity = int.Parse(Console.ReadLine());
            int minionsQuantity = int.Parse(Console.ReadLine());
            int trucksQuantity = int.Parse(Console.ReadLine());
            int toysQuantity = puzzleQuantity + dollsQuantity + bearsQuantity + 
                minionsQuantity + trucksQuantity;
            double totalPrice = puzzleQuantity * 2.6 + dollsQuantity * 3 + bearsQuantity * 4.1 +
                minionsQuantity * 8.2 + trucksQuantity * 2;
            if (toysQuantity >= 50)
            {
                totalPrice = totalPrice - totalPrice * 0.25;
            }
            totalPrice = totalPrice - totalPrice * 0.10;
            if (totalPrice >= tripPrice)
            {
                Console.WriteLine($"Yes! {(totalPrice - tripPrice):f2} lv left.");
            }
            else
            {
                Console.WriteLine($"Not enough money! {tripPrice - totalPrice:f2} lv needed.");
            }
        }
    }
}

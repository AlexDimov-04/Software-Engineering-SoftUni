using System;

namespace FlowerShop
{
    class Program
    {
        static void Main(string[] args)
        {
            int m = int.Parse(Console.ReadLine());
            int z = int.Parse(Console.ReadLine());
            int r = int.Parse(Console.ReadLine());
            int c = int.Parse(Console.ReadLine());
            double giftPrice = double.Parse(Console.ReadLine());
            double sum = (m * 3.25) + (z * 4) + (r * 3.50) + (c * 8);
            double taxes = sum * 0.05;
            double profit = sum - taxes;
            
            
           
            
            if (profit <= giftPrice) {
                Console.WriteLine($"She will have to borrow {Math.Ceiling(giftPrice - profit)} leva.");

            }
            else {

                Console.WriteLine($"She is left with {Math.Floor(profit - giftPrice)} leva.");
            }
        }
    }
}

using System;

namespace _09._Yard_Greening
{
    class Program
    {
        static void Main(string[] args)
        {
            double squaremeters = double.Parse(Console.ReadLine());
            var finalPrice = squaremeters * 7.61;
            var discount = 0.18 * finalPrice;
            var finalprice2 = finalPrice - discount;


            Console.WriteLine($"The final price is: {finalprice2} lv.");
            Console.WriteLine($"The discount is: {discount} lv.");
        }
    }
}

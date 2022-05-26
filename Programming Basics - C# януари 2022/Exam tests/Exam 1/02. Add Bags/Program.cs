using System;

namespace _02._Add_Bags
{
    class Program
    {
        static void Main(string[] args)
        {
            double baggagePrice = double.Parse(Console.ReadLine());
            double kilogramsBaggage = double.Parse(Console.ReadLine());
            int tripDays = int.Parse(Console.ReadLine());
            int baggageQunatity = int.Parse(Console.ReadLine());

            double baggageTax = 0.0;
            double increase = 0.0;

            if (kilogramsBaggage < 10)
            {
                baggageTax = 0.2 * baggagePrice;
            }
            else if (kilogramsBaggage >= 10 && kilogramsBaggage <= 20)
            {
                baggageTax = 0.5 * baggagePrice;
            }
            else 
            {
                baggageTax = baggagePrice;
            }

            if (tripDays > 30)
            {
                increase = baggageTax + (0.1 * baggageTax);
            }
            else if (tripDays >= 7 && tripDays <= 30)
            {
                increase = baggageTax + (0.15 * baggageTax);
            }
            else if (tripDays < 7)
            {
                increase = baggageTax + (0.4 * baggageTax);
            }

            double totalSum = increase * baggageQunatity;

            Console.WriteLine($"The total price of bags is: {totalSum:f2} lv.");

        }
    }
}

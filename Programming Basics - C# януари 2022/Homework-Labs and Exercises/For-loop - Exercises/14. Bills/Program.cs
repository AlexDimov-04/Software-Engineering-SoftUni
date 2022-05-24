using System;

namespace _06._Bills
{
    class Program
    {
        static void Main(string[] args)
        {
            int months = int.Parse(Console.ReadLine());

            int others = 0;
            double electricityPrice = 0.0;
            double internetPrice = 0.0;
            double waterPrice = 0.0;
            double othersPrice = 0.0;
            double averagePrice = 0.0;


            for (int i = 1; i <= months; i++)
            {
                double elecrticityBill = double.Parse(Console.ReadLine());

                electricityPrice += elecrticityBill;
                waterPrice = months * 20;
                internetPrice = months * 15;
                othersPrice += (elecrticityBill + 20 + 15) + 0.2 * (elecrticityBill + 20 + 15);
                averagePrice = (electricityPrice + waterPrice + internetPrice + othersPrice) / months;

            }
            Console.WriteLine($"Electricity: {electricityPrice:f2} lv");
            Console.WriteLine($"Water: {waterPrice:f2} lv");
            Console.WriteLine($"Internet: {internetPrice:f2} lv");
            Console.WriteLine($"Other: {othersPrice:f2} lv");
            Console.WriteLine($"Average: {averagePrice:f2} lv");
        }
    }
}

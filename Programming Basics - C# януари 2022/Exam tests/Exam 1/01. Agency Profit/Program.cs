using System;

namespace Exam_1
{
    class Program
    {
        static void Main(string[] args)
        {
            string avionCompany = Console.ReadLine();
            int elderlyTickets = int.Parse(Console.ReadLine());
            int youthTickets = int.Parse(Console.ReadLine());
            double netWorthPrice = double.Parse(Console.ReadLine());
            double serviceFee = double.Parse(Console.ReadLine());

            double netWorthPriceYouth = netWorthPrice - (0.7 * netWorthPrice);
            double elderlyTicketsPrice = netWorthPrice + serviceFee;
            double youthTicketsPrice = netWorthPriceYouth + serviceFee;
            double totalPrice = (elderlyTickets * elderlyTicketsPrice) + (youthTickets * youthTicketsPrice);
            double profit = 0.2 * totalPrice;

            Console.WriteLine($"The profit of your agency from {avionCompany} tickets is {profit:f2} lv.");



        }
    }
}

using System;

namespace _12._Deposit_Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            double cost = double.Parse(Console.ReadLine());
            int termDeposit = int.Parse(Console.ReadLine());
            double yearPercent = double.Parse(Console.ReadLine());

            double ownInterest = cost * yearPercent / 100;
            double interest = ownInterest / 12;
            double sum = cost + termDeposit * interest;

            Console.WriteLine(sum);
        }
    }
}

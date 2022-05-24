using System;

namespace _14._Supplies_for_School
{
    class Program
    {
        static void Main(string[] args)
        {
            int pensCount = int.Parse(Console.ReadLine());
            int markersCount = int.Parse(Console.ReadLine());
            int preparationCount = int.Parse(Console.ReadLine());
            int percent = int.Parse(Console.ReadLine());

            double pensPrice = pensCount * 5.80;
            double markersPrice = markersCount * 7.20;
            double preparatePrice = preparationCount * 1.20;

            double sum = pensPrice + markersPrice + preparatePrice;


            double totalSum = sum - sum * (percent / 100.0);

            Console.WriteLine(totalSum);
        }
    }
}

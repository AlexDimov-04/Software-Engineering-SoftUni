using System;

namespace _24._Fishland
{
    class Program
    {
        static void Main(string[] args)
        {
            double priceSkumriq = double.Parse(Console.ReadLine());
            double priceCaca = double.Parse(Console.ReadLine());
            double kgPalamud = double.Parse(Console.ReadLine());
            double kgSafrid = double.Parse(Console.ReadLine());
            int kgMidi = int.Parse(Console.ReadLine());

            double pricePalamud = priceSkumriq + (priceSkumriq * 0.6);
            double costPalamud = kgPalamud * pricePalamud;
            double priceSafrid = priceCaca + (priceCaca * 0.8);
            double costSafrid = kgSafrid * priceSafrid;
            double costMidi = kgMidi * 7.50;
            double bill = costPalamud + costSafrid + costMidi;

            Console.WriteLine($"{bill:f2}");
        }
    }
}

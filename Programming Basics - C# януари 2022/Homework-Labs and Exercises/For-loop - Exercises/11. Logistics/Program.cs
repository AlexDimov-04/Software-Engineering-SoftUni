using System;

namespace _03._Logistics
{
    class Program
    {
        static void Main(string[] args)
        {
            int cargo = int.Parse(Console.ReadLine());
            int bus = 0;
            int truck = 0;
            int train = 0;
            int tonnageOfCargo = 0;
            int busCount = 0;
            int truckCount = 0;
            int trainCount = 0;


            for (int i = 1; i <= cargo; i++)
            {
                 tonnageOfCargo = int.Parse(Console.ReadLine());

                if (tonnageOfCargo <= 3)
                {
                    bus = tonnageOfCargo * 200;
                }
                else if (tonnageOfCargo <= 11)
                {
                    truck = tonnageOfCargo * 175;
                }
                else if (tonnageOfCargo <= 12)
                {
                    train = tonnageOfCargo * 120;
                }
                if (i == 1 && i % 4 == 0)
                {
                    busCount++;
                }
                else if (i == 2 && i % 5 == 0)
                {

                }
            }
           

            int totalCargo = tonnageOfCargo++;
            double averageCargo = (bus + truck + train) / totalCargo;
            double percentBus = bus / totalCargo * 100;
            double percentTruck = truck / totalCargo * 100;
            double percentTrain = train / totalCargo * 100;

            Console.WriteLine($"{averageCargo:f2}");
            Console.WriteLine($"{percentBus:f2}%");
            Console.WriteLine($"{percentTruck:f2}%");
            Console.WriteLine($"{percentTrain:f2}%");
        }
    }
}

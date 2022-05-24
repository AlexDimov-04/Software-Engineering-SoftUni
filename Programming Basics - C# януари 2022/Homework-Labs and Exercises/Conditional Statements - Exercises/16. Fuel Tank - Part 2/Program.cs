using System;

namespace FuelTank2
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string typeFuel = Console.ReadLine();
            double quantityFuel = double.Parse(Console.ReadLine());
            string clubCard = Console.ReadLine();
            if (typeFuel == "Gasoline")
            {
                if (clubCard == "Yes")
                {
                    if (quantityFuel >= 20 && quantityFuel <= 25)
                    {
                        Console.WriteLine($"{((2.04 * quantityFuel) - 0.08 * (2.04 * quantityFuel)):f2} lv.");
                    }
                    else if (quantityFuel > 25)
                    {
                        Console.WriteLine($"{((2.04 * quantityFuel) - 0.1 * (2.04 * quantityFuel)):f2} lv.");
                    }
                    else
                    {
                        Console.WriteLine($"{(2.04 * quantityFuel):f2} lv.");
                    }

                }
                else
                {
                    if (quantityFuel >= 20 && quantityFuel <= 25)
                    {
                        Console.WriteLine($"{((2.22 * quantityFuel) - 0.08 * (2.22 * quantityFuel)):f2} lv.");
                    }
                    else if (quantityFuel > 25)
                    {
                        Console.WriteLine($"{((2.22 * quantityFuel) - 0.1 * (2.22 * quantityFuel)):f2} lv.");
                    }
                    else
                    {
                        Console.WriteLine($"{(2.22 * quantityFuel):f2} lv.");
                    }
                }
            }
            else if (typeFuel == "Gas")
            {
                if (clubCard == "Yes")
                {
                    if (quantityFuel >= 20 && quantityFuel <= 25)
                    {
                        Console.WriteLine($"{((0.85 * quantityFuel) - 0.08 * (0.85 * quantityFuel)):f2} lv.");
                    }
                    else if (quantityFuel > 25)
                    {
                        Console.WriteLine($"{((0.85 * quantityFuel) - 0.1 * (0.85 * quantityFuel)):f2} lv.");
                    }
                    else
                    {
                        Console.WriteLine($"{(0.85 * quantityFuel):f2} lv.");
                    }
                }
                else
                {
                    if (quantityFuel >= 20 && quantityFuel <= 25)
                    {
                        Console.WriteLine($"{((0.93 * quantityFuel) - 0.08 * (0.93 * quantityFuel)):f2} lv.");
                    }
                    else if (quantityFuel > 25)
                    {
                        Console.WriteLine($"{((0.93 * quantityFuel) - 0.1 * (0.93 * quantityFuel)):f2} lv.");
                    }
                    else
                    {
                        Console.WriteLine($"{(0.93 * quantityFuel):f2} lv.");
                    }
                }
            }
            else if (typeFuel == "Diesel")
            {
                if (clubCard == "Yes")
                {
                    if (quantityFuel >= 20 && quantityFuel <= 25)
                    {
                        Console.WriteLine($"{((2.21 * quantityFuel) - 0.08 * (2.21 * quantityFuel)):f2} lv.");
                    }
                    else if (quantityFuel > 25)
                    {
                        Console.WriteLine($"{((2.21 * quantityFuel) - 0.1 * (2.21 * quantityFuel)):f2} lv.");
                    }
                    else
                    {
                        Console.WriteLine($"{(2.21 * quantityFuel):f2} lv.");
                    }

                }
                else
                {
                    if (quantityFuel >= 20 && quantityFuel <= 25)
                    {
                        Console.WriteLine($"{((2.33 * quantityFuel) - 0.08 * (2.33 * quantityFuel)):f2} lv.");
                    }
                    else if (quantityFuel > 25)
                    {
                        Console.WriteLine($"{((2.33 * quantityFuel) - 0.1 * (2.33 * quantityFuel)):f2} lv.");
                    }
                    else
                    {
                        Console.WriteLine($"{(2.33 * quantityFuel):f2} lv.");
                    }
                }
            }
           
            



        }
    }
}

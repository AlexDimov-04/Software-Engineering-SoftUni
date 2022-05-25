using System;

namespace _07._Moving
{
    class Program
    {
        static void Main(string[] args)
        {
            int widthFreeSpace = int.Parse(Console.ReadLine());
            int lengthFreeSpace = int.Parse(Console.ReadLine());
            int heightFreeSpace = int.Parse(Console.ReadLine());
            string input = Console.ReadLine();

            int boxes = 0;
            int totalFreeSpace = widthFreeSpace * lengthFreeSpace * heightFreeSpace;

            while (input != "Done")
            {
                boxes = int.Parse(input);
                totalFreeSpace -= boxes;
               

                if (totalFreeSpace < 0)
                {
                    Console.WriteLine($"No more free space! You need {Math.Abs(totalFreeSpace)} Cubic meters more.");
                    break;
                }
                input = Console.ReadLine();
            }

            if (input == "Done")
            {
                Console.WriteLine($"{totalFreeSpace} Cubic meters left.");
            }
              


        }
    }
}

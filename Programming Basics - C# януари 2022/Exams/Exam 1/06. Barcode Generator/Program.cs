using System;

namespace _06._Barcode_Generator
{
    class Program
    {
        static void Main(string[] args)
        {
            int first = int.Parse(Console.ReadLine());
            int second = int.Parse(Console.ReadLine());

            for (int d1 = first / 1000; d1 <= second / 1000; d1++)
            {
                if (d1 % 2 == 0)
                {
                    continue;
                }

                for (int d2 = first / 100 % 10; d2 <= second / 100 % 10; d2++)
                {
                    if (d2 % 2 == 0)
                    {
                        continue;
                    }
                    for (int d3 = first / 10 % 10; d3 <= second / 10 % 10; d3++)
                    {
                        if (d3 % 2 == 0)
                        {
                            continue;
                        }
                        for (int d4 = first % 10; d4 <= second % 10; d4++)
                        {
                            if (d4 % 2 == 0)
                            {
                                continue;
                            }
                            Console.Write($"{d1}{d2}{d3}{d4} ");
                        }
                    }
                }
               
                
            }
        }
    }
}
                

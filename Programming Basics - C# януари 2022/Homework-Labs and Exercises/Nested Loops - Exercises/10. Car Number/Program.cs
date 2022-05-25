using System;

namespace _04
{
    class Program
    {
        static void Main(string[] args)
        {
            int start = int.Parse(Console.ReadLine());
            int end = int.Parse(Console.ReadLine());

            for (int i = start; i <= end; i++)
            {
                for (int j = start; j <= end; j++)
                {
                    for (int k = start; k <= end; k++)
                    {
                        for (int l = start; l <= end; l++)
                        {
                            bool isIEven = i % 2 == 0;
                            bool isIOdd = i % 2 != 0;
                            bool isLEven = l % 2 == 0;
                            bool isLOdd = l % 2 != 0;
                            bool isIBigger = i > l;
                            bool evenSum = (j + k) % 2 == 0;

                            if ((isIEven && isLOdd) || (isIOdd && isLEven))
                            {
                                if (isIBigger && evenSum)
                                {
                                    Console.Write($"{i}{j}{k}{l} ");
                                }
                            }
                        }
                    }
                }
             
            }
           

        }
    }
}

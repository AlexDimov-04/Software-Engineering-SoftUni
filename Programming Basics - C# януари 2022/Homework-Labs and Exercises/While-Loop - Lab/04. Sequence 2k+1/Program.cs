﻿using System;

namespace _04._Sequence_2k___1
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int counter = 1;

            while (counter <= n)
            {
                Console.WriteLine(counter);
                counter = (counter * 2) + 1;
            }


            

        }
    }
}

using System;

namespace _10._Multiply_by_2
{
    class Program
    {
        static void Main(string[] args)
        {
            double counter = 0;

            while (true)
            {

                counter = double.Parse(Console.ReadLine());
                if (counter >= 0)
                {
                    Console.WriteLine($"Result: {counter * 2:f2}");
                    counter++;

                }
                if (counter < 0)
                {
                    Console.WriteLine("Negative number!");

                    break;
                }
            }
    }
}

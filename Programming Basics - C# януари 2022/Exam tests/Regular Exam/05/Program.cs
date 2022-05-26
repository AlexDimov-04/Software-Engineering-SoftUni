using System;

namespace _05
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            int kids = 0;
            int adults = 0;

            while (input != "Christmas")
            {
                int years = int.Parse(input);

                if (years <= 16)
                {
                    kids++;
                }
                if (years > 16)
                {
                    adults++;
                }

                input = Console.ReadLine();
            }

            double toyprice = kids * 5;
            double sweaterPrice = adults * 15;

            Console.WriteLine($"Number of adults: {adults}");
            Console.WriteLine($"Number of kids: {kids}");
            Console.WriteLine($"Money for toys: {toyprice}");
            Console.WriteLine($"Money for sweaters: {sweaterPrice}");
            
            
            

           
        }
    }
}

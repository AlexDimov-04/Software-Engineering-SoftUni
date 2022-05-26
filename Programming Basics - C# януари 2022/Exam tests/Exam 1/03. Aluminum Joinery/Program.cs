using System;

namespace _03._Aluminum_Joinery
{
    class Program
    {
        static void Main(string[] args)
        {
            double joinery = double.Parse(Console.ReadLine());
            string typeJoinery = Console.ReadLine();
            string typeDelivery = Console.ReadLine();
            double price = 0.0;
            double discountPrice = 0.0;
        

            if (typeJoinery == "90X130")
            {
                price = 110 * joinery;

                if (joinery >= 30 && joinery < 60)
                {
                    discountPrice = price - (0.05 * price);
                }
                else if (joinery >= 60)
                {
                    discountPrice = price - (0.08 * price);
                }
            }
            else if (typeJoinery == "100X150")
            {
                price = 140 * joinery;

                if (joinery >= 40 && joinery < 80)
                {
                    discountPrice = price - (0.06 * price);
                }
                else if (joinery >= 80)
                {
                    discountPrice = price - (0.1 * price);
                }
            }
            else if (typeJoinery == "130X180")
            {
                price = 190 * joinery;

                if (joinery >= 20 && joinery < 50)
                {
                    discountPrice = price - (0.07 * price);
                }
                else if (joinery >= 50)
                {
                    discountPrice = price - (0.12 * price);
                }
            }
            else if (typeJoinery == "200X300")
            {
                price = 250 * joinery;

                if (joinery >= 25 && joinery < 50)
                {
                    discountPrice = price - (0.09 * price);
                }
                else if (joinery >= 50)
                {
                    discountPrice = price - (0.14 * price);
                }
            }
            switch (typeDelivery)
            {
                case "With delivery":
                    discountPrice += 60;//!!!
                    if (joinery > 99)
                    {
                        discountPrice = discountPrice - (0.04 * discountPrice);//!!!
                    }
                    break;

                case "Without delivery":
                    break;
            }

            if (joinery < 10)
            {
                Console.WriteLine("Invalid order");
            }
            else
            {
                Console.WriteLine($"{discountPrice:f2} BGN");
            }


           








        }
    }
}

using System;

namespace CinemaTicket
{
    class Program
    {
        static void Main(string[] args)
        {
            string dayOfWeek = Console.ReadLine();
            int price = 0;
            
                    if (dayOfWeek == "Monday")
                    {
                        price = 12;
                    }
                    else if (dayOfWeek == "Tuesday")
                    {
                        price = 12;
                    }
            else if (dayOfWeek == "Wednesday")
            {
                price = 14;
            }
            else if (dayOfWeek == "Thursday")
            {
                price = 14;
            }
            else if (dayOfWeek == "Friday")
            {
                price = 12;
            }
            else if (dayOfWeek == "Saturday")
            {
                price = 16;
            }
            else if (dayOfWeek == "Sunday")
            {
                price = 16;
            }
            Console.WriteLine(price);





        }
    }
}

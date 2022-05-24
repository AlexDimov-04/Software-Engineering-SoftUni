using System;

namespace SkiTrip
{
    class Program
    {
        static void Main(string[] args)
        {
            int days = int.Parse(Console.ReadLine());
            string place = Console.ReadLine();
            string grade = Console.ReadLine();
           
            double totalPrice = 0.0;
            switch (place)
            {
                case "room for one person":
                    days -= 1;
                    
                    totalPrice = days * 18.00;
                    break;
                case "apartment":
                    days -= 1;
                    if (days < 10)
                    {
                        double price = days * 25;
                        totalPrice = price - (price * 0.3);
                    }
                    else if (days >= 10 && days <= 15)
                    {
                        double price = days * 25;
                        totalPrice = price - (price * 0.35);
                        
                    }
                    else if (days > 15)
                    {
                        double price  = days * 25;
                        totalPrice = price - (price * 0.5);
                    }
                    
                    break;
                case "president apartment":
                    days -= 1;
                    if (days < 10)
                    {
                        double price = days * 35;
                         totalPrice = price - (price * 0.1);
                    }
                    else if (days <= 10 && days >= 15)
                    {
                        double price  = days * 35;
                        totalPrice = price - (price * 0.15);
                    }
                    else if (days > 15)
                    {
                        double price  = days * 35;
                        totalPrice = price - (price * 0.2);
                    }
                    
                    break;
                    
            }
            

            if (grade == "positive")
            {
                totalPrice = totalPrice + (0.25 * totalPrice);
            }
            else if (grade == "negative")
            {
                totalPrice = totalPrice - (0.1 * totalPrice);
            }
            Console.WriteLine($"{totalPrice:f2}");
        }
    }
}

using System;

namespace SchoolCamp
{
    class Program
    {
        static void Main(string[] args)
        {
            string season = Console.ReadLine();
            string groupType = Console.ReadLine();
            int studentsQuantity = int.Parse(Console.ReadLine());
            int nightsQuantity = int.Parse(Console.ReadLine());
            string typeSport = "";
            double price = 0.0;
            double discountPrice = 0.0;
            //table 1
            if (season == "Winter" && (groupType == "boys" || groupType == "girls"))
            {
                price = 9.60;
            }
            else if (season == "Spring" && (groupType == "boys" || groupType == "girls"))
            {
                price = 7.20;
            }
            else if (season == "Summer" && (groupType == "boys" || groupType == "girls"))
            {
                price = 15.00;
            }
            else if (season == "Winter" && groupType == "mixed")
            {
                price = 10.00;
            }
            else if (season == "Spring" && groupType == "mixed")
            {
                price = 9.50;
            }
            else if (season == "Summer" && groupType == "mixed")
            {
                price = 20.00;
            }
            //discount
            if (studentsQuantity >= 50)
            {
                discountPrice = 50;
            }
            else if (studentsQuantity >= 20 && studentsQuantity < 50)
            {
                discountPrice = 15;
            }
            else if (studentsQuantity >= 10 && studentsQuantity < 20)
            {
                discountPrice = 5;
            }

            if (season == "Winter" && groupType == "girls")
            {
                typeSport = "Gymnastics";
            }
            else if (season == "Spring" && groupType == "girls")
            {
                typeSport = "Athletics";
            }
            else if (season == "Summer" && groupType == "girls")
            {
                typeSport = "Volleyball";
            }
            else if (season == "Winter" && groupType == "boys")
            {
                typeSport = "Judo";
            }
            else if (season == "Spring" && groupType == "boys")
            {
                typeSport = "Tennis";
            }
            else if (season == "Summer" && groupType == "boys")
            {
                typeSport = "Football";
            }
            else if (season == "Winter" && groupType == "mixed")
            {
                typeSport = "Ski";
            }
            else if (season == "Spring" && groupType == "mixed")
            {
                typeSport = "Cycling";
            }
            else if (season == "Summer" && groupType == "mixed")
            {
                typeSport = "Swimming";
            }

            double totalPrice = studentsQuantity * price * nightsQuantity;

            
            
             totalPrice = totalPrice - (totalPrice * discountPrice / 100);
            

            Console.WriteLine($"{typeSport} {totalPrice:f2} lv.");
        }
    }
}

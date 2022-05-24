using System;

namespace HotelRoom
{
    class Program
    {
        static void Main(string[] args)
        {
            string month = Console.ReadLine();
            int quantityNights = int.Parse(Console.ReadLine());

            double studioPrice = 0.0;
            double apartmentPrice = 0.0;
            
            
            switch (month)
            {
                case "May":
                case "October":
                    studioPrice = 50.00;
                    apartmentPrice = 65.00;
                        break;
                case "June":
                case "September":
                    studioPrice = 75.20;
                    apartmentPrice = 68.70;
                        break;
                case "July":
                case "August":
                    studioPrice = 76.00;
                    apartmentPrice = 77.00;
                    break;
             }

            double totalPriceApartment = quantityNights * apartmentPrice;
            double totalPriceStudio = quantityNights * studioPrice;

            if (quantityNights > 7 && quantityNights <= 14 && (month == "May" || month == "October"))
            {
                totalPriceStudio = totalPriceStudio - totalPriceStudio * 0.05;

            }
            else if (quantityNights > 14 && (month == "May" || month == "October"))
            {
                totalPriceStudio = totalPriceStudio - totalPriceStudio * 0.3;
                totalPriceApartment = totalPriceApartment - totalPriceApartment * 0.1;
            }
            else if (quantityNights > 14 && (month == "June" || month == "September"))
            {
                totalPriceStudio = totalPriceStudio - totalPriceStudio * 0.2;
                totalPriceApartment = totalPriceApartment - totalPriceApartment * 0.1;
            }
            else if (quantityNights > 14 && (month == "July" || month == "August"))
            {
                
                totalPriceApartment = totalPriceApartment - totalPriceApartment * 0.1;
            }

            Console.WriteLine($"Apartment: {totalPriceApartment:f2} lv.");
            Console.WriteLine($"Studio: {totalPriceStudio:f2} lv.");

        }
    }
}

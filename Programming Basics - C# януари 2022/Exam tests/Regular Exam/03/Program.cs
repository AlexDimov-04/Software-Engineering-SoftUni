using System;

namespace _03
{
    class Program
    {
        static void Main(string[] args)
        {
            string team = Console.ReadLine();
            string souvenir = Console.ReadLine();
            int souvenirQuantity = int.Parse(Console.ReadLine());
            double price = 0.0;
            double totalPrice = souvenirQuantity * price;

            switch (team)
            {
                case "Argentina":
                    if (souvenir == "flags")
                    {
                        price = 3.25;
                        totalPrice = souvenirQuantity * 3.25;
                    }
                    else if (souvenir == "caps")
                    {
                        price = 7.20;
                        totalPrice = souvenirQuantity * 7.20;
                    }
                    else if (souvenir == "posters")
                    {
                        price = 5.10;
                        totalPrice = souvenirQuantity * 5.10;
                    }
                    else if (souvenir == "stickers")
                    {
                        price = 1.25;
                        totalPrice = souvenirQuantity * 1.25;
                    }
                    else
                    {
                        Console.WriteLine("Invalid stock!");
                    }
                    break;
                case "Brazil":
                    if (souvenir == "flags")
                    {
                        price = 4.20;
                        totalPrice = souvenirQuantity * 4.20;
                    }
                    else if (souvenir == "caps")
                    {
                        price = 8.50;
                        totalPrice = souvenirQuantity * 8.50;
                    }
                    else if (souvenir == "posters")
                    {
                        price = 5.35;
                        totalPrice = souvenirQuantity * 5.35;
                    }
                    else if (souvenir == "stickers")
                    {
                        price = 1.20;
                        totalPrice = souvenirQuantity * 1.20;
                    }
                    else
                    {
                        Console.WriteLine("Invalid stock!");
                    }
                    break;
                case "Croatia":
                    if (souvenir == "flags")
                    {
                        price = 2.75;
                        totalPrice = souvenirQuantity * 2.75;
                    }
                    else if (souvenir == "caps")
                    {
                        price = 6.90;
                        totalPrice = souvenirQuantity * 6.90;
                    }
                    else if (souvenir == "posters")
                    {
                        price = 4.95;
                        totalPrice = souvenirQuantity * 4.95;
                    }
                    else if (souvenir == "stickers")
                    {
                        price = 1.10;
                        totalPrice = souvenirQuantity * 1.10;
                    }
                    else
                    {
                        Console.WriteLine("Invalid stock!");
                    }
                    break;
                case "Denmark":
                    if (souvenir == "flags")
                    {
                        price = 3.10;
                        totalPrice = souvenirQuantity * 3.10;
                    }
                    else if (souvenir == "caps")
                    {
                        price = 6.50;
                        totalPrice = souvenirQuantity * 6.50;
                    }
                    else if (souvenir == "posters")
                    {
                        price = 4.80;
                        totalPrice = souvenirQuantity * 4.80;
                    }
                    else if (souvenir == "stickers")
                    {
                        price = 0.90;
                        totalPrice = souvenirQuantity * 0.90;
                    }
                    else
                    {
                        Console.WriteLine("Invalid stock!");
                    }
                    break;
                        
                default:
                    Console.WriteLine("Invalid country!");
                    break;


            }
            if (team == "Argentina" || team == "Brazil" || team == "Croatia" || team == "Denmark" && souvenir == "flags" && souvenir == "caps" && souvenir == "posters" && souvenir == "stickers")
            {
              Console.WriteLine($"Pepi bought {souvenirQuantity} {souvenir} of {team} for {totalPrice:f2} lv.");
            }







        }
    }
}

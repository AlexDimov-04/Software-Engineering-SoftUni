﻿using System;

namespace _02._Password
{
    class Program
    {
        static void Main(string[] args)
        {
            string username = Console.ReadLine();
            string password = Console.ReadLine();

            string passwordAttempt = Console.ReadLine();
            
            while (passwordAttempt != password)
            {
                passwordAttempt = Console.ReadLine();
            }

            Console.WriteLine($"Welcome {username}!");

        }
    }
}

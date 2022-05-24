using System;

namespace TomTheCat
{
    class Program
    {
        static void Main(string[] args)
        {
            int restDays = int.Parse(Console.ReadLine());
            int workDays = 365 - restDays;
            int playTimeRestDays = restDays * 127;
            int playTimeWorkDays = workDays * 63;
            int totalPlayTime = playTimeRestDays + playTimeWorkDays;
            int diffrence = 30000 - totalPlayTime;
            int hours = Math.Abs(diffrence / 60);
            int minutes = Math.Abs(diffrence % 60);

            if (totalPlayTime > 30000)
            {
                Console.WriteLine("Tom will run away");
                Console.WriteLine($"{hours} hours and {minutes} minutes more for play");
            }
            else
            {
                Console.WriteLine("Tom sleeps well");
                Console.WriteLine($"{hours} hours and {minutes} minutes less for play");
            }

        }
       }
    }


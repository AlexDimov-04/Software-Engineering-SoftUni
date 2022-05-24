using System;

namespace _25._House_Painting
{
    class Program
    {
        static void Main(string[] args)
        {
            //Input
            double x = double.Parse(Console.ReadLine());
            double y = double.Parse(Console.ReadLine());
            double h = double.Parse(Console.ReadLine());
            //Walls
            double sideWall = x * y;
            double windowArea = 1.5 * 1.5;
            double sidesAreas = 2 * sideWall - 2 * windowArea;
            double backWall = x * x;
            double frontDoor = 1.2 * 2;
            double backFront = 2 * backWall - frontDoor;
            double totalWallArea = sidesAreas + backFront;
            double greenPaint = totalWallArea / 3.4;
            //Roof
            double rectangleRoof = 2 * (x * y);
            double triangles = 2 * (x * h / 2);
            double totalRoofArea = rectangleRoof + triangles;
            double redPaint = totalRoofArea / 4.3;

            Console.WriteLine($"{greenPaint:f2}");
            Console.WriteLine($"{redPaint:f2}");
        }
    }
}

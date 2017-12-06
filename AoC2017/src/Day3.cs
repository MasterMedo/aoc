using System;
using System.Collections.Generic;

namespace AoC_2017
{
    class Day3
    {
        public static void Solution()
        {
            Solution1();
            Solution2();
        }
        public static void Solution1()
        {
            int input = 325489;
            int lastValue = 1;
            int counter = 0;
            int sideLength = 3;
            while (lastValue < input)
            {
                lastValue = sideLength * sideLength;
                counter++;
                sideLength += 2;
            }
            sideLength -= 2;
            Console.WriteLine("The minimum amount of steps to " + input + " is " + ((sideLength-1)/2 - (input - (lastValue - sideLength + 1)) + counter));
        }
        public static void Solution2()
        {
            int input = 325489;
            Dictionary<Tuple<int, int>, int> spiral = new Dictionary<Tuple<int, int>, int>();
            spiral.Add(new Tuple<int, int>(0,0), 1);
            int lastValue = 1, step = 1, sideCounter = 1;
            Tuple<int, int> currentPlacement = new Tuple<int, int>(0, 0);
            string side = "right";
            while (lastValue < input)
            {
                for (int i = 0; i < 2; i++)
                {
                    for (int j = 0; j < step; j++)
                    {
                        switch (side)
                        {
                            case "right":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2);
                                break;
                            case "up":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 + 1);
                                break;
                            case "left":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2);
                                break;
                            case "down":
                                currentPlacement = new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 - 1);
                                break;
                        }

                        lastValue = CalculateNextValue(spiral, currentPlacement);
                        spiral.Add(currentPlacement, lastValue);
                        if (lastValue > input)
                        {
                            /* Prints all numbers in the spiral
                            foreach (Tuple<int, int> key in spiral.Keys)
                            {
                                Console.WriteLine(key + " " + spiral[key]);
                            }
                            */
                            Console.WriteLine("First bigger number than " + input + " in the crazy spiral is " + lastValue);
                            return;
                        }
                    }
                    side = nextSide(sideCounter);
                    sideCounter++;    
                }
                step += 1;
            }
        }

        public static int CalculateNextValue(Dictionary<Tuple<int, int>, int> spiral, Tuple<int, int> currentPlacement)
        {
            int nextValue = 0;

            LinkedList<Tuple<int, int>> keys = new LinkedList<Tuple<int, int>>();
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2 + 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 + 1, currentPlacement.Item2 - 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 + 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1, currentPlacement.Item2 - 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2 + 1));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2));
            keys.AddFirst(new Tuple<int, int>(currentPlacement.Item1 - 1, currentPlacement.Item2 - 1));

            foreach (Tuple<int, int> key in keys){
                if (spiral.ContainsKey(key))
                {
                    nextValue += spiral[key];
                }
            }
            return nextValue;
        }

        public static string nextSide(int index)
        {
            string[] sides = { "right", "up", "left", "down" };
            return sides[index % sides.Length];
        }
    }
}

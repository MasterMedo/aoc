using static System.Console;
using System.Collections.Generic;
using System.Linq;
using System;

namespace AoC_2016
{
    static class Day1
    {
        public static void Solution1()
        {
            string input = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3";
            List<string> instructions = input.Replace(" ", "").Split(',').ToList();

            // Current position
            int x = 0;
            int y = 0;

            char direction = 'N';

            // Set of all positions I visited
            HashSet<Tuple<int, int>> easterBunnyPosition = new HashSet<Tuple<int, int>>();
            int easterBunnyDistance = 0;
            bool easterBunnyFlag = false;

            // Amount of steps to take in the instruction
            int amount = 0;
            foreach (string instruction in instructions)
            {
                amount = int.Parse(instruction.Substring(1, instruction.Length - 1));
                switch (direction.ToString() + instruction[0].ToString())
                {
                    case "EL":
                    case "WR":
                        // Taking the amount of steps and remembering all positions I visited
                        for (int i = 0; i < amount; i++)
                        {
                            y += 1;
                            if (!easterBunnyPosition.Add(new Tuple<int, int>(x, y)) && !easterBunnyFlag)
                            {
                                easterBunnyDistance = Math.Abs(x) + Math.Abs(y);
                                easterBunnyFlag = true;
                            }
                        }
                        direction = 'N';
                        break;
                    case "ER":
                    case "WL":
                        // Taking the amount of steps and remembering all positions I visited
                        for (int i = 0; i < amount; i++)
                        {
                            y -= 1;
                            if (!easterBunnyPosition.Add(new Tuple<int, int>(x, y)) && !easterBunnyFlag)
                            {
                                easterBunnyDistance = Math.Abs(x) + Math.Abs(y);
                                easterBunnyFlag = true;
                            }
                        }
                        direction = 'S';
                        break;
                    case "NR":
                    case "SL":
                        // Taking the amount of steps and remembering all positions I visited
                        for (int i = 0; i < amount; i++)
                        {
                            x += 1;
                            if (!easterBunnyPosition.Add(new Tuple<int, int>(x, y)) && !easterBunnyFlag)
                            {
                                easterBunnyDistance = Math.Abs(x) + Math.Abs(y);
                                easterBunnyFlag = true;
                            }
                        }
                        direction = 'E';
                        break;
                    case "NL":
                    case "SR":
                        // Taking the amount of steps and remembering all positions I visited
                        for (int i = 0; i < amount; i++)
                        {
                            x -= 1;
                            if (!easterBunnyPosition.Add(new Tuple<int, int>(x, y)) && !easterBunnyFlag)
                            {
                                easterBunnyDistance = Math.Abs(x) + Math.Abs(y);
                                easterBunnyFlag = true;
                            }
                        }
                        direction = 'W';
                        break;
                }
            }
            WriteLine("The block is " + (Math.Abs(x)+Math.Abs(y)) + " blocks away from the dropoff point!");
            WriteLine("EasterBunny is " + easterBunnyDistance + " blocks away from the dropoff point!");
        }

        // Taking the amount of steps and remembering all positions I visited
        private static void iteration(int amount, ref int x, ref int y, ref HashSet<Tuple<int, int>> easterBunnyPosition, ref int easterBunnyDistance, ref bool easterBunnyFlag)
        {
            for (int i = 0; i < amount; i++)
            {
                x -= 1;
                if (!easterBunnyPosition.Add(new Tuple<int, int>(x, y)) && !easterBunnyFlag)
                {
                    easterBunnyDistance = Math.Abs(x) + Math.Abs(y);
                    easterBunnyFlag = true;
                }
            }
        }
    }
}

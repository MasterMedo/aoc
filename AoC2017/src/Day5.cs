using System;
using System.Collections.Generic;

namespace AoC_2017
{
    class Day5
    {
        public static void Solution()
        {
            string line;
            List<int> list = new List<int>();
            System.IO.StreamReader input = new System.IO.StreamReader(@"C:\Users\MasterMedo\Source\Repos\AdventOfCode\AoC2017\inputs\p05.txt");
            while ((line = input.ReadLine()) != null)
            {
                list.Add(int.Parse(line));
            }
            int  index = 0;
            int current = 0;
            int counter = 0;
            bool flag = false;
            while (!flag)
            {
                try
                {
                    // Solution 1: i = -list[current]++;
                    index = -list[current];
                    // Solution 1: Remove if-else block
                    if (-index >= 3) list[current]--;
                    else list[current]++;
                    current = current - index;
                    counter++;
                } catch(Exception)
                {
                    Console.WriteLine("Solution to part 2 is: " + counter);
                    flag = true;
                }
            }
        }
    }
}

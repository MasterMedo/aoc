using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC_2017
{
    class Day8
    {
        public static void Solution()
        {
            int max = 0;
            string line;
            Dictionary<string, int> dict = new Dictionary<string, int>();
            System.IO.StreamReader input = new System.IO.StreamReader(@"C:\Users\MasterMedo\Source\Repos\AdventOfCode\AoC2017\inputs\Day8_input.txt");
            while ((line = input.ReadLine()) != null)
            {
                bool flag = false;
                string[] list = line.Split(' ');
                if (!dict.ContainsKey(list[4])) dict.Add(list[4], 0);
                switch (list[5])
                {
                    case "<":
                        if (dict[list[4]] < int.Parse(list[6])) flag = true;
                        break;
                    case "<=":
                        if (dict[list[4]] <= int.Parse(list[6])) flag = true;
                        break;
                    case ">":
                        if (dict[list[4]] > int.Parse(list[6])) flag = true;
                        break;
                    case ">=":
                        if (dict[list[4]] >= int.Parse(list[6])) flag = true;
                        break;
                    case "==":
                        if (dict[list[4]] == int.Parse(list[6])) flag = true;
                        break;
                    case "!=":
                        if (dict[list[4]] != int.Parse(list[6])) flag = true;
                        break;
                }
                if(!dict.ContainsKey(list[0])) dict.Add(list[0], 0);
                if (list[1] == "inc" && flag) dict[list[0]] += int.Parse(list[2]);
                else if (list[1] == "dec" && flag) dict[list[0]] -= int.Parse(list[2]);
                if (max < dict.Values.Max()) max = dict.Values.Max();
            }
            Console.WriteLine("The largest value in the end is: " + dict.Values.Max());
            Console.WriteLine("The largest value ever is: " + max);
        }
    }
}

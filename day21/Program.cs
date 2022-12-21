



using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.Design.Serialization;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text.RegularExpressions;
using adventOfCodeDag21;
BigInteger FindValueRec(IReadOnlyDictionary<string, Monkey> dict, Monkey monkey)
{
    if (BigInteger.TryParse(monkey.value, out var val))
    {
        return val;
    }

    var pattern = "([a-z]{4}) ([*/+-=]{1}) ([a-z]{4})";
    // Create a Regex  
    var rg = new Regex(pattern);
    var res = rg.Match(monkey.value);
    var mon1 = res.Groups.Values.ToArray()[1].Value;
    var sign = res.Groups.Values.ToArray()[2].Value;
    var mon2 = res.Groups.Values.ToArray()[3].Value;
   
    var s = sign switch
    {
        "*" => FindValueRec(dict, dict[mon1]) * FindValueRec(dict, dict[mon2]),
        "+" => FindValueRec(dict, dict[mon1]) + FindValueRec(dict, dict[mon2]),
        "-" => FindValueRec(dict, dict[mon1]) - FindValueRec(dict, dict[mon2]),
        "/" => FindValueRec(dict, dict[mon1]) / FindValueRec(dict, dict[mon2]),
        "=" => FindValueRec(dict, dict[mon1]) == FindValueRec(dict, dict[mon2]) ? 1 : 0,
        _ => throw new Exception()
    };
    return s;
}


bool HasHumnInTree(IReadOnlyDictionary<string, Monkey> dict, Monkey monkey)
{
    if (monkey.Name == "humn")
    {
        return true;
    }
    else if (BigInteger.TryParse(monkey.value, out var val))
    {
        return false;
    }

    var pattern = "([a-z]{4}) ([*/+-=]{1}) ([a-z]{4})";
    // Create a Regex  
    var rg = new Regex(pattern);
    var res = rg.Match(monkey.value);
    var mon1 = res.Groups.Values.ToArray()[1].Value;
    var mon2 = res.Groups.Values.ToArray()[3].Value;
    return HasHumnInTree(dict, dict[mon1]) || HasHumnInTree(dict, dict[mon2]);
}


var monkeys = System.IO.File.ReadLines("./input.txt").Select(line => line.Split(": ")).Select(s => new Monkey { Name = s[0], value = s[1] }).ToList();

Dictionary<string, Monkey> dict = new Dictionary<string, Monkey>();

foreach (var monkey in monkeys)
{
    dict.Add(monkey.Name, monkey);
}

var root = dict["root"];

Console.WriteLine("part 1: " + FindValueRec(dict,root));


dict["root"].value = dict["root"].value.Replace("+", "=");

var humnNotFound = true;

var branches = root.value.Split(" = ");
var a = HasHumnInTree(dict, dict[branches[0]]);
BigInteger mustEqual;
Monkey tooCheck;
if (a)
{
    mustEqual = FindValueRec(dict, dict[branches[1]]);
    tooCheck = dict[branches[0]];
}
else
{
    mustEqual = FindValueRec(dict, dict[branches[0]]);
    tooCheck = dict[branches[1]];
}

while (humnNotFound)
{

    if (tooCheck.Name == "humn")
    {
        humnNotFound = false;
    }
    else
    {
        var pattern = "([a-z]{4}) ([*/+-=]{1}) ([a-z]{4})";
        // Create a Regex  
        var rg = new Regex(pattern);
        var res = rg.Match(tooCheck.value);
        var mon1 = res.Groups.Values.ToArray()[1].Value;
        var sign = res.Groups.Values.ToArray()[2].Value;
        var mon2 = res.Groups.Values.ToArray()[3].Value;

        bool left = HasHumnInTree(dict, dict[mon1]);

        if (left)
        {
            var valRight = FindValueRec(dict, dict[mon2]);

            mustEqual = sign switch
            {
                "+" => mustEqual - valRight,
                "-" => mustEqual + valRight,
                "*" => mustEqual / valRight,
                "/" => mustEqual * valRight,
                _ => mustEqual
            };

            tooCheck = dict[mon1];
        }
        else
        {
            var valLeft = FindValueRec(dict, dict[mon1]);

            mustEqual = sign switch
            {
                "+" => mustEqual - valLeft,
                "-" => valLeft - mustEqual,
                "*" => mustEqual / valLeft,
                "/" => valLeft / mustEqual,
                _ => mustEqual
            };
            tooCheck = dict[mon2];
        }
    }
    
}

Console.WriteLine("part 2: " + mustEqual);




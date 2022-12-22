
using System.Runtime.InteropServices;
using Microsoft.VisualBasic;
using static System.Char;
using static System.Console;




var lines = System.IO.File.ReadLines("./input.txt").ToList();

var instrucs = "";
var lineCount = 0;
var right = new Dictionary<string, string>
{
    { "R", "D" },
    { "D", "L" },
    { "L", "U" },
    { "U", "R" }
};

var left = new Dictionary<string, string>
{
    { "R", "U" },
    { "D", "R" },
    { "L", "D" },
    { "U", "L" }
};




var map = new Dictionary<Point, char>();
foreach (var line in lines)
{
    if (line.Contains("R"))
    {
        instrucs = line;
    }

    int charcount = 0;
    foreach (var x in line)
    {
        if (x is '#' or '.')
        {
            map.Add(new Point(charcount, lineCount), x);
        }

        charcount++;
    }

    lineCount++;

}

var minx = map.Keys.Where(k => k.Y == 0).Min(k => k.X);
var point = map.Keys.First(k => k.Y == 0 && k.X == minx);
var direction = "R";

var currInt = "";

foreach (var c in instrucs)
{
    if (IsDigit(c))
    {
        currInt += c;
    }
    else
    {
        var moves = int.Parse(currInt);
        point = MoveXTimes(point, moves, direction, map);

        if (c == 'R')
        {
            direction = right[direction];
        }
        else
        {
            direction = left[direction];
        }

        currInt = "";
    }
}

var movesRemaining = int.Parse(currInt);
point = MoveXTimes(point, movesRemaining, direction, map);

int dirPoints = direction switch
{
    "R" => 0,
    "D" => 1,
    "L" => 2,
    "U" => 3,
    _ => 0
};
var result = (1000 * (point.Y + 1)) + (4 * (point.X + 1)) + dirPoints;
WriteLine("part1: " + result);


minx = map.Keys.Where(k => k.Y == 0).Min(k => k.X);
point = map.Keys.First(k => k.Y == 0 && k.X == minx);
direction = "R";


currInt = "";

foreach (var c in instrucs)
{
    if (IsDigit(c))
    {
        currInt += c;
    }
    else
    {
        var moves = int.Parse(currInt);
        point = MovePart2(point, moves, direction, map, out var newDirection);

        direction = newDirection;
        if (c == 'R')
        {
            direction = right[direction];
        }
        else
        {
            direction = left[direction];
        }

        currInt = "";
    }
}

movesRemaining = int.Parse(currInt);
point = MovePart2(point, movesRemaining, direction, map, out var finalDirection);


dirPoints = finalDirection switch
{
    "R" => 0,
    "D" => 1,
    "L" => 2,
    "U" => 3,
    _ => 0
};
result = (1000 * (point.Y + 1)) + (4 * (point.X + 1)) + dirPoints;
WriteLine("part2: " + result);




//part one solution
Point MoveXTimes(Point point, int i, string direction, Dictionary<Point, char> map)
{
    while (i > 0)
    {
        i--;

        Point nextPoint = null;
        switch (direction)
        {
            case "R":
                {
                    nextPoint = new Point(point.X + 1, point.Y);
                    if (!map.ContainsKey(nextPoint))
                    {
                        var minx = map.Keys.Where(k => k.Y == point.Y).Min(k => k.X);
                        nextPoint = map.Keys.First(k => k.Y == point.Y && k.X == minx);
                    }

                    break;
                }
            case "L":
                {
                    nextPoint = new Point(point.X - 1, point.Y);
                    if (!map.ContainsKey(nextPoint))
                    {
                        var maxX = map.Keys.Where(k => k.Y == point.Y).Max(k => k.X);
                        nextPoint = map.Keys.First(k => k.Y == point.Y && k.X == maxX);
                    }

                    break;
                }
            case "D":
                {
                    nextPoint = new Point(point.X, point.Y + 1);
                    if (!map.ContainsKey(nextPoint))
                    {
                        var miny = map.Keys.Where(k => k.X == point.X).Min(k => k.Y);
                        nextPoint = map.Keys.First(k => k.Y == miny && k.X == point.X);
                    }

                    break;
                }
            case "U":
                {
                    nextPoint = new Point(point.X, point.Y - 1);
                    if (!map.ContainsKey(nextPoint))
                    {
                        var maxy = map.Keys.Where(k => k.X == point.X).Max(k => k.Y);
                        nextPoint = map.Keys.First(k => k.Y == maxy && k.X == point.X);
                    }

                    break;
                }
        }

        if (map[nextPoint] == '.')
        {
            point = nextPoint;
        }
        else
        {
            break;
        }

    }

    return point;
}


// Ã†***************Hard coding part 2 for my input because im too dumb**************************

Point MovePart2(Point point, int i, string direction, Dictionary<Point, char> map, out string newDirection)
{
   
    while (i > 0)
    {
        i--;

        newDirection = "";
        Point nextPoint = null;
        switch (direction)
        {
            case "R":
                {
                    nextPoint = new Point(point.X + 1, point.Y);
                    if (!map.ContainsKey(nextPoint))
                    {
                        nextPoint = WrapAroundPart2(point, direction, out newDirection);
                    }

                    break;
                }
            case "L":
                {
                    nextPoint = new Point(point.X - 1, point.Y);
                    if (!map.ContainsKey(nextPoint))
                    {
                        nextPoint = WrapAroundPart2(point, direction, out newDirection);
                    }

                    break;
                }
            case "D":
                {
                    nextPoint = new Point(point.X, point.Y + 1);
                    if (!map.ContainsKey(nextPoint))
                    {
                        nextPoint = WrapAroundPart2(point, direction, out newDirection);
                    }

                    break;
                }
            case "U":
                {
                    nextPoint = new Point(point.X, point.Y - 1);
                    if (!map.ContainsKey(nextPoint))
                    {
                        nextPoint = WrapAroundPart2(point, direction, out newDirection);
                    }

                    break;
                }
        }

        if (map[nextPoint] == '.')
        {
            point = nextPoint;
            if (newDirection != "")
            {
                direction = newDirection;
            }
        }
        else
        {
            break;
        }

        
    }

    newDirection = direction;
    return point;
}

Point WrapAroundPart2(Point point, string oldDirection, out string direction)
{
    //find the cube face for the point we are currently on.
    //we know we are wrapping so find the correct wrap based on point and direction to the new side
    var cubeface = FindCubeFace(point);
    Point newPoint = cubeface switch
    {
        "b" => FindPointB(point, oldDirection, out direction),
        "rs" => FindPointRs(point, oldDirection, out direction),
        "ds" => FindPointDs(point, oldDirection, out direction),
        "t" => FindPointT(point, oldDirection, out direction),
        "ls" => FindPointLs(point, oldDirection, out direction),
        _ => FindPointUs(point, oldDirection, out direction)
    };

    return newPoint;
}

Point FindPointB(Point point, string oldDirection, out string direction)
{
    if (point.Y == 0 && oldDirection == "U")
    {
        direction = "R";
        return new Point(0, 150 + (point.X - 50));
    }

    direction = "R";
    return new Point(0, 100 + (49 - point.Y));
}

Point FindPointRs(Point point, string oldDirection, out string direction)
{
    if (point.Y == 0 && oldDirection == "U")
    {
        direction = "U";
        return new Point(point.X - 100, 199);
    }
    else if (point.Y == 49 && oldDirection == "D")
    {
        direction = "L";
        return new Point(99, 50 + (point.X - 100));
    }
    else
    {
        direction = "L";
        return new Point(99, 149 - point.Y);
    }
}

Point FindPointDs(Point point, string oldDirection, out string direction)
{
    if (point.X == 50 && oldDirection == "L")
    {
        direction = "D";
        return new Point((point.Y - 50), 100);
    }

    direction = "U";
    return new Point(100 + (point.Y - 50), 49);

}

Point FindPointT(Point point, string oldDirection, out string direction)
{
    if (point.X == 99 && oldDirection == "R")
    {
        direction = "L";
        return new Point(149, 49 - (point.Y - 100));
    }

    direction = "L";
    return new Point(49, 150 + (point.X - 50));
}

Point FindPointLs(Point point, string oldDirection, out string direction)
{
    if (point.X == 0 && oldDirection == "L")
    {
        direction = "R";
        return new Point(50, 49 - (point.Y - 100));
    }

    direction = "R";
    return new Point(50, 50 + point.X);
}


Point FindPointUs(Point point, string oldDirection, out string direction)
{
    if (point.X == 0 && oldDirection == "L")
    {
        direction = "D";
        return new Point(50 + (point.Y - 150), 0);
    }

    else if (point.Y == 199 && oldDirection == "D")
    {
        direction = "D";
        return new Point(100 + point.X, 0);
    }

    direction = "U";
    return new Point(50 + (point.Y - 150), 149);
}

string FindCubeFace(Point point)
{
    return point.X switch
    {
        >= 50 and < 100 when point.Y is >= 0 and < 50 => "b",
        >= 100 and < 150 when point.Y is >= 0 and < 50 => "rs",
        >= 50 and < 100 when point.Y is >= 50 and < 100 => "ds",
        >= 50 and < 100 when point.Y is >= 100 and < 150 => "t",
        >= 0 and < 50 when point.Y is >= 100 and < 150 => "ls",
        _ => "us"
    };
}


internal class Point : IEquatable<Point>
{
    public int X { get; set; }
    public int Y { get; set; }

    public Point(int x, int y)
    {
        this.X = x; this.Y = y;
    }

    public bool Equals(Point? other)
    {
        if (ReferenceEquals(null, other)) return false;
        if (ReferenceEquals(this, other)) return true;
        return X == other.X && Y == other.Y;
    }

    public override bool Equals(object? obj)
    {
        if (ReferenceEquals(null, obj)) return false;
        if (ReferenceEquals(this, obj)) return true;
        if (obj.GetType() != this.GetType()) return false;
        return Equals((Point)obj);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(X, Y);
    }
}
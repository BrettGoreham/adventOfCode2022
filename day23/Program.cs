
var lines = System.IO.File.ReadLines("./input.txt").ToList();

var lineCount = 0;
var elves = new Dictionary<Point, Point?>();
while (lineCount < lines.Count())
{
    var line = lines[lineCount];

    var charcount = 0;
    while (charcount < line.Length)
    {
        if (line[charcount] == '#')
        {
            elves.Add(new Point(charcount, lineCount), null);
        }

        charcount++;
    }
    lineCount++;
    
} 

var searchOrder = new List<string>{"N", "S", "W", "E"};

var roundcount = 0;
var moved = true;

while (moved)
{
    if (roundcount == 10)
    {
        Console.WriteLine("part 1: " + GetScore(elves));

    }

    var movedThisRound = false;
    foreach (var elf in elves.Keys)
    {
        var nothingAround = CheckNothingAround(elf, elves);

        if (!nothingAround)
        {
            var searching = true;
            var searchCount = 0;
            while (searching)
            {
                if (searchCount >= searchOrder.Count)
                {
                    searching = false;
                }
                else
                {
                    var elvesFound = SearchForElvesInDirection(searchOrder[searchCount], elf, elves);

                    if (!elvesFound)
                    {
                        searching = false;
                        elves[elf] = GetPointInDirection(elf, searchOrder[searchCount]);
                    }

                }

                searchCount++;
            }
        }
        
    }

    var distinctGoals = elves.Values.Where(x => x != null)
        .GroupBy(z => z)
        .Where(x => x.Count() == 1)
        .Select(x => x.Key)
        .ToList();
    var movedElves = new Dictionary<Point, Point?>();
    foreach (var elf in elves)
    {
        if (elf.Value == null || !distinctGoals.Contains(elf.Value))
        {
            movedElves.Add(elf.Key, null);
        }
        else
        {
            movedThisRound = true;
            movedElves.Add(elf.Value, null);
        }
    }

    moved = movedThisRound;
    roundcount++;
    elves = movedElves;
    searchOrder.Add(searchOrder[0]);
    searchOrder.RemoveAt(0);
}

PrintElfMap(elves);
Console.WriteLine("part 2 round where everything stationary: " + roundcount);



int GetScore(Dictionary<Point, Point?> dictionary)
{
    var minx = dictionary.Keys.Select(k => k.X).Min();
    var maxx = dictionary.Keys.Select(k => k.X).Max();
    var miny = dictionary.Keys.Select(k => k.Y).Min();
    var maxy = dictionary.Keys.Select(k => k.Y).Max();


    return (maxx - minx + 1) * (maxy - miny + 1) - dictionary.Count;
}


bool CheckNothingAround(Point point, Dictionary<Point, Point?> dictionary)
{
    var toCheck = new List<Point>
    {
        new Point(point.X, point.Y + 1),
        new Point(point.X - 1, point.Y + 1),
        new Point(point.X + 1, point.Y + 1),
        new Point(point.X + 1, point.Y),
        new Point(point.X + 1, point.Y - 1),
        new Point(point.X, point.Y - 1),
        new Point(point.X - 1, point.Y - 1),
        new Point(point.X - 1, point.Y)
    };

    return toCheck.All(p => !dictionary.ContainsKey(p));
}

void PrintElfMap(IReadOnlyDictionary<Point, Point> dictionary)
{
    var minx = dictionary.Keys.Select(k => k.X).Min();
    var maxx = dictionary.Keys.Select(k => k.X).Max();
    var miny = dictionary.Keys.Select(k => k.Y).Min();
    var maxy = dictionary.Keys.Select(k => k.Y).Max();

    Console.WriteLine("\n");
    for (var y = miny; y <= maxy; y++)
    {
        var s = "";
        for (var x = minx; x <= maxx; x++)
        {
            if (dictionary.ContainsKey(new Point(x, y)))
            {
                s += "#";
            }
            else
            {
                s += ".";
            }
        }

        Console.WriteLine(s);
    }
}
Point GetPointInDirection(Point point, string s)
{
    switch (s)
    {
        case "N":
            return new Point(point.X, point.Y - 1);
        case "S":
            return new Point(point.X, point.Y + 1);
        case "E":
            return new Point(point.X + 1, point.Y);
        case "W":
            return new Point(point.X - 1, point.Y);
        default:
            throw new Exception("no direction");
    }
}

static bool SearchForElvesInDirection(string s, Point point, IReadOnlyDictionary<Point, Point> dictionary)
{
    var listPointsToSearch = new List<Point>();
    switch (s)
    {
        case "N":
            listPointsToSearch.Add(new Point(point.X, point.Y -1));
            listPointsToSearch.Add(new Point(point.X - 1, point.Y - 1));
            listPointsToSearch.Add(new Point(point.X + 1, point.Y - 1));
            break;
        case "S":
            listPointsToSearch.Add(new Point(point.X, point.Y + 1));
            listPointsToSearch.Add(new Point(point.X - 1, point.Y + 1));
            listPointsToSearch.Add(new Point(point.X + 1, point.Y + 1));
            break;
        case "E":
            listPointsToSearch.Add(new Point(point.X + 1, point.Y));
            listPointsToSearch.Add(new Point(point.X + 1, point.Y + 1));
            listPointsToSearch.Add(new Point(point.X + 1, point.Y - 1));
            break;
        case "W":
            listPointsToSearch.Add(new Point(point.X - 1, point.Y));
            listPointsToSearch.Add(new Point(point.X - 1, point.Y + 1));
            listPointsToSearch.Add(new Point(point.X - 1, point.Y - 1));
            break;
        default:
            throw new Exception("no direction");
    }

    return dictionary.ContainsKey(listPointsToSearch[0]) || dictionary.ContainsKey(listPointsToSearch[1]) ||
           dictionary.ContainsKey(listPointsToSearch[2]);

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
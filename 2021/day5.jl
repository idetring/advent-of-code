const Point = NamedTuple{(:x, :y), Tuple{Int, Int}}
topoint(x, y) = (x = x, y = y)

# Type alias and constructors for `Slope`
const Slope = NamedTuple{(:dx, :dy), Tuple{Int, Int}}
toslope(dx, dy) = (dx = dx, dy = dy)

function getslope(a::Point, b::Point)::Slope
    (xdiff, ydiff) = (b.x - a.x, b.y - a.y)
    xygcd = gcd(xdiff, ydiff)
    (dx, dy) = (xdiff ÷ xygcd, ydiff ÷ xygcd)
    toslope(dx, dy)
end

# Represents a line from point `a` to point `b`
struct Line
    a::Point
    b::Point
    slope::Slope
end

Line(a::Point, b::Point) = Line(a, b, getslope(a, b))

function Line(s::AbstractString)::Line
    re = r"(\d+),(\d+) -> (\d+),(\d+)"
    rematch = match(re, s)
    (x1, y1, x2, y2) = parse.(Int, rematch.captures)
    pointa = topoint(x1, y1)
    pointb = topoint(x2, y2)
    Line(pointa, pointb)
end


# Ingestion -------------------------------------------------------------------

# Read input from a file path
function ingest(path)
    open(path) do f
        [Line(s) for s in readlines(f)]
    end
end


# Iterator Implementation -----------------------------------------------------

# Iterator interface implementations for `Line`
Base.iterate(line::Line) = (line.a, line.a)
Base.eltype(::Type{Line}) = Point

function Base.iterate(line::Line, lastpoint::Point)
    lastpoint == line.b && return nothing
    nextpoint = lastpoint + line.slope
    (nextpoint, nextpoint)
end

function Base.length(line::Line) 
    (a, b) = (line.a, line.b)
    return max(abs(b.x - a.x), abs(b.y - a.y)) + 1
end


# Operator Overloads ----------------------------------------------------------

# Operator overloading for adding a `Slope` to a `Point`
function Base.:+(point::Point, slope::Slope)::Point
    (x, y) = (point.x + slope.dx, point.y + slope.dy)
    topoint(x, y)
end

# Operator overloading for comparing `Points`
function Base.:(==)(a::Point, b::Point)
    a.x == b.x && a.y == b.y
end

# Solve Part One --------------------------------------------------------------

function ishorizontal(line)
    line.slope[1] == 0 
end
function isvertical(line)
    line.slope[2] == 0
end

function part1(input)
    pointsmap = zeros(Int64, 1000, 1000)
    for line in input
        (isvertical(line) || ishorizontal(line)) || continue
        points = collect(line)
        for (x, y) in points
            pointsmap[x, y] += 1
        end
    end


    count(x -> x > 1, pointsmap)
end

function part2(input)
    pointsmap = zeros(Int64, 1000, 1000)
    for line in input
        points = collect(line)
        for (x, y) in points
            pointsmap[x, y] += 1
        end
    end

    count(x -> x > 1, pointsmap)
end


input= ingest("2021/input/day5.txt")
part1(input)
part2(input)
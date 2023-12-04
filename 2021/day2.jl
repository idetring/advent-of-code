## Day 1 ....

mutable struct Position
    X::Int
    Y::Int
end

function forward(Pos,n)
    Pos.X = Pos.X + n
end

function down(Pos,n)
    Pos.Y = Pos.Y + n
end

function up(Pos,n)
    Pos.Y = Pos.Y - n
end

struct GoTo
    dir
    num::Int
end



input = open("2021/input/day2.txt") do f
    map(s -> GoTo(getfield(Main,Symbol(split(s)[1])) , parse(Int,split(s)[2])) , readlines(f))
#    [parse(Int, s) for s in readlines(f)]
end


function D2P1(input)
    submarine = Position(0,0)
    for gt in input
        gt.dir(submarine,gt.num)
    end
    return submarine
end

@time D2P1(input)

result = D2P1(input)
result = result.X * result.Y


## Part2

# adding aim to structure
mutable struct PositionExt
    X::Int
    Y::Int
    aim::Int
end

# new functions....
function forward(Pos,n)
    Pos.X = Pos.X + n
    Pos.Y = Pos.Y + n * Pos.aim
end

function down(Pos,n)
    Pos.aim = Pos.aim + n
end

function up(Pos,n)
    Pos.aim = Pos.aim - n
end


function D2P1(input)
    submarine = PositionExt(0,0,0)
    for gt in input
        gt.dir(submarine,gt.num)
    end
    return submarine
end


@time D2P1(input)

result = D2P1(input)
result = result.X * result.Y


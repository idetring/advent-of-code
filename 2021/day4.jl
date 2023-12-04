abstract type AbstractIndexType end
struct RowIndex <: AbstractIndexType idx::Int end
struct ColIndex <: AbstractIndexType idx::Int end

mutable struct Board
    indexmap::Dict{Int, Int}
    numbers::Matrix{Int}
    found::BitMatrix
    linecounts::Dict{AbstractIndexType, Int}
end

function Board(numbers::Matrix) 
    # Build the `indexmap`
    mapnumbers(n) = map(i -> (numbers[i], i), n)
    (indexmap
        =  numbers
        |> eachindex
        |> mapnumbers
        |> Dict)
    
    found = falses(size(numbers))
    linecounts = Dict()
    Board(indexmap, numbers, found, linecounts)
end

function read_Day4()
    open("2021/input/day4.txt") do f
    
        s = readuntil(f,"\n\n")
        Draws = parse.(Int,split(s,','))
    
        Boards = []
        while !eof(f)
            s = readuntil(f,"\n\n")
            numbers = [split(st) for st in split(s,"\n")]
            numbers = reduce(hcat,numbers)
            numbers = parse.(Int,numbers)
            numbers = Board(collect(numbers'))
            push!(Boards,numbers)
        end
        (Draws,Boards)
    end
end


function play!(number,board)
    haskey(board.indexmap,number) || return false

    pos = get(board.indexmap,number,0)
    board.found[pos] = true

    (row, col) = Tuple(CartesianIndices(board.numbers)[pos])
    winner = false
    linekeys = [RowIndex(row),ColIndex(col)]
    for key in linekeys
        linecount = get(board.linecounts, key, 0)
        board.linecounts[key] = linecount + 1
        if linecount + 1 >= 5; winner = true; end
    end

    return winner
end


function D4P1(input)
    Draws=input[1]
    Boards=input[2]
    while !isempty(Draws)
        draw = popfirst!(Draws)
        for board in Boards
            if play!(draw,board)
                unmarked = board.numbers[.!board.found]
                return sum(unmarked) * draw
            end
        end
    end
    error("No board has won...")
end

input = read_Day4()
D4P1(input)


function D4P2(input)
    Draws=input[1]
    Boards=input[2]
    haswon=zeros(Bool,length(Boards))
    while !isempty(Draws)
        draw = popfirst!(Draws)
        for (i,board) in Iterators.enumerate(Boards)
            if play!(draw,board)
                haswon[i] = true
                if all(haswon)
                    @show i
                    unmarked = board.numbers[.!board.found]
                    return sum(unmarked) * draw
                end
            end
        end
    end
    error("No board has won...")
end

input = read_Day4()
D4P2(input)
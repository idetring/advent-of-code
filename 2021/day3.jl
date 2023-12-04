
process(s::AbstractString)::Vector{Bool} = split(s, "") .== "1"

input = open("2021/input/day3.txt") do f

        bitvecs = [process(s) for s in readlines(f)]
        bitmatrix = reduce(hcat, bitvecs)
        transpose(bitmatrix)
end

function mostcommon(arr)::Bool
    trues = count(arr)
    trues >= (length(arr) - trues)
end

function Base.convert(t::Type{Int}, bv::BitVector)
    (powers
        =  (length(bv)-1:-1:0)
        |> collect
        |> (x -> x[bv]))
    sum(2 .^ powers)
end

function D3P1(input)
    (gamma
        = eachcol(input)
        |> (x -> map(mostcommon, x))
        |> BitVector)
    epsilon = .!gamma

    convert(Int, gamma) * convert(Int, epsilon)
end

D3P1(input)




function D3P2(input)
    gamma="0b"
    epsilon="0b"    
    oxid=""
    co2=""
    tmp = [[parse(Int,string(j[i])) for j in input] for i in 1:length(input[1])]
    for i in tmp
        a = sum(i)
        b = length(i) - a
        a > b ? gamma*="1" : gamma*="0"
        a > b ? epsilon*="0" : epsilon*="1"
    end
    gamma = parse(Int,gamma)
    epsilon = parse(Int,epsilon)
    return gamma * epsilon
end

D3P1(input)


function getrating(input,in)
    out = "0b"
    for i in eachindex(in)
        tmp = input[startswith.(input,in[1:i])]
        @show (in,tmp)
        length(tmp) == 1 ? out *= tmp[1] : nothing
    end
    return out
end
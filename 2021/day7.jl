using Statistics

function read_Day7()
    out = open("2021/input/day7.txt") do f
        [parse.(Int,split(s,',')) for s in readlines(f)]
    end
    reduce(hcat,out)
end
input = read_Day7()
input = [16,1,2,0,4,2,7,1,2,14]

# input - Y = constant

# input - const = Y


function D7P1(input)
    fuel(input,pos) = sum(abs.(input .- pos))
    a = minimum(input)
    b = maximum(input)
    tot = (0,1e+10)
    for i in a:b
        tmp = fuel(input,i)
        tmp < tot[2] ? tot = (i,tmp) : nothing
    end
    return tot
end

D7P1(input)

littlegaus(n) = n*(n+1)/2

function D7P2(input)
    fuel(input,pos) = sum(littlegaus.(big.(abs.(input .- pos))))
    a = minimum(input)
    b = maximum(input)
    tot = (0,big(100000000))
    for i in a:b
        tmp = fuel(input,i)
        tmp < tot[2] ? tot = (i,tmp) : nothing
    end
    return tot
end

a = D7P2(input)
## Day 1 ....
#-- Task: count the number of times a depth measurement increases from the previous measurement. 
# - (There is no measurement before the first measurement.)

input = open("2021/input/day1.txt") do f
    [parse(Int, s) for s in readlines(f)]
end

function D1P1(input)
    sum(diff(input) .> 0)
end

result_D1P1 = D1P1(input)
# part two

function rolling_sum(a, n::Int)
    @assert 1<=n<=length(a)
    out = similar(a, length(a)-n+1)
    out[1] = sum(a[1:n])
    for i in eachindex(out)[2:end]
        out[i] = out[i-1]-a[i-1]+a[i+n-1]
    end
    return out
end

function D1P2(input,n::Int=3)
    D1P1(rolling_sum(input,n))
end

result_D1P2 = D1P2(input,3)


function counter()
    count = 0
    return function()
        count+=1
        return count
    end
end


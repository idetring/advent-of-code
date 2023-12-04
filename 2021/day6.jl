function initialize(input)
    ages = Dict()
    for i in 0:8
        ages[i] = 0
    end

    u = unique(input)
    for u in unique(input)
        s = length(findall(input .== u))
        ages[u] = s
    end
    return ages
end

function day!(ages)
    old = copy(ages)
    newfish = ages[0]
    for i in 1:8
        ages[i-1] = old[i]
    end
    ages[6] = ages[6] + newfish
    ages[8] = newfish
    return
end

function sumfish(ages)
    total = 0 
    for i in 0:8
        total += ages[i]
    end
    return total
end


function D6P1(input,days)
    ages = initialize(input)
    while days >0
        day!(ages)
        days -= 1
    end

    sumfish(ages)
end


input = open("Day6_input.txt") do f 
    [parse.(Int,split(s,","))  for s in readlines(f)]
end

D6P1(input[1],256)



### ALTERNATE SOLUTION:::

function ingest(path)
    fish = open(path) do f
        readsplit(x) = split(readchomp(x), ",")
        [parse(Int, s) for s in readsplit(f)]
    end

    # Instead of reporting back the fish individually, return a
    # Vector of length `9` where each index represents the number 
    # of fish of age `idx - 1` . (Julia is 1-indexed)
    groups = zeros(Int64, 9)
    for f in fish
        groups[f+1] += 1
    end
    return groups
end


struct School
    agegroups::Vector{Int64}
end

# This function is called for the first iteration
function Base.iterate(iter::School)
    groups = copy(iter.agegroups)
    (sum(groups), groups)
end

# This function is called for each subsequent iteration
# Instead of keeping track of each fish and its progeny, we group all
# the fish by age and calculate the size of the next generation. Each
# generation/iteration creates `groups[1]` new fish at age `8` and rotates
# the group counts one to the left (such that the fish that were age `2` 
# are now age `1`)
function Base.iterate(iter::School, groups::Vector{Int64})
    groups = circshift(groups, -1)
    groups[7] += groups[9]
    (sum(groups), groups)
end

# Used to get the `nth` generation of a school. 
function Base.getindex(school::School, i::Int)
    for (generation, groups) in enumerate(school)
        generation > i && return groups
    end
end


# Solve the puzzle ------------------------------------------------------------

# Solve the puzzle, creating an iterator over generations of a 
# `School` and summing the values for a given day.
function solve(input, days)
    school = School(input)
    return sum(school[days])
end

input = ingest("2021/input/day6.txt")
solve(input,80)
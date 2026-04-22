function resize(maze, new_size)
    m, n = size(maze)
    new_maze = zeros(new_size*m, new_size*n)

    for i in 0:m-1
        for new_row in 1:new_size
            for j in 0:n-1
                for new_column in 1:new_size
                    new_maze[i*new_size+new_row, j*new_size+new_column] = maze[i+1, j+1]
                end
            end
        end 
    end

    return new_maze
end

bd57 = Dict(
    "000" => false,
    "001" => true,
    "010" => true,
    "011" => true,
    "100" => true,
    "101" => false,
    "110" => false,
    "111" => false,
)

bd32 = Dict(
    "000" => false,
    "001" => true,
    "010" => true,
    "011" => true,
    "100" => true,
    "101" => false,
    "110" => false,
    "111" => false,
)

bdtest = Dict(
    "000" => true,
    "001" => false,
    "010" => false,
    "011" => false,
    "100" => true,
    "101" => true,
    "110" => false,
    "111" => false,
)

function ruleTest(c1::Bool, c2::Bool, c3::Bool)
    return bdtest[toB(c1)*toB(c2)*toB(c3)]
end

function toB(b::Bool)
    return b ? "1" : "0"
end

# function rule57(c1::Bool, c2::Bool, c3::Bool)
#     return bd["$c1"] 
# end

function rule110(c1::Bool, c2::Bool, c3::Bool)
    return (c1&c2&!c3)|(c1&!c2&c3)|(!c1&c2&c3)|(!c1&c2&!c3)|(!c1&!c2&c3)
end

function rule18(c1::Bool, c2::Bool, c3::Bool)
    return (!c1&!c2&c3)|(c1&!c2&!c3)
end

function rule32(c1::Bool, c2::Bool, c3::Bool)
    return (!c1&!c2&!c3)|(c1&!c2&!c3)|(!c1&c2&!c3)|(!c1&!c2&c3)
end

function rule30(c1::Bool, c2::Bool, c3::Bool)
    # return false
    return (c1&!c2&!c3)|(!c1&c2&!c3)|(!c1&!c2&c3)|(!c1&!c2&!c3)
end

rules = [ruleTest] # rule110, rule30,
numbers = ["test", "32", "57", "18", "110",]

function run_automaton(width, steps, rule)
    matrix = falses(steps, width)

    matrix[1, Int(round(width/2))] = true
    matrix[1, Int(round(width/2))+1] = true
    matrix[1, Int(round(width/2))+2] = true
    # matrix[1, Int(round(width/2))+4] = true
    # matrix[1, Int(round(width/2))+4] = true
    # matrix[1, Int(round(width/2))+5] = true
    # matrix[1, Int(round(width/2))+9] = true
    # matrix[1, Int(round(width/2))+14] = true
    println()
    for i in range(2, steps)
        for j in range(2, width-1)

            matrix[i,j] = rule(Bool(matrix[i-1,j-1]), Bool(matrix[i-1,j]), Bool(matrix[i-1,j+1]))
        end
    end
    return matrix[:,2:end-1]
end

using Pkg
# Pkg.add("Images")
using Images
# using Statistics
# using BenchmarkTools

file_path = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/78"

for i in 1:size(rules)[1]
    matrix = run_automaton(500, 200, rules[i])
    
    save("$file_path/rule$(numbers[i]).bmp", .!matrix)
end

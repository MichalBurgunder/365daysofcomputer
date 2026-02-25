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

rules = [rule18] # rule110, rule30,
numbers = ["18", "32", "110", "30"]

function run_automaton(width, steps, rule)
    matrix = falses(steps, width)

    # mid = Int(round(width/2))
    matrix[1, Int(round(width/2))] = true
    println()
    for i in range(2, steps)
        for j in range(2, width-1)
        # for j in range(mid-i, mid+i)
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

file_path = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157"

for i in 1:size(rules)[1]
    matrix = run_automaton(500, 200, rules[i])
    
    save("$file_path/rule$(numbers[i]).bmp", .!matrix)
end

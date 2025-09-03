using Pkg
# Pkg.add(["FFMPEG", "Plots", "FileIO"])
using Plots
using FileIO
using Images
using IndirectArrays
using Colors
using FFMPEG

using Base.Threads

function resize(maze, new_size)
    m, n = size(maze)
    new_maze = Array{Bool}(undef, new_size*m, new_size*n)

    for i in 0:m-1
        println(threadid())
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

images_directory = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157"
counter = 1


function save_image(matrix_naive, size_multiplier)
    mat_to_save = resize(matrix_naive, size_multiplier)
    # println(size(mat_to_save))
    # exit()
    global counter
    name = "bb_basic"# lpad(counter, 4, "0")
    counter += 1

    save("$images_directory/$name.png", mat_to_save)
end

letter_to_pos = Dict(
    "A" => 1,
    "B" => 2,
    "C" => 3,
    "D" => 4,
    "E" => 5,
    "Z" => 1 # halts elsewhere
)

hm_rl = Dict(
    "R" =>  1,
    "L" => -1
)

bool_to_pos = Dict(
    0 => 1,
    1 => 2
    )


function extract_info(tf, pos)
    the_string = tf[letter_to_pos[string(pos[1])]][bool_to_pos[pos[2]]]
    return [the_string[1], pos[3]+hm_rl[string(the_string[2])], the_string[3], pos[3]]
end

function single_timestep(the_row, tf, step_data)
    to_write, new_loc, next_letter, old_loc = extract_info(tf, step_data)

    the_row[old_loc] = Bool(parse(Int, to_write))
    return [next_letter, the_row[new_loc], new_loc]
end

# tf = transition function
function busy_beaver(tf, the_size, size_multiplier=5,shave=10, steps=100, fps=10)
    matrix = falses(the_size[1], the_size[2])
    the_row = falses(the_size[2])
    # print(the_row)
    new_timestep_data = ["A", 0, Int(the_size[2]/2)] # tf letter, tf number, location
    # save_image(matrix, size_multiplier)
    
    for i in 2:steps
        new_timestep_data = single_timestep(the_row, tf, new_timestep_data)

        if string(new_timestep_data[1]) == string("Z")
            return save_image(matrix, size_multiplier)
        end
        
        matrix[i,:] = the_row
    end
    
    save_image(matrix, size_multiplier)
    # gif_creation(steps, fps)
end

# 5-state busy beaver example
# transition_function = [
#     ["1RB", "1LC"],
#     ["1RC", "1RB"],
#     ["1RD", "0LE"],
#     ["1LA", "1LD"],
#     ["1RZ", "0LA"]
# ]

# 2-state busy bueaver example
transition_function = [
    ["1RB", "0LA"],
    ["1LA", "1RZ"],
]


# NOTE: the two varialbes below should remain the same in order to guarantee completion. Otherwise, if a TM can overflow. 
line_length = 50
steps = 50

size_multiplier = 20
shave = 0 # how many pixels should be shaved from the sides
fps = 1

busy_beaver(transition_function, (steps, line_length), size_multiplier, shave, steps, fps)

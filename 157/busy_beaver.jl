using Pkg
# Pkg.add(["FFMPEG", "Plots", "FileIO"])
using Plots
using FileIO
using Images
using IndirectArrays
using Colors
using FFMPEG

function resize(maze, new_size)
    m, n = size(maze)
    new_maze = Array{Bool}(undef, new_size*m, new_size*n)

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

function shave_off_sides(the_row, squares=0)
    if squares == 0
        return the_row
    end

    n = size(the_row)[1]
    new_row = falses(n-2*squares)

    for i in 1:n
        # end
    end

    return new_row
end

images_directory = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157"
counter = 1

function gif_creation(steps, fps)
    images = []

    for i in 1:steps
        ending = lpad(i, 4, "0")
        image = load("$images_directory/$ending.png")
        push!(images, image)
    end

    # create the gif
    gifname = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/bb_basic.gif"
    FFMPEG.ffmpeg_exe(`-framerate $(fps) -f image2 -i $(images_directory)/%04d.png -y $(gifname)`)

    # we remove the images, as we now have our gif
    # rm(images_directory, recursive=true)
end


function save_image(matrix_naive, shave, size_multiplier)
    mat_to_save = resize(shave_off_sides(matrix_naive, shave), size_multiplier)
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
    "E" => 5
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

function single_timestep(the_row, tf, step, step_data)
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
    # save_image(transpose(the_row), shave, size_multiplier)

    for i in 1:steps
        new_timestep_data = single_timestep(the_row, tf, i, new_timestep_data)
        matrix[i,:] = the_row
    end
    
    save_image(matrix, shave, size_multiplier)
    # gif_creation(steps, fps)
end


transition_function = [
    ["1RB", "1LC"],
    ["1RC", "1RB"],
    ["1RD", "0LE"],
    ["1LA", "1LD"],
    ["1RZ", "0LA"]
]
line_length = 200
steps = 400
size_multiplier = 20
shave = 0 # 100
fps = 20

busy_beaver(transition_function, (steps, line_length), size_multiplier, shave, steps, fps)

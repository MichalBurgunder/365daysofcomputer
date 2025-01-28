using Pkg
# Pkg.add(["FFMPEG"])
using Plots
using FileIO
using Images
using IndirectArrays
using Colors
using FFMPEG
# using IndirectArrays, FileIO, Colors

# this is just the gif creation process. Don't worry about it.
# function gif_creation(images)

#     # create the gif
#     images_directory = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157"
#     framerate = 100
#     gifname = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/conways_glider.gif"
#     FFMPEG.ffmpeg_exe(`-framerate $(framerate) -f image2 -i $(images_directory)/%04d.png -y $(gifname)`)

#     # we remove the images, as we now have our gif
#     rm(images_directory, recursive=true)
# end

function check_valid(matrix, i, j, offset)
    x,y = size(matrix)
    return (i < 1 | i < x | j < 1 |j < y) ? 0 : 1
end

cell_offset = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,1], [1,0], [1,-1]]

function rule(matrix, i, j)
    the_sum = sum([check_valid(matrix, i, j, offset) for offset in cell_offset])
    return the_sum == 2 || the_sum == 3 ? 1 : 0
end

function single_timestep(matrix, the_size)
    for i in range(1, the_size)
        for j in range(1, the_size)
            matrix[i,j] = rule(matrix, i, j)
        end
    end
    return matrix
end


function insert_object(matrix, location, offsets)
    i, j = location
    
    for os in range(1, size(offsets)[1])
        oi, oj = offsets[os]
        matrix[i+oi, j+oj] = 1
    end
end

images_directory = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/images"
file_name = "conway"
function gif_creation(steps)
    images = []


    for i in 1:steps
        ending = lpad(i, 4, "0")
        image = load("$images_directory/$file_name-$ending.png")
        # rgb_matrix = convert(Matrix{RGB}, image)
        # final_image = map(clamp01nan, rgb_matrix)
        push!(images, image)
    end

    # create the gif
   
    framerate = 100
    gifname = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/conways_glider.gif"
    FFMPEG.ffmpeg_exe(`-framerate $(framerate) -f image2 -i $(images_directory)/conway-0001.png -y $(gifname)`)

    # we remove the images, as we now have our gif
    # rm(images_directory, recursive=true)
end


counter = 1
function save_image(maze)
    global counter
    # save_maze = map(clamp01, maze)
    name = lpad(counter, 4, "0")
    counter += 1

    save("$images_directory/$file_name-$name.png", maze)
end



function conways_game_of_life(the_size=10, steps=100)
    matrix = falses(the_size, the_size)

    insert_object(matrix, (Int(the_size/2),Int(the_size/2)), [[-1,0], [1,0], [1,1], [1,-1], [0,1]])
    matrix[1,1] = 1
    println(matrix[1,1])
    save_image(matrix)

    all_matricies = []
    for i in 1:steps
        matrix = single_timestep(matrix, the_size)
        save_image(matrix)
    end

    # final_path = 


    # idxarray = rand(1:3, 100, 100, 50);
    gif_creation(steps)

#     # Create a plot (heatmap works well for images)
#     plt = heatmap(all_matricies[1])

#     # Animation for GIF
#     anim = @animate for i in 2:size(all_matricies)[1]
#         # Modify the plot or data (e.g., rotate, scale, etc.)
#         heatmap!(all_matricies[i])
#     end

# # Save as GIF
#     gif(anim, final_path, fps=10)

    # for i in 1:size(all_matricies)[1]
    #     frame(animation, all_matricies[i])
    # end

    # gif(animation, final_path, fps = 10)
end

conways_game_of_life()
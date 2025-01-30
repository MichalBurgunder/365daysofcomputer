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

function check_valid(matrix, i, j)
    x,y = size(matrix)
    return (i < 1 || i > x || j < 1 || j > y) ? 0 : matrix[i,j]
end

cell_offset = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,1], [1,0], [1,-1]]

function rule(matrix, i, j)
    the_sum = sum([check_valid(matrix, i+os[1], j+os[2]) for os in cell_offset])
    if matrix[i,j] == 1
        return (the_sum == 2 || the_sum == 3) ? 1 : 0
    else
        return the_sum == 3 ? 1 : 0
    end
        
end

function single_timestep(matrix, the_size)
    new_matrix = falses(the_size, the_size)
    for i in range(1, the_size)
        for j in range(1, the_size)
            new_matrix[i,j] = rule(matrix, i, j)
        end
    end

    return new_matrix
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
        image = load("$images_directory/$ending.png")
        push!(images, image)
    end

    # create the gif
    framerate = 100
    gifname = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/conways_glider.gif"
    FFMPEG.ffmpeg_exe(`-framerate $(framerate) -f image2 -i $(images_directory)/%04d.png -y $(gifname)`)

    # we remove the images, as we now have our gif
    # rm(images_directory, recursive=true)
end


counter = 1
function save_image(maze)
    global counter
    # save_maze = map(clamp01, maze)
    name = lpad(counter, 4, "0")
    counter += 1

    save("$images_directory/$name.png", maze)
end



function shave_off_squares(matrix, squares=10)
    n, m = size(matrix)
    new_matrix = falses(n-squares, n-squares)

    for i in 1:n-2*squares
        for j in 1:m-2*squares
            new_matrix[i,j] = matrix[i+squares, j+squares]
        end
    end

    return new_matrix
end

function conways_game_of_life(the_size=100, steps=100)
    matrix = falses(the_size, the_size)

    insert_object(matrix, (Int(the_size/2),Int(the_size/2)), [[-1,0], [1,0], [1,1], [1,-1], [0,1]])
    # matrix[1,1] = 1

    # println(matrix)
    # println(matrix[1,1])
    # exit()
    mat_to_save = shave_off_squares(matrix)
    save_image(mat_to_save)

    for i in 1:steps
        new_matrix = single_timestep(matrix, the_size)
        # println(new_matrix)
        # exit()
        mat_to_save2 = shave_off_squares(matrix)
        save_image(mat_to_save2)
        matrix = new_matrix
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
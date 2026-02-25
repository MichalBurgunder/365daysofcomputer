# CONWAYS GAME OF LIFE SIMULATION
using Pkg
Pkg.add(["Colors", "FFMPEG", "FileIO", "Images", "IndirectArrays", "Plots"])
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

function single_timestep(matrix, the_size)
    new_matrix = falses(the_size[1], the_size[2])
    for i in range(1, the_size[1])
        for j in range(1, the_size[2])
            new_matrix[i,j] = rule(matrix, i, j)
        end
    end

    return new_matrix
end


function insert_object(matrix, location, offsets)
    i, j = location

    for os in offsets
        oi, oj = os
        matrix[i+oi, j+oj] = 1
    end
end

images_directory = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/images"
file_name = "conway"

function gif_creation(steps, fps)
    images = []

    for i in 1:steps
        ending = lpad(i, 4, "0")
        image = load("$images_directory/$ending.png")
        push!(images, image)
    end

    # create the gif
    gifname = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code/157/random_gol.gif"
    FFMPEG.ffmpeg_exe(`-framerate $(fps) -f image2 -i $(images_directory)/%04d.png -y $(gifname)`)

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
    new_matrix = falses(n-2*squares, m-2*squares)

    for i in 1:n-2*squares
        for j in 1:m-2*squares
            new_matrix[i,j] = matrix[i+squares, j+squares]
        end
    end

    return new_matrix
end

function conways_game_of_life(the_size=(100,100), steps=100, objects=[], size_multiplier=5,shave=10,random_board=false)
    matrix = falses(the_size[1], the_size[2])

    for obj in objects
        insert_object(matrix, (Int(the_size[1]/2),Int(the_size[2]/2)), obj)
    end

    # you can comment out the following line, if you want a non-random board
    create_random_board(matrix)

    mat_to_save = resize(shave_off_squares(matrix, shave),size_multiplier)
    save_image(mat_to_save)

    for i in 1:steps
        new_matrix = single_timestep(matrix, the_size)
        mat_to_save2 = resize(shave_off_squares(new_matrix, shave),size_multiplier)
        save_image(mat_to_save2)
        matrix = new_matrix
    end
    gif_creation(steps, fps)
end

function create_random_board(matrix)
    for i in 1:10000
        matrix[rand(range(1,matrix_size[1])),rand(range(1,matrix_size[2]))] = rand((0,1))
    end
end

matrix_size = (90,120)
steps = 200
size_multiplier = 15
shave = 20 # 100
fps = 10
random_board = true

objects = []

# here you can add certain objects into the field 

## glider
# objects = [[[-1,0], [1,0], [1,1], [1,-1], [0,1]]]
## glider gun
# objects = [[
#     [0,0],[-1,-1],[0,-1],[1,-1],[-2,-2],[2,-2],[0,-3], # tip
#     [0,-7],[1,-7,],[-1,-7],[-2,-6],[2,-6],[-3,-5],[3,-5],[-3,-4],[3,-4], # left shell
#     [0,-16],[0,-17,],[-1,-16],[-1,-17], # left square
#     [-1,3],[-2,3],[-3,3],[-1,4],[-2,4],[-3,4],[0,5],[-4,5], # right segment
#     [0,7],[1,7],[-4,7],[-5,7], # right line
#     [-2,17],[-3,17],[-2,18],[-3,18], # right square
#     ]]


conways_game_of_life(matrix_size, steps, objects, size_multiplier, shave, random_board)
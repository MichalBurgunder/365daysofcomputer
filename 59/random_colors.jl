using Pkg
Pkg.add("ImageMagick")
Pkg.add("Colors")
Pkg.add("FileIO")
using Colors, FileIO, ImageMagick

# here we generate a plot of of random colored pixels, and then resize it for
# better visualization (otherwise you'd need to zoom in) 

# create the image
function create_image()
    width, height = 100, 100

    base_image = Array{RGB}(undef, width, height)

    for i in 1:width
        for j in 1:height
            base_image[i, j] = RGB(rand(), rand(), rand())
        end
    end

    return base_image
end

# resize the image 
function resize(maze, new_size)
    m, n = size(maze)
    new_maze = Array{RGB}(undef, new_size*m, new_size*n)

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

the_image = create_image()
the_image_resize = resize(the_image, 5)
save("random_colors.png", the_image_resize)

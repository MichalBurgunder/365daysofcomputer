# POOLING FILTER DEMONSTRATION

using Pkg
Pkg.add(["FileIO", "Images", "ImageIO"]) 
using FileIO, Images, ImageIO


# load the image
image = load("image.png")  # Replace with your image file

# change this parameter to see different pooling filters
ss = 3 # square size (numbers used: 1, 3, 10, 25)
ss2 = ss*ss
n, m = size(image)

new_n = Int(floor(n / ss))
new_m = Int(floor(m / ss))

new_image = Array{RGBA{Float64}, 2}(undef, new_n, new_m)

for i in 1:new_n-1
    for j in 1:new_m-1
        #     r   g   b   alpha
        r = [0.0,0.0,0.0]
        for sq_i in 1:ss
            for sq_j in 1:ss
                r[1] += image[ss*i+sq_i,ss*j+sq_j].r
                r[2] += image[ss*i+sq_i, ss*j+sq_j].g
                r[3] += image[ss*i+sq_i, ss*j+sq_j].b
            end
        end

        new_image[i,j] = RGBA((r[1]/ss2), (r[2]/ss2), (r[3]/ss2), 1)
    end
end

new_image = map(clamp01nan, new_image)

save("pooled_test_$ss.png", new_image)
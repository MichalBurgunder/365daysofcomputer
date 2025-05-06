# using Pkg
# Pkg.add(["Images", "FileIO", "ImageIO"]) 
using Images, FileIO, ImageIO


# Load the image
image = load("image.png")  # Replace with your image file

# Display the image

println(image[1,1])
println(image[1,1].r)
# exit()
ss = 3 # square size
ss2 = ss*ss
n, m = size(image)

new_n = Int(floor(n / ss))
new_m = Int(floor(m / ss))

new_image = Array{RGBA{Float64}, 2}(undef, new_n, new_m) # fill(RGBA(0,0,0,0), (, ))

for i in 1:new_n-1
    for j in 1:new_m-1
        #       r g b alpha
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

save("pooled_$ss.png", new_image)

# # Load the image
# image = load("your_image.png")

# # Get image dimensions
# h, w = size(image)

# # Ensure dimensions are multiples of 3
# h_new, w_new = (h ÷ 3) * 3, (w ÷ 3) * 3
# gray_image = gray_image[1:h_new, 1:w_new]  # Crop excess

# # Function for explicit 3×3 max pooling
# function max_pooling(img, pool_size=3)
#     h, w = size(img)
#     new_h, new_w = h ÷ pool_size, w ÷ pool_size
#     pooled_image = zeros(Gray{Float64}, new_h, new_w)  # Output image

#     for i in 1:new_h
#         for j in 1:new_w
#             pooled_image[i, j] = maximum(img[((i-1)*pool_size+1):(i*pool_size), ((j-1)*pool_size+1):(j*pool_size)])
#         end
#     end

#     return pooled_image
# end

# # Apply pooling
# pooled_image = max_pooling(gray_image)

# # Save the pooled image
# save("pooled_image.png", pooled_image)

# # Display original and pooled images
# fig, axs = plt.subplots(1, 2, figsize=(8, 4))
# axs[1].imshow(gray_image, cmap="gray")
# axs[1].set_title("Original Image")
# axs[2].imshow(pooled_image, cmap="gray")
# axs[2].set_title("3x3 Max Pooled Image")
# plt.show()
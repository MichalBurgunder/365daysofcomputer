using Pkg
# Pkg.add("Plots")
# Pkg.add("Images")
using Plots
using Images


function weierstrass_function(x, a, b)
    return sum([a^(n)*cos(b^(n)*pi*x) for n in 1:100])
end

function weierstrass_demonstration(size_increment, se_range)
    xs = []
    ys = []
    a = 0.5
    b = 3

    for x in se_range[1]:1/size_increment:se_range[2]
        push!(xs, x)
        push!(ys, weierstrass_function(x, a, b))
    end

    clamp
    save("weierstrass.png", plot(xs, [ys], size = (800,600), label="Weierstrass function"))

end

number_of_points = 1000 # 10000 # 1000
start_point = -0.5 # 0.1 # -0.5
end_point = 0.5 # 0.2  # 0.5
weierstrass_demonstration(number_of_points, [start_point, end_point])
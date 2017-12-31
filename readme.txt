readme

This program approximates the dimension (Hausdorff dimension) of a fractal using the box counting method. https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension

Inspired by this 3blue1brown video. https://www.youtube.com/watch?v=gB9n2gHsHN4


You can try this on the sample images with `python3 fractals.py sierpinsky.png`

This program is set to brute-force test for the fractal dimension of an object. It generates the factors of the nxn image and box-counts each iteration, and calculates the dimension between each iteration. Finding the true answer is left as an exercise to the user.



This program works best with large resolution fractals, or fractals with many iterations. It can also be modified to work with simple 2d binary arrays. 

This is a winter break project, so do not expect perfection.


Big sierpinski - no
large sierpinski - yes
circle - no
square - no
carpet 5 - yes
carpet 6 - yes
carpet big 7 - yes



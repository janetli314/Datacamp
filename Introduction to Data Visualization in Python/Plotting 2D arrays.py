'''
Generate two one-dimensional arrays u and v using np.linspace(). The array u should contain 41 values uniformly spaced between -2 and +2. The array v should contain 21 values uniformly spaced between -1 and +1.
Construct two two-dimensional arrays X and Y from u and v using np.meshgrid().
After the array Z is computed using X and Y, visualize the array Z using plt.pcolor() and plt.show().
Save the resulting figure as 'sine_mesh.png'.
'''
# Import numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1,1, 21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u,v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

# Display the resulting image with pcolor()
plt.pcolor(Z)
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')

'''
Using the meshgrid X, Y as axes for each plot:
Generate a default contour plot of the array Z in the upper left subplot.
Generate a contour plot of the array Z in the upper right subplot with 20 contours.
Generate a default filled contour plot of the array Z in the lower left subplot.
Generate a default filled contour plot of the array Z in the lower right subplot with 20 contours.
Improve the spacing between the subplots with plt.tight_layout() and display the figure.
'''
# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(X,Y,Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X,Y,Z,20)

'''
Modify the call to plt.contourf() so the filled contours in the top left subplot use the 'viridis' colormap.
Modify the call to plt.contourf() so the filled contours in the top right subplot use the 'gray' colormap.
Modify the call to plt.contourf() so the filled contours in the bottom left subplot use the 'autumn' colormap.
Modify the call to plt.contourf() so the filled contours in the bottom right subplot use the 'winter' colormap.
'''
# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20,cmap = 'autumn')
plt.colorbar()
plt.title('Autumn')

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20,cmap = 'winter')
plt.colorbar()
plt.title('Winter')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()

'''
Generate a two-dimensional histogram to view the joint variation of the mpg and hp arrays.

Put hp along the horizontal axis and mpg along the vertical axis.
Specify 20 by 20 rectangular bins with the bins argument.
Specify the region covered by using the optional range argument so that the plot samples hp between 40 and 235 on the x-axis and mpg between 8 and 48 on the y-axis. Your argument should take the form: range=((xmin, xmax), (ymin, ymax)).
Add a color bar to the histogram.
'''
# Generate a 2-D histogram
plt.hist2d(hp,mpg,bins=(20,20),range=((40,235),(8,48)))

# Add a color bar to the histogram
plt.colorbar()
# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()

'''
Generate a two-dimensional histogram with plt.hexbin() to view the joint variation of the mpg and hp vectors.

Put hp along the horizontal axis and mpg along the vertical axis.
Specify a hexagonal tesselation with 15 hexagons across the x-direction and 12 hexagons across the y-direction using gridsize.
Specify the rectangular region covered with the optional extent argument: use hp from 40 to 235 and mpg from 8 to 48. Note: Unlike the range argument in the previous exercise, extent takes one tuple of four values.
'''
# Generate a 2d histogram with hexagonal bins
plt.hexbin(hp, mpg, gridsize=(15,12), extent=(40,235,8,48))
           
# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()

'''
Load the file '480px-Astronaut-EVA.jpg' into an array.
Print the shape of the img array. How wide and tall do you expect the image to be?
Prepare img for display using plt.imshow().
Turn off the axes using plt.axis('off').
'''
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image
plt.imshow(img)
# Hide the axes
plt.axis('off')
plt.show()

'''
Print the shape of the existing image array.
Compute the sum of the red, green, and blue channels of img by using the .sum() method with axis=2.
Print the shape of the intensity array to verify this is the shape you expect.
Plot intensity with plt.imshow() using a 'gray' colormap.
Add a colorbar to the figure.
'''
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis = 2)

# Print the shape of the intensity
print(intensity.shape)

# Djavascript:void(0)isplay the intensity with a colormap of 'gray'
plt.imshow(intensity,cmap = 'gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()


'''
Display img in the top left subplot with horizontal extent from -1 to 1, vertical extent from -1 to 1, and aspect ratio 0.5.
Display img in the top right subplot with horizontal extent from -1 to 1, vertical extent from -1 to 1, and aspect ratio 1.
Display img in the bottom left subplot with horizontal extent from -1 to 1, vertical extent from -1 to 1, and aspect ratio 2.
Display img in the bottom right subplot with horizontal extent from -2 to 2, vertical extent from -1 to 1, and aspect ratio 2.
'''
# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Specify the extent and aspect ratio of the top left subplot
plt.subplot(2,2,1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5') 
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=0.5)

# Specify the extent and aspect ratio of the top right subplot
plt.subplot(2,2,2)
plt.title('extent=(-1,1,-1,1),\naspect=1')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=1)

# Specify the extent and aspect ratio of the bottom left subplot
plt.subplot(2,2,3)
plt.title('extent=(-1,1,-1,1),\naspect=2')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent = (-1,1,-1,1), aspect=2)

# Specify the extent and aspect ratio of the bottom right subplot
plt.subplot(2,2,4)
plt.title('extent=(-2,2,-1,1),\naspect=2')
plt.xticks([-2,-1,0,1,2])
plt.yticks([-1,0,1])
plt.imshow(img, extent= (-2,2,-1,1), aspect=2)

# Improve spacing and display the figure
plt.tight_layout()
plt.show()

'''
Use the methods .min() and .max() to save the minimum and maximum values from the array image as pmin and pmax respectively.
Create a new 2-D array rescaled_image using 256*(image-pmin)/(pmax-pmin)
Plot the new array rescaled_image.
'''
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(),image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin ) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." % 
      (rescaled_image.min(), rescaled_image.max()))

# Display the rescaled image
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)

plt.show()




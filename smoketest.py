

import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.image as mpimg


def main():

    fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))

    ax0.set_aspect("equal")
    ax0.fill([0, 500, 500, 0], [0, 0, 50, 50], color="white")
    circle1 = plt.Circle((50, 25), 20, color="yellow")
    ax0.add_patch(circle1)
    circle2 = plt.Circle((150, 25), 20, color="red")
    ax0.add_patch(circle2)
    circle3 = plt.Circle((250, 25), 20, color="purple")
    ax0.add_patch(circle3)
    circle4 = plt.Circle((350, 25), 20, color="green")
    ax0.add_patch(circle4)
    circle5 = plt.Circle((450, 25), 20, color="pink")
    ax0.add_patch(circle5)

    # Add reflection of stage lights
    blinking_polygon1 = plt.Polygon(np.array([[20, 60], [50, 460], [80, 60]]), color="yellow", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon1)
    blinking_polygon2 = plt.Polygon(np.array([[130, 60], [160, 460], [190, 60]]), color="red", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon2)
    blinking_polygon3 = plt.Polygon(np.array([[220, 60], [250, 460], [280, 60]]), color="purple", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon3)
    blinking_polygon4 = plt.Polygon(np.array([[320, 60], [350, 460], [380, 60]]), color="green", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon4)
    blinking_polygon5 = plt.Polygon(np.array([[430, 60], [460, 460], [490, 60]]), color="pink", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon5)

    # Add 10 circles with the specified properties
    for i in range(10):
        circle = plt.Circle((20 + i * 50, 30), 20, color="yellow", zorder=10)
        ax1.add_patch(circle)



    ax1.set_aspect("equal")
    ax1.fill([0, 500, 500, 0], [0, 0, 500, 500], color="white")

    rectangle = plt.Rectangle((220, 130), 60, 100, color="gray", zorder=10)
    ax1.add_patch(rectangle)

    # Add a circle outside the stage with a higher order value
    circle6 = plt.Circle((250, 250), 50, color="orange", zorder=10)
    ax1.add_patch(circle6)

    # Add another circle outside the stage with the same properties as circle6
    circle7 = plt.Circle((30, 150), 30, color="gray", zorder=10)
    ax1.add_patch(circle7)

    rectangle = plt.Rectangle((0, 450), 500, 80, color="Purple", zorder=10)
    ax1.add_patch(rectangle)

    rectangle = plt.Rectangle((10, 60), 40, 100, color="gray", zorder=10)
    ax1.add_patch(rectangle)

    # Add the stage 
    ax1.fill([0, 500, 500, 0], [0, 0, 60, 60], color="wheat")

    # Load the JPEG image
    image_path1 = "123.jpg"
    #image_path2= "images.jpeg"  # Replace with the actual path to your image file
    image1 = mpimg.imread(image_path1)
    #image2 = mping.imread(image_path2)

    # Get the size of the screen
    screen_width = ax1.get_xlim()[1]
    screen_height = ax1.get_ylim()[1]

    # Set the desired image size
    image_width = 480
    image_height = 380

    image_x = (screen_width - image_width) / 2.5
    image_y = (screen_height - image_height) / 2.5



    ax1.imshow(image1, extent=[image_x, image_x + image_width, image_y, image_y + image_height], alpha=0.8, zorder=10)
    #ax1.imshow(image2, extent=[image_x, image_x + image_width, image_y, image_y + image_height], alpha=0.5, zorder=10)
    # Store the stage lights patches
    stage_lights = [circle1, circle2, circle3, circle4, circle5]
    blinking_polygon = [blinking_polygon1, blinking_polygon2, blinking_polygon3, blinking_polygon4,
                          blinking_polygon5]

    # for beams on the side
    
    #ax1.fill([230,270,270,230],[490,490,500,500], color="red")
    ax1.fill([15,10,100,400],[450,490,100,100], color="red")
    #ax1.fill([330,370,370,330],[490,490,500,500], color="blue")
    ax1.fill([500,490,430,270],[490,490,100,100], color="blue")

    # Define the size of the grid
    grid_size = 50

    # Create a grid of zeros
    grid = np.zeros((grid_size, grid_size))

    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    ax.set_aspect('equal')


    


    for a in range(20):
        for light, reflect_rect in zip(stage_lights, blinking_polygon):
            color = random.choice(["green", "orange", "blue"])
            light.set_color(color)
            reflect_rect.set_color(color)


            
      
        plt.title("Stage Dance Floor" + str(a + 1), fontsize="11")
        plt.pause(0.5)

    plt.show()


if __name__ == "__main__":
    main()

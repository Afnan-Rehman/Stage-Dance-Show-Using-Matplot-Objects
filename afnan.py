

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
    blinking_polygon1 = plt.Polygon(np.array([[20, 60], [50, 460], [80, 60]]), color="cyan", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon1)
    blinking_polygon2 = plt.Polygon(np.array([[130, 60], [160, 460], [190, 60]]), color="magenta", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon2)
    blinking_polygon3 = plt.Polygon(np.array([[220, 60], [250, 460], [280, 60]]), color="yellow", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon3)
    blinking_polygon4 = plt.Polygon(np.array([[320, 60], [350, 460], [380, 60]]), color="green", alpha=0.3, zorder=10)
    ax1.add_patch(blinking_polygon4)
    blinking_polygon5 = plt.Polygon(np.array([[430, 60], [460, 460], [490, 60]]), color="orange", alpha=0.3, zorder=10)
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

    # For smoke Machine Object on the side
    circle7 = plt.Circle((30, 150), 30, color="gray", zorder=10)
    ax1.add_patch(circle7)
    rectangle = plt.Rectangle((10, 60), 40, 100, color="gray", zorder=10)
    ax1.add_patch(rectangle)


    # Adds curtain

    rectangle = plt.Rectangle((0, 450), 500, 80, color="Purple", zorder=10)
    ax1.add_patch(rectangle)

    #rectangle = plt.Rectangle((10, 60), 40, 100, color="gray", zorder=10)
    #ax1.add_patch(rectangle)

    # Add the stage 
    ax1.fill([0, 500, 500, 0], [0, 0, 80, 80], color="wheat")

    # Load the JPEG image
    image_path1 = "123.jpg"
    #image_path2= "images.jpeg"  # Replace with the actual path to your image file
    background = mpimg.imread(image_path1)
    #image2 = mping.imread(image_path2)

    # Get the size of the screen
    screen_width = ax1.get_xlim()[1]
    screen_height = ax1.get_ylim()[1]

    #Set the desired image size
    image_width = 480
    image_height = 380

    image_x = (screen_width - image_width) / 2.5
    image_y = (screen_height - image_height) / 2.5

    #ax1.imshow(image1, extent=[1, screen_width, 1, screen_height], alpha=0.8, zorder=2)

    ax1.imshow(background, extent=[image_x, image_x + image_width, image_y, image_y + image_height], alpha=0.4, zorder=10)
    #ax1.imshow(image2, extent=[image_x, image_x + image_width, image_y, image_y + image_height], alpha=0.5, zorder=10)
    # Store the stage lights patches
    stage_lights = [circle1, circle2, circle3, circle4, circle5]
    blinking_polygon = [blinking_polygon1, blinking_polygon2, blinking_polygon3, blinking_polygon4,
                          blinking_polygon5]

    # for beams on the side
    
    #ax1.fill([230,270,270,230],[490,490,500,500], color="red")
    beam = ax1.fill([15,10,50,100],[450,490,100,100], color="red", alpha= 0.3)
    #ax1.fill([330,370,370,330],[490,490,500,500], color="blue")
   # beam = ax1.fill([100,190,130,170],[490,490,100,100], color="blue", alpha= 0.3)

    def smoke_effect():
        # Generate random smoke positions
        x = np.random.uniform(100, 400, size=50)
        y = np.random.uniform(100, 400, size=50)
        sizes = np.random.uniform(10, 30, size=100)
        opacities = np.random.uniform(0.3, 0.5, size=100)
        colors = np.random.uniform(0.3, 0.5, size=(100, 3))

        # Add smoke patches to the plot
        neighbors = [(x[5]-50, y[5]), (x[5]+50, y[5]), (x[5], y[5]-50), (x[5], y[5]+50)]
        for neighbor in neighbors:
            if 0 <= neighbor[0] <= 500 and 0 <= neighbor[1] <= 500:
                circle_neighbor = plt.Circle(neighbor, sizes[5], color=colors[5], alpha=opacities[5])
                ax1.add_patch(circle_neighbor)

    for a in range(20):
        for light, reflect_rect in zip(stage_lights, blinking_polygon):
            color = random.choice(["green", "orange", "blue"])
            light.set_color(color)
            reflect_rect.set_color(color)


            
        smoke_effect()
        plt.title("Stage Dance Floor" + str(a + 1), fontsize="11")
        plt.pause(0.5)

        #print = input("Enter a value: ")

    plt.show()


if __name__ == "__main__":
    main()

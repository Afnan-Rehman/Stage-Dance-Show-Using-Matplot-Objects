

import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.image as mpimg



def main():

    fig, (top, bottom) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 10]}, figsize=(10, 10))
    #Lights  
    # Adds light on top of the stage
    top.set_aspect("equal")
    top.fill([0, 500, 500, 0], [0, 0, 50, 50], color="white")
    light1 = plt.Circle((50, 25), 20, color="yellow")
    top.add_patch(light1)
    light2 = plt.Circle((150, 25), 20, color="red")
    top.add_patch(light2)
    light3 = plt.Circle((250, 25), 20, color="purple")
    top.add_patch(light3)
    light4 = plt.Circle((350, 25), 20, color="green")
    top.add_patch(light4)
    light5 = plt.Circle((450, 25), 20, color="pink")
    top.add_patch(light5)

    # Add corresponding reflection of stage lights
    blinking_polygon1 = plt.Polygon(np.array([[20, 60], [50, 460], [80, 60]]), color="cyan", alpha=0.3, zorder=10)
    bottom.add_patch(blinking_polygon1)
    blinking_polygon2 = plt.Polygon(np.array([[130, 60], [160, 460], [190, 60]]), color="magenta", alpha=0.3, zorder=10)
    bottom.add_patch(blinking_polygon2)
    blinking_polygon3 = plt.Polygon(np.array([[220, 60], [250, 460], [280, 60]]), color="yellow", alpha=0.3, zorder=10)
    bottom.add_patch(blinking_polygon3)
    blinking_polygon4 = plt.Polygon(np.array([[320, 60], [350, 460], [380, 60]]), color="green", alpha=0.3, zorder=10)
    bottom.add_patch(blinking_polygon4)
    blinking_polygon5 = plt.Polygon(np.array([[430, 60], [460, 460], [490, 60]]), color="orange", alpha=0.3, zorder=10)
    bottom.add_patch(blinking_polygon5)

    bottom.set_aspect("equal")
    bottom.fill([0, 500, 500, 0], [0, 0, 500, 500], color="white")

    #BACKDROP Background Image

    backdrop = "123.jpg"
    
    background = mpimg.imread(backdrop)
    #image2 = mping.imread(backdrop2)

    # sets size of the screen
    screen_width = bottom.get_xlim()[1]
    screen_height = bottom.get_ylim()[1]

    image_width = 490
    image_height = 380

    image_x = (screen_width - image_width) / 4
    image_y = (screen_height - image_height) / 2

    #bottom.imshow(image1, extent=[1, screen_width, 1, screen_height], alpha=0.8, zorder=2)

    bottom.imshow(background, extent=[image_x, image_x + image_width, image_y, image_y + image_height], alpha=0.4, zorder=5)
    

    #PROPS
    # starting code to make Props and bands, I think object on the middle would act as person standing. I will make a stage too, and add some audience objects,,letss see
    # lets start with making a stage

    stage =  bottom.fill([0, 500, 500, 0], [0, 0, 80, 80], color="wheat")

    #stage is working, now for props i think lets add an object on stage
    #this is visualising smoke machine i guess
    rectangle = plt.Rectangle((10, 60), 40, 100, color="gray", zorder=10)
    bottom.add_patch(rectangle)

    circle1 = plt.Circle((30, 150), 30, color="gray", zorder=10)
    bottom.add_patch(circle1)

    # i think lets add another rectangle to make it visualise as a curtain on top of the stage
    rectangle = plt.Rectangle((0, 450), 500, 80, color="Purple", zorder=10)
    bottom.add_patch(rectangle)

    # add another object visualising a person in the middle
    rectangle = plt.Rectangle((220, 130), 60, 100, color="brown", zorder=10)
    bottom.add_patch(rectangle)
    circle2 = plt.Circle((250, 250), 50, color="orange", zorder=10)
    bottom.add_patch(circle2)


        #lets add circle visualizing audience on the stage

    for h in range(10):
        circle = plt.Circle((20 + h * 50, 30), 20, color="yellow", zorder=10)
        bottom.add_patch(circle)
    
    # Lets ADD SOME CHOREOGRAPHY

    top_lights = [light1, light2, light3, light4, light5]
    blinking_polygon = [blinking_polygon1, blinking_polygon2, blinking_polygon3, blinking_polygon4,
                          blinking_polygon5]
   

    for a in range(5):
        for light, reflect_rect in zip(top_lights, blinking_polygon):  
            color = random.choice(["green", "orange", "blue"])
            light.set_color(color)
            reflect_rect.set_color(color)

        plt.title("Stage Show" + str(a + 1), fontsize="11")
        plt.savefig("Stage Show" + str(a + 1)+ '.png')
        plt.pause(0.5)
    

    plt.show()


if __name__ == "__main__":
    main()

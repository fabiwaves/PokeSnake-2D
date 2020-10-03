import sys
import glfw
from OpenGL.GL import *
from CourseResources import easy_shaders as es
from MVC.Models import Snake
from MVC.Models import Background
from MVC.Models import Wall
from MVC.Controllers import Controller


if __name__ == '__main__':

    # We initialize glfw
    if not glfw.init():
        sys.exit()

    # Set width and height of the window
    width = 800
    height = 800

    # We create the window with the previous params
    window = glfw.create_window(width, height, 'Poke-Snake', None, None)

    # Handle the exception of the window not been created properly
    if not window:
        glfw.terminate()
        sys.exit()

    # We set the window as the current window
    glfw.make_context_current(window)

    # We set the controller
    controller = Controller.Controller()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controller.on_key)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()

    # Telling OpenGL to use our shader program
    glUseProgram(pipeline.shaderProgram)

    # Setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    # Our shapes here are always fully painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # We create the models
    wall = Wall.Wall(5)
    snake = Snake.Snake(5)
    background = Background.Background()

    # We set the models to the controller
    controller.set_snake(snake)

    # Here we draw the models to play the Snake
    while not glfw.window_should_close(window):

        # We obtain the events
        glfw.poll_events()

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        # Dibujar los modelos
        # 1. Field
        # 2. Walls

        # 3. Apple
        background.draw(pipeline)
        wall.draw(pipeline)
        # 4. Snake
        snake.draw(pipeline)

        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    # We terminate the window
    glfw.terminate()

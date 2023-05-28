# FRONT = 
# 
#     [A, A, ... ,A]
#     [A, A, ... ,A]
#             .
#             .
#             .
#     [A, A, ... ,A]

class Rubik:
    def __init__(self, n):
        self.n = n
        self.front = CONSTRUCT n*n matrix with 'red'
        self.right = CONSTRUCT n*n matrix with 'blue'
        self.left = CONSTRUCT n*n matrix with 'green'
        self.back = CONSTRUCT n*n matrix with 'orange'
        self.up = CONSTRUCT n*n matrix with 'white'
        self.down = CONSTRUCT n*n matrix with 'yellow'

    def display():
        print("FRONT :\n", self.front)
        print("RIGHT :\n", self.back)
        print("LEFT :\n", self.left)
        print("BACK :\n", self.back)
        print("UP :\n", self.up)
        print("DOWN :\n", self.down)

    def move(axis, num, direction): 
        # assert : axis == 'x','y', or, 'z' AND 0 <= num < n
        if (axis == 'x'):
            # assert : direction == 'up', 'down'
            """

            If this is FRONT

                    [1,1,1]
                    [1,1,1]
                    [1,1,1]

                     <-x->

            then x-axis goes from left(0) to right(n-1)
            x-axis move would look like this

            move('x', 0, 'up')

                    [0,1,1]
                    [0,1,1]
                    [0,1,1]

            if the bottom face only has 0's
            """

            switch(direction, num, front, up, back, down)

            if (num == 0):
                rotate(left, APPROPRIATE DIRECTION(direction))
                
            else if (num == n-1):
                rotate(right, APPROPRIATE DIRECTION(direction))

        else if (axis == 'y'):
            # assert : direction == 'right', 'left'
            """

            If this is FRONT
                ^
                |   [1,1,1]
                y   [1,1,1]
                |   [1,1,1]
                v

            then y-axis goes from top(0) to bottom(n-1) 
            y-axis move would look like this

            move('y', 0, 'right')

                    [0,0,0]
                    [1,1,1]
                    [1,1,1]

            if the left face only has 0's
            """

            switch(direction, num, front, right, back, left)

            if (num == 0):
                rotate(up, APPROPRIATE DIRECTION(direction))
                
            else if (num == n-1):
                rotate(down, APPROPRIATE DIRECTION(direction))
        else:
            """

            If this is FRONT
                
                    [1,1,1]
                z   [1,1,1]
                    [1,1,1]
                

            then z-axis goes from front(0) to back(n-1) 
            z-axis move would look like this

            move('z', 0, 'right')

                    [1,1,1]
                    [1,1,1]
                    [1,1,1]

            The front face would simply rotate right.
            """

            switch(direction, num, up, right, down, left)

            if (num == 0):
                rotate(front, APPROPRIATE DIRECTION(direction))
                
            else if (num == n-1):
                rotate(back, APPROPRIATE DIRECTION(direction))
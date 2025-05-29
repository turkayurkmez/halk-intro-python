from turtle import Turtle, done

tospa = Turtle()
tospa.fillcolor("red")
tospa.begin_fill()
for x in range(1,5):
    tospa.forward(250)
    tospa.right(90)

tospa.fillcolor('Blue')
tospa.write('Ben tospaayım')

tospa.fillcolor("Green")
tospa.begin_fill()
tospa.circle(200)
tospa.end_fill()
done()
import circle
import square

radius = float(input('input the radius:'))
print('the area of the circle is', circle.area(radius))
print('the diameter of the circle is', circle.diameter(radius))

side = float(input('input the side:'))
print('the area of the square is', square.area(side))
print('the diagonal of the square is', square.diagonal(side))
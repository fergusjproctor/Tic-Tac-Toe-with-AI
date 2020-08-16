class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.S = self.a * self.b / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if input_a * input_a + input_b * input_b == input_c * input_c:
    triangle = RightTriangle(input_c, input_a, input_b)
    print(round(triangle.S, 1))
else:
    print('Not right')

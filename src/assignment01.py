'''
You are to write a Python program which recommends how many small and large
boxes of cupcakes to buy at a cupcake shop.
Small boxes have 3 cupcakes, and large boxes have 4 cupcakes.
You will always recommend the fewest number of boxes.
For example, for 12 people, you should recommend 3 large boxes, not 4 small boxes.
Many orders will require a mixture of small and large.
For example, for 7 people, you should recommend 1 small box and 1 large box
(7 cupcakes in total).

For 1, 2 or 5 people, you cannot precisely match those numbers using a
combination of small and large boxes.
In this case, you should double (or triple) the order so that every person gets
exactly the same number of cupcakes.
For example, for 5 people, you should recommend 2 small and 1 large boxes,
giving 10 cupcakes in total, and each person can have 2 cupcakes.
'''


def calculate_boxes(num_people, multiple):
    target_cupcakes = num_people * multiple
    num_cupcakes = 0

    def calculate_cupcakes():
        return small_boxes * 3 + large_boxes * 4

    large_boxes = target_cupcakes // 4
    small_boxes = target_cupcakes % 4 // 3
    num_cupcakes = calculate_cupcakes()

    while(num_cupcakes != target_cupcakes):
        if(num_cupcakes > target_cupcakes):
            large_boxes -= 1
            num_cupcakes = calculate_cupcakes()

        elif(num_cupcakes < target_cupcakes):
            small_boxes += 1
            num_cupcakes = calculate_cupcakes()

    if(large_boxes < 0 or small_boxes < 0):
        return calculate_boxes(num_people, multiple + 1)

    return small_boxes, large_boxes


print("Welcome to the Cupcake Shop!")
print("Small boxes have 3 cupcakes")
print("Large boxes have 4 cupcakes")
num_people = int(input("How many people do you need to buy cupcakes for? "))

small_boxes, large_boxes = calculate_boxes(num_people, 1)
num_cupcakes = small_boxes * 3 + large_boxes * 4
cupcakes_per_person = num_cupcakes // num_people

print(f"You should buy {small_boxes} small boxes and {large_boxes} large boxes")
print(f"You will then have {num_cupcakes} cupcakes. Each person can have {cupcakes_per_person} cupcakes")

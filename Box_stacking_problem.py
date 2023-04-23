class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self, other):
        return self.d*self.w < other.d*other.w

def max_stack_height(boxes):
    rotated_boxes = []
    for box in boxes:
        rotated_boxes.append(Box(box.h, min(box.w, box.d), max(box.w, box.d)))
        rotated_boxes.append(Box(box.w, min(box.h, box.d), max(box.h, box.d)))
        rotated_boxes.append(Box(box.d, min(box.h, box.w), max(box.h, box.w)))
    rotated_boxes.sort(reverse=True)
    n = len(rotated_boxes)
    max_heights = [rotated_boxes[i].h for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (rotated_boxes[i].w < rotated_boxes[j].w and 
                rotated_boxes[i].d < rotated_boxes[j].d and 
                max_heights[i] < max_heights[j]+rotated_boxes[i].h):
                max_heights[i] = max_heights[j]+rotated_boxes[i].h
    return max(max_heights)

n = int(input("Enter the number of boxes: "))
boxes = []
for i in range(n):
    h, w, d = map(int, input("Enter the height, width, and depth of box {}: ".format(i+1)).split())
    boxes.append(Box(h, w, d))

max_height = max_stack_height(boxes)
print("Maximum stack height:", max_height)

"""Giraffe"""
def main():
    """Giraffe"""
    heights = []
    count = 0
    for _ in range(int(input())):
        heights.append(int(input()))
    hight_len = len(heights)
    for i in range(hight_len):
        left = heights[i-1] if i > 0 else -1
        right = heights[i+1] if i < len(heights)-1 else -1
        if (left == -1 or heights[i] > left) and (right == -1 or heights[i] > right):
            count += 1
    print(count)
main()

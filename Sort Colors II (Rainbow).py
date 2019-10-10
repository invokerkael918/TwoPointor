def sortColors2(colors, k):
    """
    Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
    :param colors:[3,2,2,1,4]
    :param k: 4
    :return:[1,2,2,3,4]

    Basic Idea: quickSort + Merge Sort
    merge sort分Color，quickSort 换位（partition)
    """
    sort(colors, 1, k, 0, len(colors) - 1)
    return colors


def sort(colors, color_from, color_to, index_from, index_to):
    if color_from == color_to or index_from == index_to:
        return

    color = (color_from + color_to) // 2

    left, right = index_from, index_to

    while left <= right:

        while left <= right and colors[left] <= color:
            left += 1
        while left <= right and colors[right] > color:
            right -= 1

        if left<= right:
            colors[left],colors[right] = colors[right], colors[left]
            left+=1
            right-=1

    sort(colors,color_from,color,index_from,right)
    sort(colors,color+1,color_to,left,index_to)

if __name__ == '__main__':
    print(sortColors2([2,1,1,2,2],2))


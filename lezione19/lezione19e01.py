def mergeSort(input_list: list) -> list:
    """
    
    """
    if len(input_list) == 1:
        
        return input_list

    mid_point: int = len(input_list) // 2

    mergeSort(input_list=input_list[:mid_point])
    mergeSort(input_list=input_list[mid_point:])


if __name__ == "__main__":

    input_list : list[int] = [0,1, 2, 3, 4, 5, 6, 7]

    mergeSort(input_list=input_list)
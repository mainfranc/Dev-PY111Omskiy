import numpy as np


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    fld = np.zeros((shape[0], shape[1]))
    rdest = point[0]
    cdest = point[1]

    iteration_ = 1
    store_list = pos_moves(fld, 0, 0, iteration_)
    fld = store_list[0]
    curr_moves = store_list[1]

    while any(curr_moves):
        next_step_moves = []
        iteration_ += 1
        for i in curr_moves:
            store_list = pos_moves(fld, i[0], i[1], iteration_)
            fld = store_list[0]
            for item_ in store_list[1]:
                next_step_moves.append(item_)
        curr_moves = next_step_moves

    print(fld)
    return fld[rdest][cdest]


def pos_moves(fld, x, y, iterat_):
    currmoves = []
    if x + 1 <= fld.shape[0] - 1 and y + 2 <= fld.shape[1] - 1:
        fld[x + 1][y + 2] += (2 ** iterat_) # + fld[x][y])
        currmoves.append((x + 1, y + 2))
    if x + 1 <= fld.shape[0] - 1 and y - 2 >= 0:
        fld[x + 1][y - 2] += (2 ** iterat_) # + fld[x][y])
        currmoves.append((x + 1, y - 2))
    if x + 2 <= fld.shape[0] - 1 and y + 1 <= fld.shape[1] - 1:
        fld[x + 2][y + 1] += (2 ** iterat_) # + fld[x][y])
        currmoves.append((x + 2, y + 1))
    if x + 2 <= fld.shape[0] - 1 and y - 1 >= 0:
        fld[x + 2][y - 1] += (2 ** iterat_) # + fld[x][y])
        currmoves.append((x + 2, y - 1))
    return [fld, currmoves]

if __name__ == '__main__':
    print(calculate_paths((6,4), (6,4)))
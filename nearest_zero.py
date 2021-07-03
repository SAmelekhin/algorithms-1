from typing import List


def nearest_zero(street_len: int, land_plots: List[int]) -> List:
    before, back = [0]*street_len, [0]*street_len
    bf_dist = b_dist = len(land_plots)-1
    ind_plots = [ind for ind in range(street_len)]

    for bf_num, b_num, ind in zip(land_plots, land_plots[::-1], ind_plots):
        bf_dist = (bf_dist + 1) * (bf_num != 0)
        before[ind] = bf_dist
        b_dist = (b_dist + 1) * (b_num != 0)
        back[ind] = b_dist

    dist_nums = [
        min(bf_num, b_num) for bf_num, b_num in zip(before, back[::-1])
        ]

    return dist_nums


def main():
    street_len = int(input())
    land_plots = [int(area) for area in input().split()]
    dist_nums = nearest_zero(street_len, land_plots)
    print(*dist_nums)


if __name__ == '__main__':
    main()

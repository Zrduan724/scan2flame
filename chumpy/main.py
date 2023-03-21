from landmarks import load_picked_points
from fit_scan import *

# ———————————— step 1 ————————————————
# load_picked_points函数将PP文件转为npy
# 第一个参数为PP文件的地址，请将pp文件放到pp_file文件夹
# 第二个参数为npy文件的保存地址，保存到pp_npy文件夹
load_picked_points(
    './pp_file/20230224023221564.000065_picked_points.pp',
    './pp_npy/20230224023221564.000065_picked_points.npy')

# ———————————— step 2 ————————————————
# run_fitting函数进行拟合，输出拟合结果obj保存到output文件夹
# 第一个参数为obj文件的地址，请将待拟合的obj文件放到3d_scan文件夹
# 第二个参数为该obj对应的pp文件的npy（上一步第二个参数，npy保存地址）
# 第三个参数为fit结果的名字，数字对应帧数即可
run_fitting('./3d_scans/20230224023221564.000065.obj',
            './pp_npy/20230224023221564.000065_picked_points.npy',
            'fit_scan_result_65.obj')

# 建议可以标注完成以后，将上述两步放到循环里进行，无需一次一次手动修改操作

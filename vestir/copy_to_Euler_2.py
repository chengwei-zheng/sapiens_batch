import os
import shutil

def copy_selected_folders(in_dir: str, out_dir: str, folder_list: list[str]):
    os.makedirs(out_dir, exist_ok=True)
    for folder_name in folder_list:
        src_path = os.path.join(in_dir, folder_name)
        dst_path = os.path.join(out_dir, folder_name)
        if os.path.isdir(src_path):
            print(f"Copying {src_path} → {dst_path}")
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            raise RuntimeError(f"{src_path} not exist!")

# 示例用法
if __name__ == "__main__":
    # in_dir = "/mnt/euler_scratch/garment-digitization/data/Outputs/"
    # out_dir = "/mnt/server01B/work/vestir/garment-digitization/Outputs/"
    # in_dir = "/mnt/server01B/work/vestir/garment-digitization/Inputs/"
    # out_dir = "/mnt/server01B/work/vestir/garment-digitization/Inputs_3x/"
    in_dir = "/mnt/euler/hold/hold/code/logs/"
    out_dir = "/mnt/scratch/lixin/RHINO/HOLD/"
    folder_list = [
                    "std_chen_monitor2_1/test/",
                    "std_lixin_chair2_1/test/",
                    "hea_lixin_cart4_1/test/",
                   ]

    copy_selected_folders(in_dir, out_dir, folder_list)

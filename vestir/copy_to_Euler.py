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


def copy_selected_dirs(root: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)

    # for name in os.listdir(root):
    #     if name.startswith(("full_", "hea_", "stage_")):
    for name in [
        "hea_lixin_cart4_1",
        "hea_chen_cartbox_1",
        "std_chen_monitor2_1",
    ]:
        src = os.path.join(root, name)
        dst = os.path.join(out_dir, name)
        if os.path.isdir(src):
            print(f"Copying {src} → {dst}")

            def ignore_checkpoints(dir, files):
                return ['checkpoints'] if 'checkpoints' in files else []

            shutil.copytree(src, dst, ignore=ignore_checkpoints, dirs_exist_ok=True)
        else:
            print(f"Skipping non-directory: {src}")


# 示例用法
if __name__ == "__main__":
    # in_dir = "/mnt/server01B/work/vestir/garment-digitization/Outputs/"  # Inputs_3x
    # out_dir = "/mnt/euler_scratch/garment-digitization/data/Outputs/"
    # folder_list = [
    #                 "V217F_CreamShorts_38_GP",
    #                 "V217F_CreamShorts_40_GP",
    #                 "V225F_CreamShorts_42_GP",
    #                 "V206F_CreamShorts_44_GP",
    #                 "V221F_CreamShorts_46_GP",
    #                ]
    #
    # copy_selected_folders(in_dir, out_dir, folder_list)
    root = "/mnt/euler/hold/hold/code/logs/"
    out_dir = "/mnt/scratch/lixin/RHINO/HOLD/"
    copy_selected_dirs(root, out_dir)

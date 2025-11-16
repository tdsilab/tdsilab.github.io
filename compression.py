import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed

# 输入输出目录
input_dir = "assets/photo"
output_dir = "assets/photo2"

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 支持格式
valid_ext = ['.jpg', '.jpeg', '.png', '.webp']

# 压缩质量（10~95）
quality = 10

# 是否转成 webp（True/False）
convert_to_webp = False

# 最大允许尺寸（自动缩放），不缩放则设 None
max_size = 2000


def compress_image(input_path, output_path):
    try:
        img = Image.open(input_path)

        # 自动缩小尺寸
        if max_size:
            w, h = img.size
            if max(w, h) > max_size:
                scale = max_size / max(w, h)
                img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

        # 转为 RGB 避免 PNG alpha 问题
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # 导出 webp
        if convert_to_webp:
            output_path = output_path.rsplit(".", 1)[0] + ".webp"
            img.save(output_path, "webp", quality=quality, optimize=True)
        else:
            img.save(output_path, quality=quality, optimize=True)

        return f"✔ 压缩完成: {input_path} → {output_path}"

    except Exception as e:
        return f"✘ 失败: {input_path}, 错误: {e}"


def get_all_images():
    tasks = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in valid_ext:
                input_path = os.path.join(root, file)

                # 保持目录结构
                rel_dir = os.path.relpath(root, input_dir)
                save_dir = os.path.join(output_dir, rel_dir)
                os.makedirs(save_dir, exist_ok=True)
                output_path = os.path.join(save_dir, file)

                tasks.append((input_path, output_path))
    return tasks


def main():
    tasks = get_all_images()

    print(f"共发现 {len(tasks)} 张图片，开始多线程压缩...\n")

    # 线程数（可按 CPU 核心调整，建议 4~16）
    thread_count = 16

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        future_list = {executor.submit(compress_image, inp, out): (inp, out) for inp, out in tasks}

        for future in as_completed(future_list):
            print(future.result())


if __name__ == "__main__":
    main()

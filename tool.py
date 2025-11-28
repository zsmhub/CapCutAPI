# 将剪映位置坐标(X, Y)转换为比例值
def pixel_to_ratio(x: float, y: float, video_width: int, video_height: int) -> tuple[float, float]:
    """
    将视频像素坐标转换为剪映API所需的比例坐标

    参数:
        x: 像素坐标X值
        y: 像素坐标Y值
        video_width: 视频宽度（像素）
        video_height: 视频高度（像素）

    返回:
        转换后的比例坐标(x_ratio, y_ratio)，范围均在-1~1之间
    """
    x_ratio = x / video_width
    y_ratio = y / video_height

    return (x_ratio, y_ratio)
import paddlehub as hub
from pathlib import Path
import cv2
paths = [str(i) for i in Path('./img').glob('*.jpg')]  # 当前路径下所有.jpg文件
human_seg = hub.Module(name='deeplabv3p_xception65_humanseg')
results = human_seg.segmentation(paths=paths, visualization=True, output_dir='output')
# results = human_seg.segmentation(paths=paths, use_gpu=True, visualization=True, output_dir='output')  # 使用GPU
print(results)
# human_seg.save_inference_model(dirname='/img')

#
# human_seg = hub.Module(name="deeplabv3p_xception65_humanseg")
# result = human_seg.segmentation(images=[cv2.imread('/img/justin.jpg')])
# print(result)


import paddlehub as hub
import os
import datetime
current_time = datetime.datetime.now()
# print("current_time:    " + str(current_time))

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

# module = hub.Module(name='ernie_vilg')
# results = module.generate_image(text_prompts=['巨大的白色城堡'])

lac = hub.Module(name="lac")
test_text = ["方便面条干什么东西"]

results = lac.cut(text=test_text, use_gpu=True, batch_size=1, return_tag=True)
print(results)
print(datetime.datetime.now()-current_time)

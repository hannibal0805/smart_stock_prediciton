import matplotlib.pyplot as plt
from PIL import Image

# 读取所有图片
images = []
for i in range(1, 7):
    img_path = f'image{i}.png'
    img = Image.open(img_path)
    images.append(img)

# 创建一个新的大图
fig, axs = plt.subplots(2, 3, dpi=300)

# 将每张图片放置到合适的位置
for i, ax in enumerate(axs.flat):
    ax.imshow(images[i])
    ax.axis('off')

# 在左上角、上方中央和右上角添加文字
axs[0, 0].text(0.5, 0.95, 'RNN', ha='center', va='center', transform=axs[0, 0].transAxes, fontsize=9)
axs[0, 1].text(0.5, 0.95, 'LSTM', ha='center', va='center', transform=axs[0, 1].transAxes, fontsize=9)
axs[0, 2].text(0.5, 0.95, 'GRU', ha='center', va='center', transform=axs[0, 2].transAxes, fontsize=9)


# 调整布局
plt.tight_layout()

# 保存合并后的图片
plt.savefig('combined_images_with_text.png')

# 显示合并后的图片
plt.show()

import os
import matplotlib.pyplot as plt
from PIL import Image

dataset_path = os.getcwd() + '/dataset'
# cats = ['dew', 'fogsmog', 'frost', 'glaze', 'hail', 'lightning', 'rain', 'rainbow', 'rime', 'sandstorm', 'snow']
cats = ['hail', 'lightning', 'rain', 'sandstorm']

# cropping all images by remove 50 pixsels from top and bottom


def crop_all_images(input_folder, output_folder, crop=(0, 25, 0, 25)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        for filename in os.listdir(input_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                img = Image.open(os.path.join(input_folder, filename))
                img_cropped = img.crop(
                    (crop[0], crop[1], img.width - crop[2], img.height - crop[3])).convert('RGB')
                img_cropped.save(os.path.join(output_folder, filename))


for cat in cats:
    crop_all_images(dataset_path + '/' + cat, dataset_path + '/cropped/' + cat)

# converting all images to 256 x 256 pixels


def resize_images(input_folder, output_folder, size=(256, 256)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_folder, filename))
            img_resized = img.resize(size).convert('RGB')
            img_resized.save(os.path.join(output_folder, filename))


for cat in cats:
    resize_images(dataset_path + '/cropped/' + cat,
                  dataset_path + '/cropped_resized/' + cat)

# convert all images to grayscale
# Was not used in the final model
# the model was trained on RGB images

# def convert_to_grayscale(input_folder, output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     for filename in os.listdir(input_folder):
#         if filename.endswith(".jpg") or filename.endswith(".png"):
#             img = Image.open(os.path.join(input_folder, filename))
#             img = img.convert('L')
#             img.save(os.path.join(output_folder, filename))

# for cat in cats:
#     convert_to_grayscale(dataset_path + '/cropped_resized/' + cat, dataset_path + '/cropped_resized_grayscale/' + cat)


# Data Visualization

# Visualize the distribution of image sizes
image_sizes = []
for cat in cats:
    for filename in os.listdir(os.path.join(dataset_path, 'cropped_resized_grayscale', cat)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(
                dataset_path, 'cropped_resized_grayscale', cat, filename))
            image_sizes.append(img.size)

# Plot the distribution of image sizes
widths, heights = zip(*image_sizes)
plt.figure(figsize=(12, 6))
plt.hist(widths, bins=30, alpha=0.5, label='Widths')
plt.hist(heights, bins=30, alpha=0.5, label='Heights')
plt.xlabel('Pixels')
plt.ylabel('Frequency')
plt.title('Distribution of Image Sizes')
plt.legend()
plt.show()


# Visualize the distribution of image sizes for non-processed images
non_processed_image_sizes = []
for cat in cats:
    for filename in os.listdir(os.path.join(dataset_path, cat)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(dataset_path, cat, filename))
            non_processed_image_sizes.append(img.size)

# Plot the distribution of image sizes for non-processed images
non_processed_widths, non_processed_heights = zip(*non_processed_image_sizes)
plt.figure(figsize=(12, 6))
plt.hist(non_processed_widths, bins=30, alpha=0.5, label='Widths')
plt.hist(non_processed_heights, bins=30, alpha=0.5, label='Heights')
plt.xlabel('Pixels')
plt.ylabel('Frequency')
plt.title('Distribution of Non-Processed Image Sizes')
plt.legend()
plt.show()

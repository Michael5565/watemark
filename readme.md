# Watermark Removal

Digital images are often watermarked to protect them from unauthorized use. However, there may be legitimate reasons to remove these watermarks, such as restoring the original appearance of the image. This Python script provides a solution for this problem.

Using the power of the OpenCV library, this script implements an inpainting algorithm to effectively remove watermarks from images. Inpainting is a technique that reconstructs lost or deteriorated parts of images and videos. In this case, we use it to reconstruct the parts of the image that have been marked by the watermark.

The script is easy to use and requires only a few dependencies. With a simple binary mask indicating the watermark region, you can restore your images to their original, watermark-free state.


## Dependencies

- OpenCV
- NumPy

You can install these packages using pip:

```bash
pip install opencv-python numpy
```

## Usage

The script defines a function `remove_watermark` that takes an image, a binary mask indicating the watermark region, and optional parameters for the inpainting radius and method. It returns a new image with the watermark removed.

Here's an example of how to use it:

```python
# Read the original image
image_path = input("Enter watermarked image: ")
original_image = cv2.imread(image_path)

# Create a binary mask for the watermark region (adjust as needed)
watermark_mask = np.zeros_like(original_image[:, :, 0])
x_min = int(input("Enter x_min: "))
y_min = int(input("Enter y_min: "))
watermark_width = int(input("Enter watermark width: "))
watermark_height = int(input("Enter watermark height: "))
watermark_mask[y_min:y_min+watermark_height, x_min:x_min+watermark_width] = 1

# Remove the watermark using inpainting
watermark_removed_image = remove_watermark(original_image, watermark_mask)

# Save the modified image
output_path = "watermark_removed_image.jpg"
cv2.imwrite(output_path, watermark_removed_image)
print(f"Watermark removed and saved as {output_path}")
```

Please adjust the coordinates and dimensions of the watermark region as needed.
```
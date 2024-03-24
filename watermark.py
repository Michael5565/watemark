import cv2
import numpy as np

def remove_watermark(image, watermark_mask, inpaint_radius=3, inpaint_method=cv2.INPAINT_NS):
    
    """
    Removes a watermark from an image using inpainting.

    Args:
        image: The image to remove the watermark from.
        watermark_mask: A binary mask indicating the watermark region (1 for watermark, 0 for non-watermark).
        inpaint_radius: The radius of the circular region around the watermark area to be inpainted.
        inpaint_method: The inpainting algorithm to be used. /cv2.INPAINT_NS.

    Returns:
        A new image with the watermark removed.
    """
    # Create a copy of the input image to avoid modifying the original
    output_image = image.copy()

    # Convert the mask to 8-bit format
    watermark_mask = watermark_mask.astype(np.uint8)

    # Inpaint the watermark region
    output_image = cv2.inpaint(output_image, watermark_mask, inpaint_radius, inpaint_method)

    return output_image

# Example usage:
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
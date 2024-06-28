#!/usr/bin/env python3

import gradio as gr
from facefusion import core  # Adjust based on the actual file name and class location

def face_fusion(image1, image2):
    fusion_model = FaceFusion()  # Initialize the FaceFusion model
    result_image = fusion_model.fuse(image1, image2)  # Fuse the images
    return result_image

iface = gr.Interface(
    fn=face_fusion,
    inputs=["image", "image"],
    outputs="image",
    title="Face Fusion",
    description="Upload two images to fuse them together."
)

if __name__ == "__main__":
    iface.launch(share=True)  # This will provide a public URL

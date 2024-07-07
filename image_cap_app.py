import os
import gradio as gr
from transformers import pipeline
from PIL import Image

# Initialize the image-to-text pipeline with the specified model
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def launch(input):
    """
    Function to generate image caption.
    Args:
    input (PIL.Image): Input image for captioning.
    Returns:
    str: Generated caption for the input image.
    """
    out = pipe(input)
    return out[0]['generated_text']

# Create a Gradio interface for the image-to-text pipeline
iface = gr.Interface(
    fn=launch,             # Function to generate captions
    # inputs=gr.Image(type='pil'),  # Input type: Image (PIL format)
    # outputs="text"         # Output type: Text
    inputs=gr.Image(type='pil', label="Upload Image"),  # Input type: Image (PIL format) with a label
    outputs=gr.Textbox(label="Generated Caption"),      # Output type: Text with a label
    title="Image Captioning App",                       # Title of the Gradio app
    description="Upload an image to get a generated caption using the BLIP model.",  # Description of the app
    theme="compact",                                    # Set a theme for the app
)

# Launch the Gradio interface
iface.launch()

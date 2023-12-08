import gradio as gr
import sys
sys.path.append("..")

import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse


from deepvog.model.DeepVOG_model import load_DeepVOG
from deepvog.inferer import gaze_inferer

MODEL = load_DeepVOG()

def infer(video):

    inferer = gaze_inferer(
        MODEL, 
        6, 
        (240, 320), 
        (3.6, 4.8),
        infer_gaze_flag=False
    )
    inferer.process(
        video_src=video, 
        mode="Infer", 
        batch_size=512,
        output_record_path=None, 
        output_video_path="", 
        heatmap=False,
        print_prefix=""
    )

    return inferer.vid_manager.output_video_path
    
demo = gr.Interface(infer, gr.Video(), "playable_video")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", share=False)
import tempfile
from pathlib import Path
from typing import Optional

import gradio

from educationswap import state_manager, translator
from educationswap.uis.core import register_ui_component

OUTPUT_PATH_TEXTBOX : Optional[gradio.Textbox] = None
OUTPUT_IMAGE : Optional[gradio.Image] = None
OUTPUT_VIDEO : Optional[gradio.Video] = None
OUTPUT_FILE : Optional[gradio.File] = None


def render() -> None:
	global OUTPUT_PATH_TEXTBOX
	global OUTPUT_IMAGE
	global OUTPUT_VIDEO
	global OUTPUT_FILE

	if not state_manager.get_item('output_path'):
		gdrive_directory = Path('/content/drive/MyDrive/EducationSwap/outputs')
		documents_directory = Path.home().joinpath('Documents')

		if gdrive_directory.exists():
			state_manager.set_item('output_path', str(gdrive_directory))
		elif documents_directory.exists():
			state_manager.set_item('output_path', documents_directory)
		else:
			state_manager.set_item('output_path', tempfile.gettempdir())
	OUTPUT_PATH_TEXTBOX = gradio.Textbox(
		label = translator.get('uis.output_path_textbox'),
		value = state_manager.get_item('output_path'),
		max_lines = 1
	)
	OUTPUT_IMAGE = gradio.Image(
		label = translator.get('uis.output_image_or_video'),
		visible = False
	)
	OUTPUT_VIDEO = gradio.Video(
		label = translator.get('uis.output_image_or_video')
	)
	OUTPUT_FILE = gradio.File(
		label = translator.get('uis.output_file'),
		visible = False
	)


def listen() -> None:
	OUTPUT_PATH_TEXTBOX.change(update_output_path, inputs = OUTPUT_PATH_TEXTBOX)
	register_ui_component('output_image', OUTPUT_IMAGE)
	register_ui_component('output_video', OUTPUT_VIDEO)
	register_ui_component('output_file', OUTPUT_FILE)


def update_output_path(output_path : str) -> None:
	state_manager.set_item('output_path', output_path)

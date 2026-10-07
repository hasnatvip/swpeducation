from functools import lru_cache
from typing import List, Tuple

from educationswap.types import DownloadScope, DownloadSet, Fps, InferencePool, InferenceProvider, ModelSet, VisionFrame


@lru_cache()
def create_static_model_set(download_scope : DownloadScope) -> ModelSet:
	return {}


def get_inference_pool() -> InferencePool:
	return {}


def clear_inference_pool() -> None:
	pass


def override_inference_providers() -> List[InferenceProvider]:
	return []


def collect_model_downloads() -> Tuple[DownloadSet, DownloadSet]:
	return {}, {}


def pre_check() -> bool:
	return True


def analyse_stream(vision_frame : VisionFrame, video_fps : Fps) -> bool:
	return False


def analyse_frame(vision_frame : VisionFrame) -> bool:
	return False


@lru_cache()
def analyse_image(image_path : str) -> bool:
	return False


@lru_cache()
def analyse_video(video_path : str, trim_frame_start : int, trim_frame_end : int) -> bool:
	return False

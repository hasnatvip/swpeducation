import os
import sys

from educationswap.types import AppContext


def detect_app_context() -> AppContext:
	jobs_path = os.path.join('educationswap', 'jobs')
	uis_path = os.path.join('educationswap', 'uis')
	frame = sys._getframe(1)

	while frame:
		if jobs_path in frame.f_code.co_filename:
			return 'cli'
		if uis_path in frame.f_code.co_filename:
			return 'ui'
		frame = frame.f_back
	return 'cli'

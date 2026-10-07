from typing import List, Sequence, get_args

from educationswap.common_helper import create_float_range
from educationswap.processors.modules.lip_syncer.types import LipSyncerModel

lip_syncer_models : List[LipSyncerModel] = list(get_args(LipSyncerModel))

lip_syncer_weight_range : Sequence[float] = create_float_range(0.0, 1.0, 0.05)

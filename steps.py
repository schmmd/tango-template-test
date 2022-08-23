"""
Example Python module where you can define your steps.
"""

import torch
from tango import Step


@Step.register("torch_hello")
class HelloTorchStep(Step):
    """
    This step just prints out a greeting and whether or not Torch finds any
    CUDA-enabled GPU devices.

    It has a single input: `name`.
    """

    VERSION = "001"

    def run(self, name: str) -> str:  # type: ignore[override]
        self.logger.info("Hello, %s!", name)
        if torch.cuda.is_available():
            msg = "CUDA is available!"
        else:
            msg = "No CUDA :("
        self.logger.info(msg)
        return msg

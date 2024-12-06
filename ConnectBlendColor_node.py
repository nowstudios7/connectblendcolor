class ConnectBlendColor:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_1": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "comparison_value": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "comparison_type": (["greater_than", "less_than", "greater_or_equal", "less_or_equal", "equal_to"],),
            }
        }

    RETURN_TYPES = ("BOOL", "INT")
    FUNCTION = "compare"

    CATEGORY = "Connect Blend Color"

    def compare(self, input_1, comparison_value, comparison_type):
        inputs = [input_1]

        # Iterate through inputs to find if any value meets the comparison condition
        for i, value in enumerate(inputs):
            if comparison_type == "greater_than" and value > comparison_value:
                return (True, i + 1)
            elif comparison_type == "less_than" and value < comparison_value:
                return (True, i + 1)
            elif comparison_type == "greater_or_equal" and value >= comparison_value:
                return (True, i + 1)
            elif comparison_type == "less_or_equal" and value <= comparison_value:
                return (True, i + 1)
            elif comparison_type == "equal_to" and value == comparison_value:
                return (True, i + 1)
        
        # If none of the values meet the condition, return False and 0
        return (False, 0)

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ConnectBlendColor": ConnectBlendColor
}

# Human-readable name for the node
NODE_DISPLAY_NAME_MAPPINGS = {
    "ConnectBlendColor": "Connect - Blend Color"
}

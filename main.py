#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from response.crew import Response

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A RFP response document generation system for a generating response based on the given inputs.
The system should allow users to give the following inputs and each of these inputs should be assigned to a variable having the same name as the input.
1. RFP objectives
2. Current operational pain points
3. Areas of support
The inputs obtained should be assigned to a variable and a function should be created which will call the gpt-4o llm model using the input obtained to generate the executive summary. 
The output generated from the gpt-4o llm model should given as the output of the system 
"""
module_name = "accounts.py"
class_name = "Account"

def run():
    """
    Run the response crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = Response().crew().kickoff(inputs=inputs)
    
if __name__ == "__main__":
    run()
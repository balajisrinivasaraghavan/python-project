# app.py

import gradio as gr
from accounts import Account

def generate_summary(rfp_objectives, current_operational_pain_points, areas_of_support):
    # Create an Account instance with the provided inputs
    account = Account(
        rfp_objectives=rfp_objectives,
        current_operational_pain_points=current_operational_pain_points,
        areas_of_support=areas_of_support
    )
    # Generate and return the executive summary
    return account.generate_executive_summary()

# Define the Gradio interface
inputs = [
    gr.Textbox(label="RFP Objectives"),
    gr.Textbox(label="Current Operational Pain Points"),
    gr.Textbox(label="Areas of Support")
]

outputs = gr.Textbox(label="Executive Summary")

# Create the interface
interface = gr.Interface(
    fn=generate_summary,
    inputs=inputs,
    outputs=outputs,
    title="RFP Response Document Generator",
    description="Generate an executive summary for RFP responses based on the provided inputs."
)

if __name__ == "__main__":
    interface.launch()
# Repurposed LLM Phishing Classifier

## Overview
This project demonstrates how to repurpose a Large Language Model (Llama 3.2) for binary classification of phishing messages. 

Instead of training a traditional classifier, I fine-tune an LLM twice to either: 

1. act as a specialised classification system that outputs either "true" or "false" when presented with potentially malicious messages;
2. act as a pure sequence classifier that outputs a tensor which is then converted to a class label.

## Approach
The project implements two distinct approaches:
1. **Causal Language Modeling**: Fine-tuning the model to generate "true" or "false" responses using chat templates
2. **Sequence Classification**: Adapting the model for binary classification using a classification head

Both approaches use LoRA (Low-Rank Adaptation) to efficiently tune the model while maintaining a small parameter footprint.

## Model Architecture
- Base Model: Llama 3.2 3B
- Adaptation: LoRA
- Special Tokens:
  - `<|start_header_id|>`
  - `<|end_header_id|>`
  - `<|eot_id|>`

## Results
Detailed evaluation results, including:
- Accuracy metrics
- Confusion matrices

Can be found in the `model_evaluation` notebooks in this repository.

## Technical Notes
- The model uses specific chat templates for consistent input formatting
- Both approaches demonstrate decent classification capabilities with different tradeoffs, but the sequence classifier demonstrates exceptional recall when dealing with phishing messages.

## Simplified Repository Structure (there are more files lying around)

```
├── notebooks/
│   ├── model_evaluation_causal.ipynb    # Causal LM approach evaluation
│   └── model_evaluation_seq_cls.ipynb   # Sequence classification evaluation
├── src/
│   └── utils/                           # Utilities
└── processed_data/                      # Processed dataset files
```

For detailed implementation and performance metrics, please refer to the notebooks.

## Future work

Abstract one of the models behind an API. 


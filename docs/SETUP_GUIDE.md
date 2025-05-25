# Setup Guide: Modal Deployments for Devstral 24B

This guide provides a rigorous, step-by-step process for configuring, fine-tuning, and deploying large language models (LLMs) using Modal Labs and Ollama, with a focus on the Devstral 24B model for advanced coding and agentic workflows.

## Prerequisites

- Python 3.11 or higher (recommended for compatibility with modern ML libraries)
- Git (for version control and reproducibility)
- Modal Labs account ([modal.com](https://modal.com))
- (Optional) Ollama installed locally for rapid prototyping
- Sufficient hardware resources (GPU recommended for training and inference)

## Repository Structure

Refer to the main `README.md` for a detailed breakdown of the project architecture, including configuration, source code, and deployment modules.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/modal-deployments.git
   cd modal-deployments
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   # or
   poetry install
   ```

3. **Configure Modal Labs authentication:**

   ```bash
   modal token new
   ```

4. **Review and edit configuration files:**
   - `config/model_config.yaml`: Model, deployment, and monitoring parameters
   - `config/training_config.yaml`: Fine-tuning and optimization settings
   - `config/Modelfile`: Ollama model definition for custom builds
   - `config/ollama.service`: Systemd service for Ollama orchestration

## Modal Labs Deployment

To deploy the Devstral 24B model as a cloud-native API with Modal Labs:

```bash
modal deploy src/deployment/devstral_modal_deployment.py
```

This will provision a GPU-accelerated container, initialize the Ollama service, pull the base model, and expose a FastAPI endpoint for chat completions and tool-calling workflows.

## Local Development & Testing

For rapid iteration and debugging, you may run the API locally:

```bash
python setup/quick_start.py
python examples/simple_example.py
```

## Fine-Tuning Workflow

1. **Prepare datasets:**

   - Place or symlink datasets in the `data/` directory
   - Supported formats: Hugging Face Datasets, CSV, JSONL

2. **Edit `config/training_config.yaml`** to specify learning rate, batch size, LoRA parameters, and checkpointing.

3. **Run fine-tuning:**

   - Use `src/core/ollama_finetune_system.py` for advanced, reproducible fine-tuning with reasoning and code datasets.

4. **Monitor progress:**
   - Integrate with Weights & Biases (W&B) and logging as configured in `config/model_config.yaml`.

## Advanced Topics

- **Custom Modelfile:** Edit `config/Modelfile` to define system prompts, adapters, or quantization for Ollama builds.
- **API Extension:** Extend `src/deployment/devstral_modal_deployment.py` to add new endpoints, authentication, or tool integrations.
- **Security:** Use pre-commit hooks, static analysis, and dependency scanning for production deployments.

## Troubleshooting

- See `docs/TROUBLESHOOTING.md` for solutions to common issues with Modal Labs, Ollama, or model configuration.
- For advanced debugging, enable verbose logging in `config/model_config.yaml`.

## Support

For academic collaboration, enterprise support, or technical questions, please contact the maintainers or open an issue on GitHub.

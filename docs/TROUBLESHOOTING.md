# Troubleshooting Guide: Modal Deployments & Devstral 24B

This guide addresses common issues encountered when deploying, fine-tuning, or operating large language models (LLMs) with Modal Labs and Ollama, specifically for the Devstral 24B configuration. It is intended for advanced users, including researchers and professional engineers.

## Modal Labs Deployment Issues

### Problem: Deployment Fails or Times Out

- **Check Modal Labs Quota:** Ensure your account has sufficient GPU/CPU quota.
- **Container Logs:** Inspect logs via the Modal Labs dashboard for errors in service startup, model download, or API initialization.
- **Network Configuration:** Verify that required ports (e.g., 8000 for FastAPI) are open and not blocked by firewalls.

### Problem: Model Not Found or Fails to Load

- **Model Name Consistency:** Confirm that `MODEL_NAME` and `CUSTOM_MODEL_NAME` in your deployment script match those in `config/model_config.yaml` and your Modelfile.
- **Ollama Service Health:** Use `systemctl status ollama` or check the Ollama API health endpoint to ensure the service is running.
- **Disk Space:** Large models require significant disk space; check available storage on your deployment node.

## Ollama & Model Management

### Problem: Ollama Service Fails to Start

- **Systemd Configuration:** Review `config/ollama.service` for correct paths and permissions.
- **Dependency Installation:** Ensure all dependencies (curl, systemd, etc.) are installed in your Modal image or local environment.
- **Service Logs:** Use `journalctl -u ollama` for detailed logs.

### Problem: Custom Model Creation Fails

- **Modelfile Syntax:** Validate your `config/Modelfile` for correct syntax and supported directives.
- **Base Model Availability:** Ensure the base model is available in the Ollama registry or has been pulled successfully.
- **Resource Limits:** Increase container memory or disk allocation if model creation fails due to OOM or storage errors.

## Fine-Tuning & Training

### Problem: Training Process Crashes or Hangs

- **Batch Size & Sequence Length:** Reduce batch size or sequence length in `config/training_config.yaml` to fit available GPU memory.
- **LoRA Configuration:** Ensure LoRA parameters are compatible with your model architecture.
- **PyTorch/CUDA Errors:** Check CUDA version compatibility and driver installation.

### Problem: Poor Model Performance

- **Dataset Quality:** Review and clean your training datasets for noise, duplicates, or label errors.
- **Overfitting:** Adjust regularization parameters (weight decay, dropout) and monitor validation loss.
- **Evaluation Metrics:** Use appropriate metrics for your task (e.g., BLEU for code, accuracy for reasoning).

## API & Tooling

### Problem: API Not Responding

- **CORS Configuration:** Ensure CORS is enabled in your FastAPI app for cross-origin requests.
- **Rate Limiting:** Check API rate limiting settings in `config/model_config.yaml`.
- **Error Logs:** Inspect FastAPI and Ollama logs for stack traces or error messages.

### Problem: Tool-Calling Fails

- **Tool Schema:** Validate tool definitions and ensure they are included in the API payload.
- **Function Permissions:** Grant necessary permissions for external tool invocation in your deployment environment.

## Advanced Debugging

- **Enable Debug Logging:** Set logging level to `DEBUG` in `config/model_config.yaml` for verbose output.
- **Interactive Shell:** Use `modal shell` or VS Code remote containers for live debugging.
- **Test Suites:** Run unit, integration, and e2e tests in the `tests/` directory to isolate failures.

## Getting Help

- Consult the [Modal Labs documentation](https://modal.com/docs) and [Ollama documentation](https://ollama.ai/docs) for platform-specific issues.
- For unresolved problems, open an issue on GitHub with detailed logs, configuration files, and system information.

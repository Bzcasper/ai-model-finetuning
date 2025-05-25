#!/bin/bash
# 🚀 Automatic Setup Script for AI Model Fine-tuning
# This script installs everything you need automatically

echo "🎯 Welcome to the AI Model Fine-tuning Setup!"
echo "This will install everything you need to get started."
echo ""

# Colors for pretty output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
print_status "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d" " -f2)
    print_success "Python $PYTHON_VERSION found!"
else
    print_error "Python 3 is not installed. Please install Python 3.8 or newer."
    exit 1
fi

# Check Python version
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
    print_success "Python version is compatible!"
else
    print_error "Python 3.8 or newer is required. Found: $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment
print_status "Creating virtual environment..."
python3 -m venv ai_env
source ai_env/bin/activate
print_success "Virtual environment created and activated!"

# Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Install required packages
print_status "Installing required Python packages..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    print_success "All packages installed successfully!"
else
    print_error "Failed to install some packages. Check the error messages above."
    exit 1
fi

# Check if Git is installed
print_status "Checking Git installation..."
if command -v git &> /dev/null; then
    print_success "Git is installed!"
else
    print_warning "Git is not installed. You'll need it for version control."
    echo "Install Git from: https://git-scm.com/downloads"
fi

# Create necessary directories
print_status "Creating project directories..."
mkdir -p data/raw data/processed models/checkpoints models/final logs config

# Copy example configuration files
print_status "Setting up configuration files..."
cp config/training_config.example.yaml config/training_config.yaml 2>/dev/null || true
cp config/model_config.example.yaml config/model_config.yaml 2>/dev/null || true

print_success "Configuration files created!"

# Set up environment variables template
print_status "Creating environment variables template..."
cat > .env.template << EOL
# AI Model Fine-tuning Environment Variables
# Copy this file to .env and fill in your actual values

# Modal Labs
MODAL_TOKEN_ID=your_modal_token_id_here
MODAL_TOKEN_SECRET=your_modal_token_secret_here

# Hugging Face
HUGGINGFACE_TOKEN=your_huggingface_token_here

# Weights & Biases (optional, for monitoring)
WANDB_API_KEY=your_wandb_api_key_here

# Model Configuration
MODEL_NAME=devstral-coding-assistant
TRAINING_DATA_PATH=data/processed/training_data.json
EOL

print_success "Environment template created!"

# Run system check
print_status "Running system compatibility check..."
python setup/check_requirements.py

if [ $? -eq 0 ]; then
    print_success "System check passed!"
else
    print_warning "Some system checks failed. See messages above."
fi

echo ""
echo "🎉 Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Copy .env.template to .env and fill in your API keys"
echo "2. Run: python scripts/quick_start.py"
echo "3. Follow the interactive setup to connect your accounts"
echo ""
echo "Need help? Check docs/SETUP_GUIDE.md for detailed instructions!"

"""
🎯 Simple Example: Your First AI Model Interaction
This example shows the basics of using the AI model fine-tuning system.
"""

import os
import sys
from pathlib import Path

# Add src to path so we can import our modules
sys.path.append(str(Path(__file__).parent.parent / "src"))


def run_basic_test():
    """Run a basic test to make sure everything works."""
    print("🧪 Running basic system test...")
    try:
        # Test 1: Check if we can import required modules
        print("📦 Testing imports...")
        import datasets
        import torch
        import transformers

        print("✅ All imports successful!")

        # Test 2: Check if we can load a simple model
        print("🤖 Testing model loading...")
        from transformers import AutoModelForCausalLM, AutoTokenizer

        model_name = "microsoft/DialoGPT-small"  # Small model for testing
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        # Add padding token if it doesn't exist
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        print("✅ Model loading successful!")

        # Test 3: Try a simple conversation
        print("💬 Testing conversation...")
        user_input = "Hello, can you help me with Python?"
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        print(f"User: {user_input}")
        print(f"✅ Input processed successfully! Token length: {inputs.shape[1]}")
        print("\n🎉 Basic test completed successfully!")
        print("Your system is ready for AI model fine-tuning!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def demonstrate_tokenization():
    """Show how text gets converted to tokens (numbers) for AI models."""
    print("\n🔤 Understanding Tokenization")
    print("=" * 40)
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    examples = ["Hello world!", "def hello(): return 'world'", "print('Hello, AI!')"]
    for text in examples:
        tokens = tokenizer.tokenize(text)
        token_ids = tokenizer.encode(text)
        print(f"\nText: {text}")
        print(f"Tokens: {tokens}")
        print(f"Token IDs: {token_ids}")
        print(f"Number of tokens: {len(tokens)}")


def demonstrate_dataset_format():
    """Show what training data looks like."""
    print("\n📊 Understanding Training Data Format")
    print("=" * 40)
    training_examples = [
        {
            "instruction": "Write a Python function to add two numbers",
            "input": "",
            "output": "def add_numbers(a, b):\n    return a + b",
        },
        {
            "instruction": "Debug this Python code",
            "input": "def greet(name):\n    print('Hello' + name)",
            "output": "def greet(name):\n    print('Hello, ' + name)  # Added comma and space",
        },
        {
            "instruction": "Explain this code",
            "input": "for i in range(5):\n    print(i)",
            "output": "This code uses a for loop to print numbers 0 through 4. The range(5) creates a sequence from 0 to 4.",
        },
    ]
    print("Here's what training data looks like:")
    for i, example in enumerate(training_examples, 1):
        print(f"\nExample {i}:")
        print(f"  Instruction: {example['instruction']}")
        if example["input"]:
            print(f"  Input: {example['input']}")
        print(f"  Expected Output: {example['output']}")


def main():
    """Run all examples."""
    print("🎯 Simple AI Model Fine-tuning Examples")
    print("=" * 50)
    success = run_basic_test()
    if success:
        demonstrate_tokenization()
        demonstrate_dataset_format()
        print("\n🚀 What's Next?")
        print("- Try: python examples/advanced_example.py")
        print("- Start training: python src/model_trainer.py")
        print("- Read more: docs/CONCEPTS.md")
    else:
        print("\n❌ Basic test failed. Please fix the issues above first.")
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

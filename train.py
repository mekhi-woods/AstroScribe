# 05/02/2025 -- M. D. Woods
# train.py

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset import ObservatoryDataset
from model import ObservatoryProposalModel

# Hyperparameters
EMBED_DIM = 256
HIDDEN_DIM = 512
BATCH_SIZE = 16
EPOCHS = 10
LEARNING_RATE = 1e-3

# Dummy vocab size for prototype (replace with actual tokenizer size)
VOCAB_SIZE = 10000

def train():
    # Load dataset
    dataset = ObservatoryDataset('data/raw_prompts.csv')
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    # Initialize model
    model = ObservatoryProposalModel(VOCAB_SIZE, EMBED_DIM, HIDDEN_DIM)
    model = model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # Training loop
    for epoch in range(EPOCHS):
        model.train()
        total_loss = 0
        for src, tgt_input, tgt_output in dataloader:
            src, tgt_input, tgt_output = src.to(model.device), tgt_input.to(model.device), tgt_output.to(model.device)

            optimizer.zero_grad()
            output = model(src, tgt_input)
            loss = criterion(output.view(-1, VOCAB_SIZE), tgt_output.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {total_loss / len(dataloader):.4f}")

    # Save model
    torch.save(model.state_dict(), "models/observatory_model.pt")

if __name__ == "__main__":
    train()

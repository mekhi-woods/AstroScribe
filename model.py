# 05/02/2025 -- M. D. Woods
# model.py

import torch
import torch.nn as nn

class ObservatoryProposalModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.encoder = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.decoder = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.output_layer = nn.Linear(hidden_dim, vocab_size)

    def forward(self, src, tgt):
        # Embed input sequences
        embedded_src = self.embedding(src)
        _, (hidden, cell) = self.encoder(embedded_src)

        # Embed target sequences for teacher forcing
        embedded_tgt = self.embedding(tgt)
        decoder_outputs, _ = self.decoder(embedded_tgt, (hidden, cell))

        # Project to vocab size
        output = self.output_layer(decoder_outputs)
        return output

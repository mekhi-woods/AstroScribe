# 🔭 AstroScipte: An Observatory Proposal Assistant

**AstroScipte** is a lightweight, PyTorch-based tool that helps astronomers, students, and researchers generate draft observing proposals for professional telescopes like **Gemini**, **JWST**, and **Keck** from natural language descriptions of their science goals.

---

## 🚀 Project Overview

**AstroScipte** enables users to describe their scientific goals in plain English and receive a structured, professional-grade draft proposal tailored for a specific telescope and instrument. The tool uses OpenAI's language model to generate well-formatted sections typically required by observatories, saving time and helping users get started with proposal writing.

---

## ✨ Key Features

- 📝 **Plain Language Input**: Describe your science goal naturally
- 🔧 **Telescope/Instrument Selector**: Choose from supported facilities (e.g., Gemini/GMOS, JWST/NIRCam)
- 📄 **AI-Generated Proposal Draft**:
  - Scientific Justification
  - Technical Justification
  - Instrument Setup
  - Observing Strategy
  - Time Request
- 📤 *(Coming Soon)*: Export to PDF or LaTeX
- 🔭 *(Coming Soon)*: Fetch object metadata from SIMBAD/NED

---

## 🎯 Use Cases

- Students writing their first observing proposal
- Researchers rapidly prototyping proposal drafts
- Educators and outreach staff demonstrating proposal writing

---

## 🛠️ Tech Stack

- PyTorch – core model framework
- Custom seq2seq model (LSTM or Transformer) torchtext or Hugging Face tokenizer – preprocessing
- Gradio (planned) – interactive UI for demo
- LaTeX export (planned) – for generating formatted PDFs

---

## 📦 Getting Started

Coming soon: a Jupyter prototype and Streamlit app!

---

## ✅ Progress

- [x] Define project scope and structure
- [ ] Collect sample proposals and generate prompt-response pairs
- [ ] Build dataset loader and tokenizer
- [ ] Train initial model (LSTM baseline)
- [ ] Evaluate accuracy and coherence
- [ ] Deploy via Gradio or Streamlit

---

## 🧠 Inspiration

Time Allocation Committees (TACs) are competitive, and writing a clear, compelling proposal takes time. Observatory Assistant helps reduce the friction by offering instant drafts and guidance — like having an AI science writer on your team.

---

## 🧱 Project Scructure

```
AstroScribe/ 
├── data/                  # Training CSV and tokenized outputs 
├── models/                # Saved model checkpoints 
├── notebooks/             # Experiment notebooks 
├── train.py               # Model training script 
├── evaluate.py            # Evaluation and testing 
├── dataset.py             # Data loader + preprocessing 
├── model.py               # Model architecture (LSTM, Transformer, etc.) 
└── README.md 
```
---

## 📄 License

MIT License

---

## ✍️ Author
[Mekhi Woods](https://tinyurl.com/astrokhi) (mekhidwoods@gmail.com)

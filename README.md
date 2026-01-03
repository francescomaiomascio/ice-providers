# ice-providers

**ice-providers** contains concrete provider implementations for the ICE ecosystem.

This repository hosts *infrastructure-level integrations* such as:
- Embedding providers (OpenAI, Ollama, GGUF, llama.cpp, etc.)
- LLM backends
- External inference or model-serving adapters

It does **not** contain orchestration logic, runtime lifecycle management, or cognitive behavior.

---

## Architecture Position

`ice-providers` sits **outside** the ICE core domains.

High-level architecture:

Runtime
↓
Engine (contracts, orchestration, semantics)
↓
Providers (this repository)


### Key principles

- **ICE Engine defines the interfaces**
- **Providers only implement those interfaces**
- **Runtime never talks to providers directly**
- Providers are *replaceable, optional, and external*

---

## What belongs here

✅ Concrete provider implementations  
✅ External backends and services  
✅ Infrastructure-specific logic  

Examples:
- OpenAI embeddings
- Ollama local inference
- GGUF / llama.cpp loaders
- Mock providers for testing

---

## What does NOT belong here

❌ Orchestrator  
❌ Runtime lifecycle  
❌ Session management  
❌ Cognitive logic  
❌ Agent reasoning  
❌ Business rules  

Those live in other ICE repositories.

---

## Repository structure (example)

```
ice_providers/
└── embeddings/
├── openai/
│ └── provider.py
├── ollama/
│ └── provider.py
├── llamacpp/
│ └── provider.py
└── mock/
└── provider.py
```


Each provider implements an interface defined in `ice-engine`.

---

## Usage

Providers are discovered and wired by **ICE Engine**, not manually instantiated here.

This repository can be used:
- as a dependency of ICE Engine
- as a reference for building custom providers
- as a public catalog of supported backends

---

## Status

This repository is **intentionally minimal** and **intentionally boring**.

All complexity lives in:
- ICE Engine (contracts and orchestration)
- ICE Runtime (execution and lifecycle)

---

## License

MIT

---
title: OpenClaw AI Agent
emoji: 🦞
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# OpenClaw AI Agent

This is a hosted instance of the [OpenClaw](https://openclaw.ai) AI Agent.

## 🚀 Deployment Info

- **SDK**: Docker
- **Port**: 7860 (Hugging Face Default)
- **Status**: Running

## 🔐 Security

This Space is running in a container. To use it:
1. Access the web UI via the **App** tab.
2. If prompted for a token, use the one configured in `openclaw.json` (default in this Dockerfile is `admin-token-123`).
3. **Important**: Add your `OPENROUTER_API_KEY` (and any other keys) to the **Hugging Face Space Secrets** in Settings.

## 📂 Project Structure

- `workspace/`: Contains the agent's soul, tools, and identity.
- `Dockerfile`: Sets up the Node.js environment and OpenClaw gateway.

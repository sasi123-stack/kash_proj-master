FROM node:20

# Set environment variables
ENV HOME=/home/node
ENV OPENCLAW_HOME=/home/node/.openclaw
ENV OPENCLAW_GATEWAY_PORT=7860
ENV OPENCLAW_GATEWAY_BIND=0.0.0.0
ENV NODE_ENV=production

# Install system dependencies
RUN apt-get update && apt-get install -y \
    procps \
    git \
    && rm -rf /var/lib/apt/lists/*

# Switch to node user before installing
USER node
WORKDIR /home/node

# Install OpenClaw locally in this folder
RUN npm install openclaw

# Create necessary directories
RUN mkdir -p $OPENCLAW_HOME/workspace

# Copy workspace files from the build context
COPY --chown=node:node workspace $OPENCLAW_HOME/workspace

# Create a streamlined openclaw.json for Cloud environment
RUN echo '{\n\
  "meta": {\n\
    "lastTouchedVersion": "2026.2.15"\n\
  },\n\
  "agents": {\n\
    "defaults": {\n\
      "model": {\n\
        "primary": "openrouter/auto"\n\
      },\n\
      "workspace": "/home/node/.openclaw/workspace"\n\
    }\n\
  },\n\
  "gateway": {\n\
    "port": 7860,\n\
    "mode": "cloud",\n\
    "bind": "any",\n\
    "auth": {\n\
      "mode": "token",\n\
      "token": "admin-token-123"\n\
    }\n\
  }\n\
}' > $OPENCLAW_HOME/openclaw.json

# Expose the Hugging Face port
EXPOSE 7860

# Start the gateway using npx (most reliable for finding the module)
CMD ["npx", "openclaw", "gateway", "--port", "7860", "--bind", "0.0.0.0"]
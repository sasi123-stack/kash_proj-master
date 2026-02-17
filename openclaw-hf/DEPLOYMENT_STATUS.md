# ✅ FINAL - Working Dockerfile Configuration

## 🎯 Current Status: SIMPLIFIED & WORKING

After troubleshooting, here's the final working configuration:

---

## 📝 Key Changes

### What We Simplified:
1. ❌ **Removed**: Explicit `--config` flag (OpenClaw finds it automatically)
2. ❌ **Removed**: API key from config file (uses environment variable)
3. ❌ **Removed**: Explicit port/bind flags (uses config file)
4. ✅ **Kept**: Simple `CMD ["npx", "openclaw", "gateway"]`

### Why This Works:
- OpenClaw automatically looks for config in `$OPENCLAW_HOME/openclaw.json` ✅
- OpenClaw reads `OPENROUTER_API_KEY` from environment ✅
- Config file specifies gateway mode and port ✅
- Simpler = fewer points of failure ✅

---

## 🚀 Deployment Instructions

### 1. Upload to Hugging Face

Upload these files to your Space:
```
openclaw-hf/
├── Dockerfile
├── README.md
└── workspace/
    ├── AGENTS.md
    ├── SOUL.md
    ├── IDENTITY.md
    ├── TOOLS.md
    ├── HEARTBEAT.md
    ├── BOOTSTRAP.md
    ├── USER.md
    └── .openclaw/
        └── workspace-state.json
```

### 2. Add Environment Variable

**CRITICAL**: Add this to Space Secrets:

- **Name**: `OPENROUTER_API_KEY`
- **Value**: Your OpenRouter API key (from https://openrouter.ai/keys)
- **Type**: Secret ✅ (not Variable)

### 3. Wait for Build

Build time: ~10-15 minutes

Expected logs:
```
✅ Installing openclaw...
✅ Building node-llama-cpp...
✅ Creating config...
✅ Starting gateway...
✅ Ready on port 7860
```

---

## 🔧 Environment Variables

### Required:
- `OPENROUTER_API_KEY` - Your OpenRouter API key

### Auto-Set (by Dockerfile):
- `OPENCLAW_HOME=/home/node/.openclaw`
- `OPENCLAW_GATEWAY_PORT=7860`
- `NODE_ENV=production`

---

## 📊 Config File Structure

The Dockerfile creates this config automatically:

```json
{
  "meta": {
    "lastTouchedVersion": "2026.2.15"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "meta-llama/llama-3.3-70b-instruct"
      },
      "workspace": "/home/node/.openclaw/workspace"
    }
  },
  "gateway": {
    "port": 7860,
    "mode": "cloud",
    "bind": "any",
    "auth": {
      "mode": "token",
      "token": "admin-token-123"
    }
  }
}
```

**Note**: API key comes from `OPENROUTER_API_KEY` environment variable, not the config file.

---

## 🧪 Test Locally

```bash
cd openclaw-hf

# Build
docker build -t openclaw-test .

# Run with your API key
docker run -p 7860:7860 \
  -e OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE \
  openclaw-test

# Access at http://localhost:7860
```

---

## ✅ Success Indicators

### Build Success:
- ✅ No errors during `npm install openclaw`
- ✅ `node-llama-cpp` builds successfully
- ✅ Config file created

### Runtime Success:
- ✅ Gateway starts on port 7860
- ✅ No "Missing config" errors
- ✅ Agent responds to messages
- ✅ Can send/receive chat messages

---

## 🐛 Common Issues

### Issue: "Missing config"
**Solution**: This is now fixed! Config is created automatically.

### Issue: "API key not found"
**Solution**: Make sure `OPENROUTER_API_KEY` is set as a **Secret** in HF Space settings.

### Issue: Build fails at npm install
**Solution**: Using `node:24-slim` (not Alpine) fixes this.

### Issue: SIGTERM error
**Solution**: Simplified CMD to just `["npx", "openclaw", "gateway"]` fixes this.

---

## 📚 Model Configuration

### Current Model:
- **Name**: `meta-llama/llama-3.3-70b-instruct`
- **Provider**: OpenRouter
- **Cost**: FREE tier (50 req/day)

### To Change Model:
Edit the Dockerfile config section:
```json
"model": {
  "primary": "your-model-name-here"
}
```

Popular free options:
- `meta-llama/llama-3.3-70b-instruct` (current)
- `meta-llama/llama-3.1-8b-instruct` (faster, smaller)
- `google/gemma-2-9b-it` (Google's model)

---

## 🎉 You're Ready!

This configuration has been tested and works. Just:

1. ✅ Get your free OpenRouter API key
2. ✅ Upload files to Hugging Face Space
3. ✅ Add `OPENROUTER_API_KEY` to Secrets
4. ✅ Wait for build
5. ✅ Test your agent!

**Total time**: ~15 minutes  
**Total cost**: $0.00  

---

**Last Updated**: 2026-02-17  
**Status**: ✅ WORKING  
**Dockerfile Version**: v3.0 (Simplified)

---
title: OpenClaw AI Agent (Llama 3.3 70B)
emoji: 🦞
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# OpenClaw AI Agent powered by Llama 3.3 70B

This is a hosted instance of the [OpenClaw](https://openclaw.ai) AI Agent, powered by **Meta's Llama 3.3 70B Instruct** via OpenRouter's free tier.

## 🤖 Llama 3.3 70B Features

- **🧠 Strong Reasoning**: Excellent logical and analytical capabilities
- **🔬 Biomedical Knowledge**: Well-suited for medical and scientific Q&A
- **📚 128K Context**: Large context window for complex queries
- **⚡ Fast**: 2-5 second response times
- **🆓 FREE**: Via OpenRouter's free tier (50 req/day)

## 🚀 Deployment Info

- **SDK**: Docker
- **Base Image**: Node 24 Alpine
- **Port**: 7860 (Hugging Face Default)
- **Model**: `meta-llama/llama-3.3-70b-instruct` via OpenRouter
- **Status**: Running

## 🔐 Security & Setup

This Space is running in a container. To use it:

1. **Access the web UI** via the **App** tab.

2. **Authentication**: If prompted for a token, use `admin-token-123` (default).

3. **⚠️ IMPORTANT - Add API Key**:
   - Go to **Settings** → **Variables and secrets**
   - Add a new **Secret**:
     - **Name**: `OPENROUTER_API_KEY`
     - **Value**: Your OpenRouter API key
     - Mark as "Secret" ✅
   
4. **Get FREE OpenRouter API Key**:
   - Visit: [https://openrouter.ai/keys](https://openrouter.ai/keys)
   - Sign up (no credit card needed!)
   - Create a new API key
   - Copy it (starts with `sk-or-v1-`)

## 📂 Project Structure

```
openclaw-hf/
├── Dockerfile              # Node 24 Alpine setup with OpenClaw
├── README.md              # This file
└── workspace/             # Agent configuration
    ├── AGENTS.md          # Agent behavior guidelines
    ├── SOUL.md            # Agent personality
    ├── IDENTITY.md        # Agent identity
    ├── TOOLS.md           # Available tools
    └── .openclaw/         # Workspace state
```

## 🎯 How It Works

1. **User sends message** → OpenClaw Gateway receives it
2. **Gateway processes** → Sends to OpenRouter API
3. **OpenRouter routes** → Meta Llama 3.3 70B processes
4. **Response generated** → Sent back through gateway
5. **User receives answer** → With citations and reasoning

## 💰 Pricing

### OpenRouter Free Tier
- ✅ 50 requests per day
- ✅ 20 requests per minute
- ✅ No credit card required
- ✅ $0.00 cost

### Upgrade Options (Optional)
If you need more requests:
- **Pay-as-you-go**: ~$0.50 per 1M input tokens
- **No monthly fees**: Only pay for what you use

## 🔧 Local Testing

Want to test locally before deploying?

```bash
# Build the Docker image
docker build -t openclaw-llama .

# Run with your OpenRouter API key
docker run -p 7860:7860 \
  -e OPENROUTER_API_KEY=sk-or-v1-YOUR_KEY_HERE \
  openclaw-llama

# Access at http://localhost:7860
```

## 🚀 Deployment Checklist

- [ ] Create Hugging Face Space (Docker SDK)
- [ ] Upload all files from `openclaw-hf/` folder
- [ ] Add `OPENROUTER_API_KEY` to Space Secrets
- [ ] Wait for build (~5-10 minutes)
- [ ] Test the agent via the App tab
- [ ] Share your Space URL! 🎉

## 📚 Documentation

For detailed setup instructions, see the main project documentation:
- `OPENROUTER_FREE_SETUP.md` - Complete setup guide
- `README_FREE_AI.md` - Quick start guide
- `FREE_GROQ_SETUP.md` - Alternative provider

## 🆘 Troubleshooting

### Issue: "API key not found"
**Solution**: Make sure you added `OPENROUTER_API_KEY` to Space Secrets (not Variables).

### Issue: "Rate limit exceeded"
**Solution**: Free tier allows 50 requests/day. Wait 24 hours or upgrade to paid tier.

### Issue: Build fails
**Solution**: 
- Check Node 24 is available
- Verify all workspace files are uploaded
- Check Hugging Face build logs

### Issue: Gateway won't start
**Solution**:
- Verify port 7860 is exposed
- Check environment variables are set
- Review container logs

## 🌟 Features

- **Conversational AI**: Natural dialogue with context retention
- **Biomedical Q&A**: Specialized for medical and scientific queries
- **Citation Support**: References sources with [1], [2], etc.
- **Multi-turn Conversations**: Maintains context across messages
- **Customizable**: Edit workspace files to change behavior

## 🤝 Contributing

Want to improve this agent?
1. Fork the repository
2. Modify workspace files (SOUL.md, AGENTS.md, etc.)
3. Test locally with Docker
4. Submit a pull request

## 📄 License

This project uses:
- **OpenClaw**: MIT License
- **Llama 3.3 70B**: Meta's Community License
- **OpenRouter**: Service terms apply

## 🙏 Acknowledgments

- [OpenClaw](https://openclaw.ai) - AI agent framework
- [Meta](https://llama.com) - Llama 3.3 70B model
- [OpenRouter](https://openrouter.ai) - API gateway
- [Hugging Face](https://huggingface.co) - Hosting platform

---

**Made with ❤️ using OpenRouter, Llama 3.3 70B, and OpenClaw**

*Need help? Check the documentation or open an issue!*

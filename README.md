<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:312E81,50:7C3AED,100:4F46E5&height=190&section=header&text=Yash%20Chaudhary&fontSize=44&fontColor=F8FAFC&animation=fadeIn&fontAlignY=36&desc=Indie%20Developer%20%E2%80%A2%20Native%20Apps%20%E2%80%A2%20AI%20Tools&descAlignY=58&descSize=17" alt="Yash Chaudhary — Indie developer building native apps and AI tools" />
</p>

<p align="center">
  <a href="https://yashchaudhary.dev/">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=3000&pause=900&color=A78BFA&center=true&vCenter=true&width=800&lines=Building+software+around+real+life;Native+macOS+%E2%80%A2+iOS+%E2%80%A2+Coding-agent+tooling;Local-first%2C+private+by+default" alt="Building software around real life" />
  </a>
</p>

<p align="center">
  <a href="https://yashchaudhary.dev/">
    <img src="https://img.shields.io/badge/Website-yashchaudhary.dev-6D28D9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" />
  </a>
  <a href="https://x.com/YashChaudhary">
    <img src="https://img.shields.io/badge/X-@YashChaudhary-111827?style=for-the-badge&logo=x&logoColor=white" alt="X / Twitter" />
  </a>
  <a href="https://www.linkedin.com/in/imychaudhary22/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-4F46E5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <img src="https://komarev.com/ghpvc/?username=imYashChaudhary973&label=Profile%20Views&color=7C3AED&style=for-the-badge" alt="Profile views" />
</p>

---

## About

I'm a student and indie developer from New Delhi, India. I learn by building things slightly beyond what I already know.

Most of what I make is native macOS and iOS software, plus tools for working with AI coding agents. I'm interested in software that understands context, respects privacy, and is useful in everyday life. That usually means local-first, explicit about what leaves the device, and honest in its docs about what is and isn't finished.

```yaml
principles:
  - local-first and private by default
  - native where it matters
  - humans stay in control of agents
  - evidence over claims
  - small, reviewable, reversible changes
```

---

## What I'm Building

| Product | What it is | Status |
|---|---|---|
| **[ZenVoice](https://getzenvoice.com/)** | Private dictation for Mac: press a shortcut, speak, and clean text lands in any app. Runs entirely on-device with no cloud, account, or subscription. | Live · [getzenvoice.com](https://getzenvoice.com/) |
| **[BuilderHelm](https://builderhelm.com/)** | *Your agents. You at the helm.* A local-first desktop environment for coordinating and reviewing work from multiple coding agents. | Coming soon |
| **[ClipHelm](https://github.com/imYashChaudhary973/ClipHelm)** | *AI finds the moments. You publish them.* A native macOS clip editor that turns long videos into ranked, captioned, reframed short clips. | In development |
| **Rove** | A native browser for people who build. | In development |

---

## Open Source

<details open>
<summary><strong>ClipHelm: AI video clipping for macOS</strong> · Swift</summary>

<br />

A native clip editor built on AVFoundation. It transcribes on-device with Apple's `SpeechAnalyzer` or through OpenRouter, finds and ranks moments by estimated viral chance, then reframes and burns in captions for 1080p/4K exports. API keys live only in the macOS Keychain, and only short audio chunks or bounded transcript excerpts are sent to models, never the original video.

[View repository →](https://github.com/imYashChaudhary973/ClipHelm)

</details>

<details>
<summary><strong>Codex Micro: an iPhone control pad for Codex</strong> · Swift · SwiftUI</summary>

<br />

An iPhone companion that controls Codex running on your Mac. It has glanceable agent keys, a reasoning dial, steer and interrupt controls, and push-to-talk. It pairs over the LAN using a QR code and a short authentication string, pins the Mac's TLS key, and receives only status updates scoped to the projects you grant. The Mac stays authoritative, and the phone never holds credentials or runs tools.

[View repository →](https://github.com/imYashChaudhary973/Codex-Micro-iOS)

</details>

<details>
<summary><strong>Agent City: a miniature internet for humans and agents</strong> · TypeScript · WebMCP</summary>

<br />

Built for the OpenAI WebMCP Challenge. Each website exposes typed tools through `document.modelContext`, so a browser agent and a human use the same app and share its state. An agent can plan an event across venue, catering, calendar, and budget districts and replan when constraints change. Every booking needs human approval. Runs on React 19 and a Cloudflare Worker.

[Live demo](https://agent-city.imyash-chaudhary2.workers.dev) · [View repository →](https://github.com/imYashChaudhary973/Agent-City)

</details>

<details>
<summary><strong>Goals Overlay: today's goals, always on screen</strong> · Swift · AppKit</summary>

<br />

A macOS menu bar app that pins your goals to a floating overlay on every Space, display, and fullscreen app without taking focus. It includes a `goals` CLI, natural-language deadlines (`ship eval fri`), automatic priority escalation, day rollover, and Obsidian sync. Storage is local JSON with no account, network access, or telemetry.

[View repository →](https://github.com/imYashChaudhary973/Goals-Overlay)

</details>

<details>
<summary><strong>Agent tooling: UI/UX Audit &amp; App Store Submission Auditor</strong> · JavaScript · Python</summary>

<br />

Two portable skills for AI coding agents:

- **[UI/UX Audit](https://github.com/imYashChaudhary973/ui-ux-audit)** pairs screenshots with direct DOM measurements to check contrast, target size, spacing, focus, motion, and overflow against WCAG 2.2.
- **[App Store Submission Auditor](https://github.com/imYashChaudhary973/app-store-submission-auditor)** is a read-only release-readiness audit covering metadata, privacy, SDK declarations, payments, signing, and TestFlight.

</details>

<details>
<summary><strong>More</strong></summary>

<br />

| Project | Description |
|---|---|
| [NotchDeck](https://github.com/imYashChaudhary973/NotchDeck) | A native macOS command center built around the MacBook notch (early development) |
| [SignalCheck](https://github.com/imYashChaudhary973/Early-Disease-Detection-System) | Educational early-symptom screening dashboard with explainable models trained on synthetic data |

</details>

---

## Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=swift,ts,js,python,java,kotlin,react,nextjs,nodejs,postgres,cloudflare,git,xcode,figma&theme=dark&perline=14" alt="Swift, TypeScript, JavaScript, Python, Java, Kotlin, React, Next.js, Node.js, PostgreSQL, Cloudflare, Git, Xcode, Figma" />
</p>

| Area | Tools |
|---|---|
| **Apple platforms** | Swift, SwiftUI, AppKit, SwiftData, AVFoundation, Xcode |
| **Web** | TypeScript, React, Next.js, Tailwind CSS, Cloudflare Workers |
| **Backend & data** | Node.js, Python, PostgreSQL, SQL |
| **AI & agents** | Codex, Claude Code, OpenRouter, WebMCP, on-device speech |
| **Workflow** | Git, GitHub, Figma, Obsidian |

---

## GitHub Analytics

<p align="center">
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=imYashChaudhary973&theme=tokyonight" alt="Yash Chaudhary's public GitHub statistics" />
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=imYashChaudhary973&theme=tokyonight" alt="Languages used across public repositories" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=imYashChaudhary973&theme=transparent&hide_border=true&ring=8B5CF6&fire=A78BFA&currStreakLabel=A78BFA&sideLabels=C9D1D9&dates=8B949E&currStreakNum=F8FAFC&sideNums=F8FAFC" alt="GitHub contribution streak" />
</p>

<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=imYashChaudhary973&bg_color=0D1117&color=C9D1D9&line=8B5CF6&point=A78BFA&area=true&area_color=4F46E5&hide_border=true" alt="GitHub contribution activity graph" />
</p>

---

## Right Now

```yaml
shipping:
  - ZenVoice: private, on-device dictation for Mac
building:
  - BuilderHelm: one place to run and review coding agents
  - ClipHelm: long videos in, publishable clips out
  - Rove: a native browser for builders
exploring:
  - agent interfaces humans can trust (WebMCP, approvals, scoped grants)
  - deterministic systems around probabilistic AI
```

---

<p align="center">
  <a href="https://yashchaudhary.dev/"><strong>yashchaudhary.dev</strong></a> ·
  <a href="https://x.com/YashChaudhary">X</a> ·
  <a href="https://www.linkedin.com/in/imychaudhary22/">LinkedIn</a> ·
  <a href="https://getzenvoice.com/">ZenVoice</a>
</p>

<p align="center">
  <em>Build systems that remain trustworthy when the demo is over.</em>
</p>

<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,50:7C3AED,100:312E81&height=120&section=footer" alt="Purple gradient footer" />
</p>

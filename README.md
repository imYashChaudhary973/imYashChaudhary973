<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:312E81,50:7C3AED,100:4F46E5&height=190&section=header&text=Yash%20Chaudhary&fontSize=44&fontColor=F8FAFC&animation=fadeIn&fontAlignY=36&desc=Indie%20Developer%20%E2%80%A2%20macOS%20%26%20iOS%20%E2%80%A2%20AI%20Developer%20Tooling&descAlignY=58&descSize=17" alt="Yash Chaudhary — Indie Developer, macOS and iOS, AI Developer Tooling" />
</p>

<p align="center">
  <a href="https://yashchaudhary.dev/">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=3000&pause=900&color=A78BFA&center=true&vCenter=true&width=800&lines=Building+software+around+real+life;Swift+%E2%80%A2+SwiftUI+%E2%80%A2+TypeScript+%E2%80%A2+Python;Local-first%2C+private+by+default;Your+agents.+You+at+the+helm." alt="Building software around real life" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/imYashChaudhary973">
    <img src="https://img.shields.io/badge/GitHub-imYashChaudhary973-6D28D9?style=for-the-badge&logo=github&logoColor=white" alt="GitHub profile" />
  </a>
  <a href="https://yashchaudhary.dev/">
    <img src="https://img.shields.io/badge/Website-yashchaudhary.dev-7C3AED?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" />
  </a>
  <a href="https://x.com/builderhelmai">
    <img src="https://img.shields.io/badge/X-@builderhelmai-111827?style=for-the-badge&logo=x&logoColor=white" alt="X @builderhelmai" />
  </a>
  <img src="https://komarev.com/ghpvc/?username=imYashChaudhary973&label=Profile%20Views&color=7C3AED&style=for-the-badge" alt="Profile views" />
  <a href="https://github.com/imYashChaudhary973?tab=followers">
    <img src="https://img.shields.io/github/followers/imYashChaudhary973?style=for-the-badge&logo=github&label=Followers&color=4F46E5" alt="GitHub followers" />
  </a>
</p>

---

## About

I am a student and indie developer from New Delhi, India, building native macOS and iOS products and tooling for AI coding agents. My current work spans on-device voice dictation, a desktop environment for coordinating coding agents, AI-assisted video clipping, phone-to-Mac agent control, agent-native web interfaces, and release and UI quality audits.

I care about software that understands context, respects privacy, and stays useful in everyday life: local-first data, explicit boundaries around what leaves the device, humans in control of agents, focused tests, and documentation that tells the truth about what is—and is not—ready.

```yaml
engineering_values:
  - product thinking before implementation
  - local-first and private by default
  - humans stay at the helm of their agents
  - evidence-backed quality gates
  - small, reviewable, reversible changes
```

---

## Technical Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=swift,ts,js,python,java,kotlin,react,nextjs,nodejs,postgres,cloudflare,tailwind,git,github,figma,apple&theme=dark&perline=8" alt="Swift, TypeScript, JavaScript, Python, Java, Kotlin, React, Next.js, Node.js, PostgreSQL, Cloudflare, Tailwind CSS, Git, GitHub, Figma, and Apple platform skills" />
</p>

| Area | Technologies and practices |
|---|---|
| **Apple platforms** | Swift 6, SwiftUI, AppKit, SwiftData, AVFoundation, Speech, Keychain, Xcode, Swift Package Manager |
| **Web and edge** | TypeScript, React, Next.js, Vite, Tailwind CSS, Cloudflare Workers |
| **Backend and data** | Node.js, Python, PostgreSQL, SQL, local JSON and versioned persistence |
| **AI and agents** | Codex, Claude Code, OpenRouter, WebMCP, on-device speech recognition, agent skills |
| **Quality engineering** | Unit and integration testing, threat models, release checklists, UI/UX measurement |
| **Delivery** | Git, GitHub, pull-request workflows, technical documentation, Figma |

---

## Engineering Focus

| Domain | Focus | Evidence in current work |
|---|---|---|
| **Native macOS products** | Fast, private, native desktop software | ZenVoice on-device dictation, ClipHelm clip editor, Goals Overlay, NotchDeck, Rove |
| **AI coding-agent tooling** | Humans coordinating and supervising agents | BuilderHelm agent environment, Codex Micro iPhone control pad, reusable agent audit skills |
| **Agent-native interfaces** | Typed, discoverable tools instead of screen-scraping | Agent City WebMCP tool surface with human approval on every write |
| **Privacy and security** | Data stays local unless the user decides otherwise | On-device transcription, Keychain-only secrets, pinned-TLS LAN pairing, scoped grants |
| **Release assurance and UI quality** | Measured issues and traceable evidence | App Store policy audits, WCAG 2.2 browser measurements, release gates and checklists |

---

## Featured Engineering Work

<details open>
<summary><strong>ZenVoice — Private, local-first voice dictation for Mac</strong></summary>

<br />

ZenVoice is a native macOS dictation app: press a shortcut, speak, and clean text lands in any app. Transcription runs entirely on the Mac, with no cloud, no account, and no subscription.

| | |
|---|---|
| **Stack** | Swift, native macOS |
| **Privacy** | Fully on-device transcription; no cloud processing or account required |
| **Business model** | Pay once, with a 14-day free trial |
| **Status** | Live and shipping |
| **Website** | [getzenvoice.com](https://getzenvoice.com/) |

</details>

<details>
<summary><strong>BuilderHelm — Your agents. You at the helm.</strong></summary>

<br />

BuilderHelm is a local-first desktop environment for macOS for running, coordinating, and reviewing work from multiple coding agents, so the developer stays in charge of what ships.

| | |
|---|---|
| **Stack** | TypeScript, desktop app for macOS |
| **Approach** | Local-first harness; agents do the work, humans review and decide |
| **Status** | Paid product · coming soon |
| **Website** | [builderhelm.com](https://builderhelm.com/) |

</details>

<details>
<summary><strong>ClipHelm — AI finds the moments. You publish them.</strong></summary>

<br />

A native macOS clip editor that turns long videos into short, captioned, reframed clips. It transcribes on the Mac with Apple's `SpeechAnalyzer` or through OpenRouter, finds and ranks moments by estimated viral chance, then renders 1080p or 4K exports with burned-in captions.

| | |
|---|---|
| **Stack** | Swift 6, SwiftUI, AVFoundation, Speech, OpenRouter |
| **Pipeline** | Download → transcription → scene analysis → moment finding → framing → rendering |
| **Privacy** | API key kept only in the macOS Keychain; only short audio chunks or bounded excerpts reach models, never the original video |
| **Reliability** | Tests cover media mapping, transcription, moment discovery, edit planning, mocked AI calls, and a network-free full processing run |
| **Repository** | [View source](https://github.com/imYashChaudhary973/ClipHelm) · in development |

</details>

<details>
<summary><strong>Codex Micro — An iPhone control pad for Codex on your Mac</strong></summary>

<br />

An iPhone companion that controls Codex running on a Mac: glanceable agent keys, command keys, a reasoning dial, joystick workflows, and push-to-talk. The Mac stays the authoritative host; the phone never holds the OpenAI credential and never runs tools itself.

| | |
|---|---|
| **Stack** | Swift, SwiftUI, WebSocket (WSS), Codex app-server |
| **Security** | LAN pairing with QR + short authentication string, pinned Mac TLS key, sealed sessions |
| **Access control** | Status-only projections scoped by Mac-side project grants; approvals opt-in |
| **Documentation** | Threat model, transport ADR, architecture, roadmap, and phase acceptance history |
| **Repository** | [View source](https://github.com/imYashChaudhary973/Codex-Micro-iOS) · physical parity acceptance in progress |

</details>

<details>
<summary><strong>Agent City — A miniature internet for humans and AI agents</strong></summary>

<br />

Built for the OpenAI WebMCP Challenge. Websites expose structured capabilities through WebMCP (`document.modelContext`), so humans use the visual UI while agents use typed, discoverable tools, and both share the same state. An agent can plan an event across venue, catering, calendar, and budget districts and replan when constraints change.

| | |
|---|---|
| **Stack** | React 19, TypeScript, Vite, Tailwind CSS, Cloudflare Workers |
| **Agent surface** | Read tools annotated read-only; booking and cancellation tools require human approval |
| **Data** | Deterministic datasets whose dates roll with today, so the demo always works |
| **Repository** | [View source](https://github.com/imYashChaudhary973/Agent-City) · [Live demo](https://agent-city.imyash-chaudhary2.workers.dev) · MIT |

</details>

<details>
<summary><strong>Goals Overlay — Today's goals, always on screen</strong></summary>

<br />

A macOS menu bar app that pins today's goals to a floating, always-on-top overlay across every Space, display, and fullscreen app, plus a `goals` CLI for managing tasks without leaving the terminal.

| | |
|---|---|
| **Stack** | Swift 6, SwiftUI, AppKit (`NSPanel`), Swift Package Manager |
| **Features** | Natural-language deadlines, auto-escalating priority, day rollover, focus pin, Obsidian sync |
| **Privacy** | Local JSON storage; no account, no network, no telemetry |
| **Repository** | [View source](https://github.com/imYashChaudhary973/Goals-Overlay) |

</details>

<details>
<summary><strong>App Store Submission Auditor — Release-readiness tooling</strong></summary>

<br />

A reusable audit skill and static scanner for identifying App Store submission risks before review. It covers product completeness, metadata, privacy, SDK declarations, login, account deletion, payments, signing, capabilities, sensitive domains, TestFlight readiness, and evidence preparation.

| | |
|---|---|
| **Stack** | Python, JavaScript, TypeScript, Bash, YAML |
| **Delivery** | Agent skill, CLI package, checklists, prompts, report templates, policy source index |
| **Safety** | Read-only by default; findings are evidence-linked and severity-ranked |
| **Repository** | [View source](https://github.com/imYashChaudhary973/app-store-submission-auditor) · MIT |

</details>

<details>
<summary><strong>UI/UX Audit — Measured interface quality for AI coding agents</strong></summary>

<br />

A portable browser audit workflow that combines screenshots with direct DOM measurements. It evaluates desktop and mobile experiences for contrast, target size, spacing, alignment, animation performance, focus visibility, reduced-motion support, horizontal overflow, and visual-system consistency.

| | |
|---|---|
| **Stack** | JavaScript, browser automation, Chromium measurement APIs |
| **Standards** | WCAG 2.2, web performance guidance, platform design principles |
| **Output** | Prioritized blocker/major/minor findings with locations, measured evidence, and concrete fixes |
| **Repository** | [View source](https://github.com/imYashChaudhary973/ui-ux-audit) · MIT |

</details>

<details>
<summary><strong>More projects</strong></summary>

<br />

| Project | Description |
|---|---|
| **Rove** | A native browser for people who build · in development |
| [NotchDeck](https://github.com/imYashChaudhary973/NotchDeck) | A native macOS command center built around the MacBook notch · early development |
| [SignalCheck](https://github.com/imYashChaudhary973/Early-Disease-Detection-System) | Educational early-symptom screening dashboard with explainable models trained on synthetic data |

</details>

---

## Selected Outcomes

| Engineering outcome | Details |
|---|---|
| **Shipped a paid on-device product** | Launched ZenVoice, a private macOS dictation app with its own website, checkout, and licensing |
| **Secure phone-to-Mac agent control** | Built LAN pairing with QR and short authentication string, pinned TLS, and grant-scoped access, backed by a written threat model |
| **Agent-native web experiment** | Designed a WebMCP tool surface where every booking-style action requires human approval |
| **Private AI video pipeline** | Built an end-to-end clipping pipeline with on-device transcription, Keychain-only secrets, and a network-free test run |
| **Reusable quality audits** | Published App Store readiness and UI/UX audit skills that connect findings to measured evidence |

---

## GitHub Analytics

<p align="center">
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=imYashChaudhary973&theme=tokyonight" alt="Yash Chaudhary's public GitHub statistics" />
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=imYashChaudhary973&theme=tokyonight" alt="Languages used across public repositories" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=imYashChaudhary973&theme=transparent&hide_border=true&ring=8B5CF6&fire=A78BFA&currStreakLabel=A78BFA&sideLabels=C9D1D9&dates=8B949E&currStreakNum=F8FAFC&sideNums=F8FAFC" alt="GitHub contribution streak" />
</p>

---

## Contribution Activity

<p align="center">
  <img width="100%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=imYashChaudhary973&theme=tokyonight" alt="GitHub contribution activity graph" />
</p>

---

## Current Focus

```yaml
shipping:
  - ZenVoice, private on-device dictation for Mac

building:
  - BuilderHelm, a local-first environment for coding agents
  - ClipHelm, AI video clipping for macOS
  - Rove, a native browser for people who build

learning:
  - deeper Swift concurrency and media pipelines
  - reliable agent workflows and evaluation

exploring:
  - agent interfaces humans can trust (WebMCP, approvals, scoped grants)
  - deterministic systems around probabilistic AI
```

---

## Connect

<p align="center">
  <a href="https://yashchaudhary.dev/">
    <img src="https://img.shields.io/badge/Website-yashchaudhary.dev-6D28D9?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" />
  </a>
  <a href="https://x.com/builderhelmai">
    <img src="https://img.shields.io/badge/X-@builderhelmai-111827?style=for-the-badge&logo=x&logoColor=white" alt="X @builderhelmai" />
  </a>
  <a href="https://www.linkedin.com/in/imychaudhary22/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/imYashChaudhary973">
    <img src="https://img.shields.io/badge/GitHub-Follow%20the%20work-6D28D9?style=for-the-badge&logo=github&logoColor=white" alt="Follow Yash Chaudhary on GitHub" />
  </a>
</p>

<p align="center">
  <em>Build systems that remain trustworthy when the demo is over.</em>
</p>

<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,50:7C3AED,100:312E81&height=120&section=footer" alt="Purple gradient footer" />
</p>

# jibun-de-mamoru （自分で守る）

English | [日本語](README.ja.md)

A one-page, client-side companion for people who just received a personal-data
leak notification in Japan — and for anyone who wants to prepare before one
arrives.

**Live page:** https://sunnydachs.github.io/jibun-de-mamoru/

## What it is

After Japan's Digital Minister told citizens to "protect your own
information" (Oct 6, 2026), the public reaction was: *companies leak, so what
can an individual actually do?* This page is our answer, in two parts:

1. **「自分で守る」実行チェック** — the government's three measures (stop
   password reuse, enable MFA, don't tap suspicious links) plus AI-service
   settings, each reduced to something that works if you do exactly ONE of
   them. Every item links a public authority as its source.
2. **漏えい通知の台帳 (leak-notification ledger)** — the part no existing free
   tool has: record each notification (who, when, what leaked) and the page
   turns it into dated next actions (today / this week / ~30 days), kept
   across multiple notifications. Copy the whole ledger out as text anytime.

## Why "stateful" matters

The free checkers and guides that already exist (Have I Been Pwned-style
lookups, static "what to do by leak type" pages) are stateless: they tell you
generic advice and forget you. Nothing free keeps *your* record — which
services you already changed, which deadlines (card chargeback windows,
credit-bureau 本人申告, license reissue) are still open, what your second and
third notifications added. This page keeps exactly that, and nothing else.

## Privacy & limits (stated on the page itself)

- Everything runs and stays **on your device** (localStorage). Nothing is
  sent anywhere; clearing browser data or changing devices erases the record.
- **Not a guarantee of anything.** Corporate breaches cannot be prevented by
  individuals. The steps are general guidance from public authorities
  (NPA, PPC, National Consumer Affairs Center) and official service pages —
  not legal or technical advice for your specific situation.
- Procedures age: official pages change, and Japan's 2027 payment-services
  amendments (犯収法) will move some of this. Check the linked sources.
- Real damage: Japan's cybercrime consultation window; consumer trouble: 188.

## Languages

The page opens in the visitor's language (auto-detected: Japanese for
ja browsers, English otherwise — dev.to readers land in English), with a
toggle in the top bar; the choice persists on the device. The cited
authority pages are Japanese.

## Repository layout

Single-file static site: `index.html` (no build step, no dependencies, no
tracking). Deployed via GitHub Pages.

## Sources

Each checklist item and each generated task cites a public authority or the
relevant official page inline (NPA, PPC, フィッシング対策協議会, JICC, etc.).

## License

MIT — see [LICENSE](LICENSE). 日本語のREADMEは[こちら](README.ja.md)。

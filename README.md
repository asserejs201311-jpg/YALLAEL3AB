<p align="center">
  <img src="./logo.svg" alt="YallaEl3ab" width="380">
</p>

<h1 align="center">YallaEl3ab ⚽ — Book your pitch · احجز ملعبك</h1>

A mobile-first web app for booking football pitches in Egypt (Cairo, Giza, Tanta/Gharbia, and more).
It runs as a **single self-contained HTML file** — no build step, no server. All data is stored
locally in the browser, so it works offline and you can host it anywhere static.

> Live file: **`app.html`** (the root `index.html` just redirects to it so GitHub Pages works at the
> repository root). The app opens in **Arabic by default** (full RTL) and can switch to English from the
> login screen or Settings.

## Features

- **Players:** browse & search pitches, filter by size (5/7/11-a-side), live map, full booking flow,
  favorites, and ⭐ 1–5 star reviews with comments.
- **Owners:** list up to 2 pitches (with a real photo), manage reservations, see earnings, confirm
  InstaPay payments, and report a pitch "taken by someone unknown."
- **AI assistant:** natural-language pitch finder. Open it from the floating button **or by swiping
  left** anywhere in the app. Works offline with a built-in matcher, or a real Claude model if you
  paste an Anthropic API key (stored only on your device).
- **Payments:** InstaPay-only. Players copy the owner's account; subscriptions are paid to a fixed
  InstaPay number. Card logos (Visa/Mastercard/Apple Pay) are shown locked. The app holds no money.
- **Membership:** 2-week free trial or 50 EGP/month. Paying grants provisional access immediately, but
  every payment must still be **approved by the admin (yes/no)**. A daily check notifies you when the
  trial is ending and the day it expires.
- **Double-sided verification:** owner confirms payment → a unique 6-digit entry code is issued →
  player acknowledges a pre-flight summary → owner/guard verifies the code at the gate (`checked_in`).
  Realtime sync across browser tabs.
- **Bilingual (Arabic default + English)**, **light / dark mode**, **per-booking chat**, emoji avatars
  with a colour picker, a **sliding-pill bottom nav**, a secret 10-tap admin portal, and full
  **backup / restore** of all data.
- Pitches persist across logout and auto-delete after 30 days of owner inactivity.

## Run locally

Just open `app.html` in any modern browser. That's it.
(Optional: serve the folder with any static server, e.g. `python -m http.server`, then visit `/`.)

## Deploy to GitHub Pages

1. Create a new GitHub repo and push these files.
2. In **Settings → Pages**, set **Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Your app will be live at `https://<user>.github.io/<repo>/` (the root `index.html` redirects to the app).

## Repository structure

```
.
├── app.html        # the entire app (HTML + CSS + JS in one file)
├── index.html      # redirect to app.html (for GitHub Pages root)
├── logo.svg        # brand logo
├── README.md
├── LICENSE         # MIT
├── .gitignore      # excludes scratch dev files (_*.png, _*.js, _*.html, transform.py)
└── yalla-app/      # optional production backend (React + TS + Supabase + Claude edge function)
```

## Admin & demo notes

- **Admin portal:** tap the app logo **10 times within 5 seconds** → blank password sheet.
  Passcode: `AsMa@2013F`. Only 2 admin "seats" can ever be used (clear site storage to reset).
  Note: this guards local state only and is visible in the page source — it is not real security.
- **Subscription InstaPay number:** `+20 127 418 8441`.
- Data lives in `localStorage` (keys prefixed `ye_`). Clear it to reset the app to a fresh state.
- The AI assistant calls Anthropic directly from the browser using the key you paste under **AI key**;
  without a key it falls back to the local matcher.

## Optional: production backend

The single-file app stores data per browser (no cross-device accounts). For a real multi-user launch,
the `yalla-app/` folder contains a separate, backend-ready React + TypeScript version (Supabase +
TanStack Query + a Claude Edge Function) implementing the same features against a real database.
See `yalla-app/README.md`.

## Tech

Vanilla HTML/CSS/JS, inline SVG icons, CSS animations, `localStorage` persistence, cross-tab sync via
the `storage` event. No dependencies.

## License

MIT — see [LICENSE](LICENSE).

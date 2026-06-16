# YallaEl3ab ⚽ — Book your pitch

A mobile-first web app for booking football pitches in Egypt (Cairo, Giza, Tanta/Gharbia and more).
It runs as a **single self-contained HTML file** — no build step, no server required. All data is
stored locally in the browser, so it works offline and you can host it anywhere static.

> Live file: **`app.html`** (the `index.html` here just redirects to it so GitHub Pages
> works at the repository root).

## Features

- **Players:** browse & search pitches, filter by size (5/7/11-a-side), live map, booking flow.
- **Owners:** list up to 2 pitches (with a real photo upload), manage reservations, see earnings,
  confirm InstaPay payments, read ⭐ reviews, and report a pitch "taken by someone unknown".
- **AI assistant:** natural-language pitch finder. Works with a built-in matcher offline, or a real
  Claude model if you paste an Anthropic API key (stored only on your device).
- **Payments:** InstaPay-only. Players copy the owner's account; subscriptions are paid to a fixed
  InstaPay number. Card logos (Visa/Mastercard/Apple Pay) are shown locked.
- **Membership:** 2-week free trial or 50 EGP/month. Paying grants provisional access immediately,
  but every payment must still be **approved by the admin (yes/no)** — declined payments are revoked.
- **Double-sided verification:** owner confirms payment → a unique 6-digit entry code is issued →
  player reviews a pre-flight summary and acknowledges → owner/guard verifies the code at the gate
  (`checked_in`). Realtime sync across browser tabs.
- **Per-booking chat**, **1–5 star reviews + comments**, **secret 10-tap admin portal**,
  **light / dark mode** toggle, and a **responsive** layout (phone → foldable → tablet → laptop).
- Pitches persist across logout and auto-delete after 30 days of owner inactivity.

## Run locally

Just open `app.html` in any modern browser. That's it.
(Optional: serve the folder with any static server, e.g. `python -m http.server`, then visit `/`.)

## Deploy to GitHub Pages

1. Create a new GitHub repo and push these files.
2. In **Settings → Pages**, set **Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
3. Your app will be live at `https://<user>.github.io/<repo>/` (the root `index.html` redirects to the app).

## Admin & demo notes

- **Admin portal:** tap the app logo **10 times within 5 seconds** → blank password sheet.
  Passcode: `AsMa@2013F`. Only 2 admin "seats" can ever be used (clear site storage to reset).
- **Subscription InstaPay number:** `+20 127 418 8441`.
- Data lives in `localStorage` (keys prefixed `ye_`). Clear it to reset the app to a fresh state.
- The AI assistant calls Anthropic directly from the browser using the key you paste under
  **AI key** on the home search bar; without a key it falls back to the local matcher.

## Optional: production backend

The `yalla-app/` folder contains a separate, backend-ready React + TypeScript version (Supabase +
TanStack Query + a Claude Edge Function) implementing the same features against a real database.
See `yalla-app/README.md`.

## Tech

Vanilla HTML/CSS/JS, inline SVG icons, CSS animations, `localStorage` persistence, cross-tab sync
via the `storage` event. No dependencies.

## License

MIT — see [LICENSE](LICENSE).

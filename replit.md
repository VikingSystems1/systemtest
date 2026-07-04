# Viking Valet Waste — Landing Page

A single-page static landing site for Viking Valet Waste, a luxury doorstep trash pickup service.

## Stack
- Pure HTML/CSS with Tailwind CSS (via CDN)
- No build step required — edit `index.html` directly

## Running
```
python3 -m http.server 5000
```
Served via the **Start application** workflow on port 5000.

## Structure
- `index.html` — the entire site (hero, nav, sections, FAQ)
- `CNAME` — custom domain: vikingvaletwaste.com

## Notes
- The contact form (`handleFormSubmit`) is frontend-only — it shows a success message but does not submit to any backend
- External CDN dependencies (Tailwind, FontAwesome, Google Fonts) require internet access at runtime

## User preferences
- Wants to swap in custom artwork/images
- Plans to incorporate scraped data from competitor/reference sites

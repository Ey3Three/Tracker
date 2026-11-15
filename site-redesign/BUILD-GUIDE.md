# Eye Three — Squarespace build guide

This maps each section of the prototype to the sections and blocks in the Squarespace 7.1 editor. Open the prototype page beside the editor and work top to bottom.

- Prototype files: `index.html`, `private.html`, `i3yogaintensive.html`, `free.html`
- Optional CSS: `squarespace-custom.css`
- Dashed orange boxes in the prototype are text you still need to write. Don't build those blocks until the words exist, or leave them out.

**Nothing in this guide deletes a live page.** Build each page as a duplicate first (Pages panel, hover the page, gear icon, Duplicate), check it, then swap it in.

---

## 0. Before you start

### What your plan covers

| Piece | Plan needed |
|---|---|
| Every section, block and Site Style in this guide | Personal |
| Newsletter block and Form block | Personal |
| Scheduling block | Personal, plus a separate Acuity Scheduling subscription |
| Custom CSS panel (`squarespace-custom.css`) | Listed by Squarespace as available on all plans. Check that Website > Pages > Custom Code > Custom CSS opens for you |
| Code Injection, JavaScript, iframes in Code blocks | Core, Plus, Advanced, or legacy Business/Commerce. This guide uses none of them |

Your Notion page "Privates plan: 2 Plateaued clients by February" already lists the Acuity tiers ($16 a month Starter, $27 a month Standard for the four-session package). Confirm those prices in Squarespace before you subscribe; I could not verify them.

### Site Styles (one-time, site-wide)

Open any page in Edit mode, then the paintbrush icon.

**Fonts.** Your site already uses both fonts, so this is mostly sizes.

| Style | Font | Size in the prototype |
|---|---|---|
| Heading 1 | Instrument Serif | about 4.75rem desktop, tight line height (1.0) |
| Heading 2 | Instrument Serif | about 3.25rem |
| Heading 3 | Instrument Serif | about 2rem |
| Paragraph 1 (large) | Newsreader, weight 300 | about 1.55rem |
| Paragraph 2 (body) | Newsreader, weight 400 | about 1.2rem, line height 1.6 |
| Buttons | Newsreader, weight 500, uppercase, letter spacing 0.14em | about 0.95rem |
| Site navigation | Newsreader, weight 500, uppercase, letter spacing 0.14em | about 0.9rem |

**Colors.** Edit the palette to five colors:

| Slot | Color | Used for |
|---|---|---|
| White | `#FFFFFF` | Main backgrounds |
| Light | `#F4F1EA` | Cream alternating sections |
| Accent | `#C9A45C` | Buttons and the short line under headings |
| Dark | `#1A1A1A` | Body text |
| Black | `#0B0B0B` | Header, hero, final section, footer |

The accent is my choice, not something from your current site, which is black and white only. Change that one swatch and every button and line follows.

Then set the section themes you will use: **White**, **Light 1** (cream background, dark text), **Black Bold** (black background, white text, accent buttons). Your pages already use White and Black Bold.

**Buttons.** Primary: filled with the accent, black text, square corners (radius 0), padding roughly 1em tall by 1.9em wide.

**Forms.** Field shape Square (yours is Pill today), outline style, no fill.

**Header.** Edit Site Header: black theme, logo left, navigation right, Fixed position: Basic. Remove the social icons from the header (they move to the footer). Turn off the cart icon if it shows.

**Navigation.** The prototype adds one link, "Privates", between Practice and Events. That label is a placeholder; name it what you like. "Home" is dropped because the logo links home. Both are suggestions, not requirements.

**Footer.** One black section: a Text block with "Eye.Three LLC" on the left and a Social Links block on the right.

### The repeating pattern

Every section uses the same three moves, which is what gives the pacing:

1. Heading (Text block).
2. A short accent line: **Line block**, width about 72px, thickness 3px, accent color.
3. Text, then at most one button.

Section padding: set Section Height to **Medium** for content sections and **Large** for the hero. Alternate White and Light 1 so neighbouring sections never share a background.

---

## 1. Homepage (`index.html` → `/`)

| # | Prototype section | Squarespace section | Blocks and settings |
|---|---|---|---|
| 1 | Hero with street photo | Your existing first section. Format: Height Large, Fill screen off. Background: image `DSC_5590B.jpg`, Overlay on at about 45%. Colors: Black Bold. Content alignment: bottom | Text block (H1 "I3 Yoga System", H2 "Move well. Move far. Be strong there.", Paragraph 1 for the paragraph), Line block, Button block "Learn more" → `/system`. Place all of them in the left 7 columns of the grid, lower third, so the face stays clear |
| 2 | Slim newsletter band | New blank section. Height Small. Colors: Black Bold | Text block (H3 "Sign-up here to join my newsletter!") in the left 5 columns. **Newsletter block** in the right 7 columns: Layout Float (field and button on one row), name field off, title and description hidden |
| 3 | Strength Through Asana | Blank section. Height Medium. Colors: White | Image block `DSCN3177.JPG` in columns 1–6, crop 4:5. Text block (H2), Line block, Text block (Paragraph 1) in columns 8–12, vertically centred |
| 4 | Who it's for ? | Blank section. Height Medium. Colors: Light 1 | Mirror of section 3: text in columns 1–5, Image block `DSCN3272.JPG` in columns 7–12, crop 3:2 |
| 5 | Three cards | Blank section. Height Medium. Colors: White | Three **Shape blocks** (rectangle, 4 columns each): outer two black, middle one white with a thin border. Layer on each: a Text block (small caps line, H3, paragraph), a Line block, a Button block. Buttons: "[ Details ]" → `/i3yogaintensive`, "Inquire about privates" → `/private`, "GLO" → your Glo link. An optional heading above is a gap |
| 6 | Final step: newsletter | Blank section. Height Medium. Colors: Black Bold | Left 5 columns: Text block (H2 "Subscribe to my newsletter for insight and daily updates!"), Line block, and a gap for one or two sentences. Right 6 columns: Newsletter block, Layout Stack, name field on |

Notes:

- The words in the three cards come from `/events` and `/train`. Nothing new was written.
- "Sign Up" on the newsletter buttons is Squarespace's default label. I could not read your current form's button label, so keep whatever yours says.
- Your current homepage has a Form block here ("New Form"), not a Newsletter block. Either works on Personal. Keep the Form block if it is already wired to your list; the Newsletter block is tidier on one row. Check Storage on whichever you use so sign-ups keep going where they go today.
- On phones, drag the blocks in mobile view so each section reads image, heading, line, text, button.

**Ends in:** join the newsletter.

---

## 2. Private sessions (`private.html` → `/private`)

This page does not exist yet. Pages panel, +, Blank page, then the gear icon: Page Title "Private Sessions", URL Slug `private`. Put it in Main Navigation.

| # | Prototype section | Squarespace section | Blocks and settings |
|---|---|---|---|
| 1 | Hero with street photo | Blank section. Height Large. Background: image `DSC_5547.jpg`, Overlay about 50%. Colors: Black Bold | Left 6 columns: Text block (H1 "1:1 Session (Zoom)"), a one-line gap, Line block, Button block linking to the booking section (see note). Button label is a gap |
| 2 | Intro | Blank section. Height Small. Colors: White. Content width Narrow | Text block, Paragraph 1, centred. All of it is a gap |
| 3 | Prices | Blank section. Height Medium. Colors: Light 1 | Two Shape blocks side by side (5 columns each, centred): left white, right black. On the left: Text block (H3 "Single session", H1 "$125"). On the right: Text block (H3 "Monthly", H1 "$100", "per session", then "four-session minimum ($400/month)"). Line block and Button block on each. Below both, a centred Text block: "* Inquire about 75/90 minute sessions" |
| 4 | Final step: book | Blank section. Height Medium. Colors: White | Text block (H2, a gap), then the **Scheduling block** spanning 8–10 columns, centred |

### The Scheduling block

1. Start Acuity first: Settings (or the Scheduling panel in the left menu) → Scheduling → start the trial. Your Notion plan has the steps: connect Stripe, create the appointment types, add the intake form.
2. Create only what this page sells right now: a single private at $125 and the four-session option at $400. Your Notion plan also lists a free practice review; add it later as a third appointment type and it will appear in the block without touching the page.
3. On the page: click + in section 4 → **Scheduling** (under Advanced or by search). In the block's settings choose what to show: all appointment types, one category, or a single type. Choose the category that holds the two privates.
4. Resize the block to at least 8 columns wide and let its height grow; the calendar needs room. Check it on a phone.
5. Publish and book a test appointment yourself to confirm payment and the confirmation email.

Notes:

- **Buttons that jump to the calendar.** Squarespace has no built-in "scroll to section" setting. Two options: (a) leave the hero and price buttons out, since the calendar is two short sections below, or (b) add a Code block above the Scheduling block containing `<div id="book"></div>` and link the buttons to `#book`. Option (b) is plain HTML, which Personal is reported to allow in Code blocks, but sources disagree. If the block shows a "premium feature" notice, use option (a).
- The 75/90 minute line can come off the page later if you add those lengths as appointment types.
- Once the calendar is live, the "Inquire about privates" form on `/train` duplicates it. Say the word and I'll note how to point that section here; I have not touched it.

**Ends in:** book a private.

---

## 3. Intensive (`i3yogaintensive.html` → `/i3yogaintensive`)

Duplicate the existing page and rearrange; every word is already there.

| # | Prototype section | Squarespace section | Blocks and settings |
|---|---|---|---|
| 1 | Hero | Existing first section. Height Large. Background: image `01-studio-exterior-autumn.jpg`, Overlay about 45%. Colors: Black Bold | Right 6 columns, right-aligned: Text block (H1 "i3 Practice Intensive · Groundworks", H2 "March 25 to 28, 2027", H2 "Groundworks, Hudson Valley"), Line block, Button block "Register Here!" → your Google Form, open in new tab |
| 2 | Intro | Blank section. Height Medium. Colors: White | Image block `02-shawangunk-ridge-view.jpg` in columns 1–6, crop 3:2. Columns 8–12: Text block (Paragraph 1 "Thirty five acres…"), Line block, Text block ("Everything a teacher training gives you…") |
| 3 | Over three days, you will: | Blank section. Height Medium. Colors: Light 1. Content width Narrow | Text block (H2), Line block, then five rows. Each row: a Text block with the number as H3 in accent color ("01"…"05") in 1 column, a Text block with the sentence in the rest, and a Line block (full width, 1px, grey) between rows. The "→" arrows are replaced by the numbers |
| 4 | The place | Blank section. Height Medium. Colors: White | Columns 1–5: Text block (Paragraph 1 "There is also a wood-fired sauna…"). Columns 7–12: Image block `07-main-house-exterior.jpg`, crop 3:2 |
| 5 | Price and rooms | Blank section. Height Small. Colors: Light 1 | A gap. See note |
| 6 | Final step: register | Blank section. Height Medium. Colors: Black Bold. Centred | Text block (H2 "March 25 to 28, 2027", H3 "Groundworks, Hudson Valley"), Line block, Button block "Register Here!" → Google Form |

Notes:

- **Price is missing from the page.** Your search description says "Fifteen practitioners… All meals, lodging, and program included… $1,000 to $1,600 by room", but the page body never states a price. Section 5 is where it would go.
- The page currently carries `07-main-house-exterior.jpg` twice. The prototype uses it once. Nothing is removed until you choose to.
- A simpler way to build section 3: one Text block with a numbered list. It loses the large accent numbers but takes two minutes.

**Ends in:** register for the intensive.

---

## 4. Free (`free.html` → `/free`)

This page does not exist yet and returns a 404 today. Pages panel, scroll to **Not Linked**, +, Blank page, URL Slug `free`. Keeping it in Not Linked leaves it out of the navigation but reachable by link, which suits a page you send people to from Instagram.

Almost everything here is a gap, because the resource is not ready. Build the skeleton now or wait.

| # | Prototype section | Squarespace section | Blocks and settings |
|---|---|---|---|
| 1 | Title and sign-up | Blank section. Height Large. Colors: Black Bold | Left 6 columns: Text block (H1, gap), Line block, Text block (gap). Right 5 columns: Shape block (transparent, thin white border) with a **Newsletter block** on top: Layout Stack, name field on. Button label and the disclaimer line are gaps |
| 2 | What's inside | Blank section. Height Medium. Colors: White. Content width Narrow | Same numbered-row pattern as the intensive, section 3. Heading and all rows are gaps |
| 3 | Who it's from | Blank section. Height Medium. Colors: Light 1 | Image block `DSC_5624.jpg` in columns 1–5, crop 4:5. Columns 7–12: Text block (small caps "Yoga Educator • Movement Artist", H2 "Meet Quamay "i3" Sams"), Line block, Text block with the first paragraph of your About bio |
| 4 | Final step: sign up | Blank section. Height Medium. Colors: Black Bold. Centred | Text block (H2, gap), Line block, Newsletter block, Layout Float |

### Delivering the free resource

- In the Newsletter block: Storage → connect the same list your other forms use.
- Post-Submit → either a message with the download link, or Redirect to a thank-you page. Both work on Personal.
- Your Notion plan has the welcome email ending in one reply question. That email is sent by your email tool, not by Squarespace.
- Use the same Newsletter block settings in sections 1 and 4 so both feed one list.

**Ends in:** join the newsletter.

---

## 5. Custom CSS

Everything above works with no code. `squarespace-custom.css` adds finish the editor has no setting for. Each piece is independent.

| # | What it does | Why the editor can't | Plan |
|---|---|---|---|
| 1 | Balances heading line breaks | No setting | Any (Custom CSS panel) |
| 2 | Accent underline on navigation hover | Editor styles the active link only | Any (Custom CSS panel) |
| 3 | Buttons turn to an outline on hover | No hover settings | Any (Custom CSS panel) |
| 4 | Gradient over hero photos, dark only behind the text | Overlay is a single flat tint | Any (Custom CSS panel) |
| 5 | Display-sized price numerals on `/private` | Heading sizes are site-wide | Any (Custom CSS panel) |
| 6 | Hides navigation on `/free` only | Per-page header settings don't exist; per-page Code Injection needs Core or higher, so this uses the page ID in site-wide CSS | Any (Custom CSS panel) |
| 7 | Square form fields | Not CSS: Site Styles > Forms | Personal |

To install: Website → Pages → scroll to Custom Code → Custom CSS → paste → Save. Pieces 4, 5 and 6 need an ID pasted in; the file says where to find each one.

I wrote the selectors from your live pages' markup but could not test them inside your editor. Add one piece, look at the page, then add the next. To undo, delete the piece.

---

## 6. Things I noticed and did not touch

These are your call. Nothing has been changed.

- `/about-i3` is an exact copy of the homepage and is in your sitemap.
- `/heal-your-hips` advertises October 11, which has passed. The page says 2.5 hours; its search description says three hours.
- `/train` has three competing next steps (Glo, private inquiry, two studio links).
- `/about`, `/portugal2026` and `/costa-rica-retreat` have no next step of their own.
- `/portugal2026` and `/costa-rica-retreat` have no search description, and their image descriptions are camera file names.
- The Events page links the intensive with the label "[ Details ]".

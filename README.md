# Yoga Practice Tracker

A single-file, offline-friendly tracker for a 3–4 day/week yoga practice (Mon, Wed, Fri + optional Sun).

Open `index.html` in any browser, or serve it with GitHub Pages.

- **Stats:** total days, current and best streak (in consecutive weeks with 3+ sessions), this month vs. goal days, and % of weeks you hit the goal
- **This Week** and **Monthly Progress** panels, plus a 12-week heat strip
- **Calendar:** tap a past day to log it or open its entry
- **Daily log:** date, duration, style, mood, notes (one log per day; saving again updates it)
- **Journal:** search, filter by style or month, edit, delete
- **Backup:** data lives in this browser's localStorage. Use *Export backup* (JSON) or *CSV* regularly; *Import* merges a backup back in and also accepts logs exported from the old Canva version.

# Recomp Macro Log

`artifact/macro-dashboard.html` is a calorie and macro tracker for a body-recomposition plan (start: 2,600 kcal · 215 g protein · 80 g fat · 255 g carbs). It is published as a claude.ai artifact and linked to the **🥣 Nutrition Dashboard** in Notion.

- **Today:** calories-left ring and protein/carbs/fat bars, a coaching line, and Breakfast/Lunch/Dinner/Snacks sections with done checkboxes
- **Logging:** tap a meal icon, type a food (autocomplete from your history and the Notion Food Database), set servings; or use **Quick add** for raw kcal/macros. One-tap chips for your most-logged foods
- **Copy/paste:** copy a meal, a whole day, or selected items and paste them into any day; or copy a meal/day straight from a past date. Multi-select to move or delete
- **Targets:** Mifflin–St Jeor energy calculator (age, height, weight, activity, goal) and editable targets
- **Weekly check-in:** reads your 14-day weight trend, 7-day intake and a strength rating, then suggests adding or trimming 125 kcal from carbs. The recomp range is −0.5% to +0.15% bodyweight per week. It won't adjust until you've been within 10% of target
- **Progress:** weight with smoothed trend, 28 days of calories vs target, 7-day macro averages, habits, and measured maintenance kcal once you have 3 weeks of data
- **Storage:** the artifact's own database when opened in Claude; this browser's localStorage when opened as a plain file
- **Notion:** reads Food Database and Body Metrics. New foods and weigh-ins are copied back (you can turn this off). "Import past days" brings in the Daily Food Log history

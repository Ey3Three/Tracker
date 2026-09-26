# Yoga Practice Tracker

A single-file, offline-friendly tracker for a 3–4 day/week yoga practice (Mon, Wed, Fri + optional Sun).

Open `index.html` in any browser, or serve it with GitHub Pages.

- **Stats:** total days, current and best streak (in consecutive weeks with 3+ sessions), this month vs. goal days, and % of weeks you hit the goal
- **This Week** and **Monthly Progress** panels, plus a 12-week heat strip
- **Calendar:** tap a past day to log it or open its entry
- **Daily log:** date, duration, style, mood, notes (one log per day; saving again updates it)
- **Journal:** search, filter by style or month, edit, delete
- **Backup:** data lives in this browser's localStorage. Use *Export backup* (JSON) or *CSV* regularly; *Import* merges a backup back in and also accepts logs exported from the old Canva version.

# Budget Tracker

`budget.html` is a single-file budget tracker built around Dave Ramsey's 7 Baby Steps. Open it in any browser.

- **Dashboard:** monthly income, expenses, savings, debt balance and what's left each month, Baby Step progress, financial-health ratios, and a timeline that puts every step on the calendar
- **Income / Expenses / Savings / Debt:** editable rows with *Add* and *×* buttons. Totals, progress bars and timelines update as you type. Income can be weekly, biweekly, monthly or yearly, and variable income can be left out of the plan.
- **Baby Steps:** progress comes from savings goals linked to a step and from the debt list. Step 3 is sized from essential expenses plus the mortgage payment (3–6 months).
- **Debt:** avalanche (highest rate) or snowball (smallest balance) order, dated extra payments, plan vs. minimums-only chart, interest saved, and a monthly balance log
- **Timeline engine:** a month-by-month simulation with interest, minimums, rollover of paid-off minimums and extra payments, in Baby Step order. The formulas are listed on the Data tab under *How the numbers work*.
- **Backup:** data lives in this browser's localStorage. Export a JSON backup to keep it safe. *Import* also accepts records exported from the old Canva version.

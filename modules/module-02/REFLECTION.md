# Module 2 — Reflection

**Team name**: _______________
**Branch**: `module-02/<team-name>`
**Submitted**: before Module 3 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You built a service with distinct layers: models, schemas, repository, service, and routes — each with a single responsibility.

**Why not just put everything in one file and call it done?**

Think about what happens six months later when someone new joins the team, or when you need to swap SQLite for PostgreSQL. What does the layered structure protect you from?

> *Your answer:*---------Putting it all in one file would have been faster in the beginning. But once the project grows, it becomes really hard to understand what is happening and where things are breaking,the layered structure makes it easier to code and change the code , fix issues , so even if we change from sqllite to postgresql nothing should break since the logic is implemented seperately and clearly,,f a new developer joins the team after a few months, they can understand the project much faster because every file has one clear responsibility instead of one giant file doing everything.and it is messy , always clarity>>>>>>>complexity/...

---

## 2. Your choice

Each service owns its data exclusively — no other service is allowed to touch its database directly.

**Pick one entity your service owns (e.g. `User`, `Game`). What would go wrong if another service could write to that table directly?**

Give a concrete scenario, not a general principle.

> *Your answer:*-----------------------f The User entity should only be controlled by user-service. If another service could directly write into the users table, it could easily create inconsistent or broken data.
imagine the activity-service directly edits user records when someone logs in or plays a game. A bug there could accidentally overwrite usernames, emails, or even passwords. Then users would suddenly not be able to log in, and it would be difficult to track which service caused the issue.

---

## 3. The tradeoff

You now have models, schemas, a repository, a service, and routes — five layers for what is essentially a CRUD service.

**For a system this small, what is the cost of all this structure?**

And at what point does the complexity start to pay off? Where is the tipping point?

> *Your answer:*---------------The biggest cost is complexity and time. For a very small CRUD service, having five separate layers feels like a lot of setup for something simple. Even adding a small feature means touching multiple files instead of just one.but it is worth it , alwayss clarity >>>> confusion and mess, so yes , it is worth it , we value this structure in the time of an error or bug for sure , while debugging even if it takes time to debug but once we get what is wrong it is much more relieving that a quick fix in a mess, 

---

*Keep this file. You will refer back to it during the oral presentation.*

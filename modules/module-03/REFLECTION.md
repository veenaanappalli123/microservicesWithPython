# Module 3 — Reflection

**Team name**: _______________
**Branch**: `module-03/<team-name>`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*

---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*

---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*

---

*Keep this file. You will refer back to it during the oral presentation.*



###my answers


# Reflection — Module 03

## Question 1

Without a gateway, the frontend would need to directly know every service URL and port like user-service on 8001, game-service on 8002, and activity-service on 8003. That means if even one service changes port or moves somewhere else, the frontend code also needs updates everywhere.
The gateway makes this easier because the frontend only talks to one place, and the gateway forwards the request to the correct service internally. While doing this module I also understood that user-service and game-service themselves did not need any changes for the gateway to work, which showed the purpose of separation between services.

---_____________________________________________________________________________

## Question 2

If user validation is skipped, activities could be created for users that do not even exist. That would create bad and inconsistent data in the database, so validating the user is very important and the request should fail immediately if the user is missing.
The game-service case is different. The activity itself is still valid even if game-service is down, because the game data is only extra information added to the response. That is why returning `"game": null` is better than failing the whole request. During testing, when I stopped the game-service, the activity was still saved correctly, which helped me understand graceful degradation properly.

---_____________________________________________________________________________________

## Question 3

If three services each take around 1 second, then the user may wait around 3 seconds because the request goes through multiple service calls one after another. This showed me how latency increases in microservice architecture.
If one service completely goes down, dependent requests can also fail. But in this module, activity-service was designed in a smarter way where game-service failure does not completely stop the system. Only the optional game data is missing, while the main activity still works.

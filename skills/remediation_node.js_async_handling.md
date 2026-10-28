```markdown
---
name: remediation-node.js-async-handling
description: Targeted remediation exercises and common pitfalls for Node.js Async Handling (Promises, async/await, error management).
---

# 🧠 Remediation Skill: Node.js Asynchronous Mastery

This skill is designed to solidify understanding of non-blocking I/O in Node.js, focusing specifically on the correct usage of Promises and the `async/await` syntax.

## ⚠️ Common Misconceptions (The Pitfalls)

1.  **The "Synchronous Illusion":** Believing that code immediately following an `await` call will execute only *after* the asynchronous task is finished, even if the function is not properly awaited. Misunderstanding how the event loop handles pauses.
2.  **Callback Hell & Promise Mismanagement:** Using nested callbacks or failing to correctly handle Promise rejection (`.catch()`) when errors occur deep within a promise chain, leading to unhandled rejections.

## 🛠️ Scaffolded Practice Exercise: Sequential Data Fetching

**Goal:** Simulate a multi-step data retrieval process where each step depends on the successful completion of the previous one.

**Scenario:**
You have two simulated API calls: `getUser(id)` and `getOrders(userId)`. You must retrieve the user and, only if successful, retrieve their list of orders.

**Scaffolding Instructions:**

1.  **Define Stub Functions:** Create two asynchronous stub functions:
    *   `getUser(id)`: Returns `{ id: id, username: 'StudentX' }` after a 500ms timeout.
    *   `getOrders(userId)`: Returns `[{ orderId: 101, amount: 50 }, { orderId: 102, amount: 75 }]` after a 300ms timeout.
2.  **Implement the Flow:** Use `async/await` within a main function (`fetchUserData`).
3.  **Sequential Execution:** The code must ensure `getOrders` only runs after `getUser` resolves.
4.  **Error Handling:** Wrap the entire sequence in a `try...catch` block to gracefully handle simulated API failures (e.g., if the user ID is invalid).

**Expected Output:** A single promise that resolves with an object containing both the `user` data and the `orders` list.
```
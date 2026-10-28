The core concept error is **Functional Drift (Conceptual Mismatch)**. The developer failed to implement a targeted fix or refactoring; instead, they replaced the entire function's purpose, discarding the requirements for asynchronous data fetching and substituting it with a completely unrelated, synchronous algorithmic function (`findMax`).

The remediation skill must focus on the principles of *API contract adherence* and *managing asynchronous flow* when refactoring or debugging.

***

## `SKILL.md`

```markdown
---
skill_name: Asynchronous Contract Adherence
level: Intermediate
type: Refactoring & Flow Control
description: Ensures that code modifications meet the original functional requirements, especially when dealing with time-based operations (async/await, Promises, callbacks). Avoids functional drift by maintaining the intended API contract.
---

# Asynchronous Contract Adherence

## 🚦 Core Concept Error: Functional Drift (Conceptual Mismatch)

The original code was intended to simulate an **asynchronous data fetch** (fetching `scores` after a delay). The provided patch completely abandoned this objective and replaced the functionality with a synchronous algorithm (`findMax`). This demonstrates a failure to understand that a refactoring must preserve the *external contract* of the function while potentially improving the *internal implementation*.

## ✅ Remediation Skill: Implementing Asynchronous Flow Correctly

When a function relies on time-based operations (like `setTimeout`), you must ensure the function does not return until the operation is complete. In modern JavaScript, this requires wrapping the operation in a Promise and using `async/await`.

### ❌ Anti-Pattern (What the original code attempted):

```javascript
// Function returns immediately, before setTimeout has a chance to run
async function fetchScores() {
  let scores; 
  setTimeout(() => { scores = [98, 85, 92]; }, 100);
  return scores; // Returns undefined/null instantly
}
```

### 💡 Best Practice (The correct fix for the original intent):

The function must be wrapped in a Promise to signal that its completion is deferred.

```javascript
// Correctly fetches data asynchronously and returns a Promise
function fetchScores() {
  return new Promise(resolve => {
    // The resolve() callback ensures the return value is captured by the caller
    setTimeout(() => { 
      const scores = [98, 85, 92];
      resolve(scores); // Resolves the Promise with the data
    }, 100);
  });
}

// Usage example:
async function runFetch() {
  try {
    const scores = await fetchScores();
    console.log("Fetched Scores:", scores); // Logs [98, 85, 92] after 100ms
  } catch (error) {
    console.error("Error fetching scores:", error);
  }
}
```

## 🧠 Key Takeaways

1. **Purpose is King:** Never replace a function's core purpose (e.g., data fetching) with an unrelated calculation (e.g., finding a max).
2. **`async/await` Contract:** If your function performs an action that takes time, it must signal that to the caller. In JavaScript, this means returning a `Promise`.
3. **Execution Order:** Remember that synchronous code executes immediately. `setTimeout` places code in the event queue to execute *later*. If you `return` before the event queue runs, you return the initial state.
```
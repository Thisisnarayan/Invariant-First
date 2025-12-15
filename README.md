⸻

# invariant-first

**Build financial systems where money cannot disappear.**

⸻

## What is invariant-first?

invariant-first is a lightweight Python framework for financial backends that enforces business invariants as executable laws, not comments or test cases.

Instead of starting with endpoints and use-case tests, you start by declaring what must never break — and the system ensures your core business logic cannot violate those rules.

If a change violates a declared invariant, it should fail before deployment, not in production.

⸻

## The problem this repo addresses

Modern backend systems rely heavily on:
- Use-case based tests
- Code reviews
- "Looks correct" logic

This approach does not scale when:
- Systems grow complex
- Refactors accumulate
- Retry logic is added
- AI generates code faster than humans can review

Many real-world financial bugs share the same pattern:

**Tests passed.**  
**Code was reviewed.**  
**A global business law was silently violated.**

Examples:
- Money created or destroyed
- Double spending under retries
- Negative balances after edge cases
- Subtle refactors breaking invariants

**Tests check examples.**  
**Invariants define correctness.**

⸻

## Core idea

**Business invariants are the source of truth.**  
**Code is guilty until proven innocent.**

You explicitly declare laws such as:
- Total money is conserved
- Balances never go negative
- Transfers are atomic
- Operations are idempotent under retries

The system then:
1. Forces core logic to be written as pure state transitions
2. Continuously checks that invariants hold
3. Treats invariant violations as compile-time failures (not runtime surprises)

⸻

## What invariant-first is (and is not)

**It is:**
- A tool: a Python library you use in real backends
- A discipline: law-first, spec-first design
- A bridge between today's backend practices and future formal verification

**It is not:**
- ❌ A replacement for FastAPI
- ❌ A test framework
- ❌ "Lean / Coq in production"
- ❌ Automatic or magical code repair
- ❌ An autonomous AI agent

Instead, it is a discipline and toolset that sits between today's Python backends and tomorrow's formally verified systems.

**Invariant-first does not invent business rules.**  
**It refuses to let you violate the ones you declare.**

⸻

## How it fits into a FastAPI backend

The architecture is intentionally simple:

```
FastAPI / HTTP
      ↓
   Adapters
      ↓
Pure State Transitions   ←─── verified against invariants
      ↓
   New State
      ↓
Database
```

- FastAPI handles IO
- The database handles persistence
- Invariant-first protects the business logic

Only the pure model is subject to invariants and (eventually) proofs.

⸻

## Example (conceptual)

Declare an invariant:

```python
@invariant("Total balance is conserved")
def total_balance_preserved(before, after):
    return sum(before.balances.values()) == sum(after.balances.values())
```

Write a pure transition:

```python
def transfer(state, from_id, to_id, amount):
    ...
    return new_state
```

If a refactor, feature, or AI-generated change violates the invariant:
- The system fails immediately
- A counterexample is produced
- The change cannot be shipped

**No guessing. No post-mortems.**

⸻

Why financial systems first?

This project starts intentionally narrow.

Financial systems have:
- Clear, non-negotiable invariants
- High cost of failure
- Well-documented real-world incidents
- Immediate relevance in an AI-generated code world

Wallets, ledgers, exchanges, and trading systems are where "probably correct" is unacceptable.

Once proven here, the approach generalizes to other domains.


⸻

Invariant-first is designed as a bridge, not a leap:
**Today**
- Executable invariants (Python)
- Test-time and runtime enforcement
- Clear separation of IO and logic
- Optional AI assistance for invariant discovery

**Tomorrow**
- Exportable formal models (Lean / Coq)
- AI-generated proof attempts
- Proof failures treated like compiler errors

The goal is not academic purity — it is machine-checkable correctness.

## Project goals

- Make invariants first-class
- Make violations impossible to ignore
- Prepare backends for AI-generated code
- Teach a spec-first way of thinking
- Stay practical, incremental, and usable

⸻

## Non-goals (for now)

- Proving HTTP servers or databases
- Replacing integration tests
- Solving all concurrency problems magically
- Being a general-purpose framework from day one

**Clarity > breadth.**

⸻

## Status

🚧 **Early design / exploration**

This repo is focused on ideas, architecture, and correctness, not production polish.

Contributions, critique, and hard questions are welcome.

⸻

**Tests sample behavior.**  
**Invariants define reality.**

⸻


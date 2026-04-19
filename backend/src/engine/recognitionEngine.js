const pool = require("../db");
const crypto = require("crypto");

function uuidv4() {
  return crypto.randomUUID();
}

async function computeRecognition(resourceId) {
  // -------------------------
  // 1. LOAD DATA
  // -------------------------
  const obligations = await pool.query(
    "SELECT * FROM obligation WHERE resource_id = $1",
    [resourceId]
  );

  const events = await pool.query(
    "SELECT * FROM governance_event WHERE resource_id = $1 ORDER BY timestamp DESC",
    [resourceId]
  );

  let state = "VALID";
  let reason = "All conditions satisfied";

  // -------------------------
  // 2. EVENT RULES (LOCAL)
  // -------------------------
  for (const event of events.rows) {
    if (event.event_type === "THORIUM_EXCEEDED") {
      state = "SUSPENDED";
      reason = "Thorium threshold exceeded";
      break;
    }

    if (event.event_type === "AUTHORITY_SUSPEND") {
      state = "SUSPENDED";
      reason = "Authority suspension";
      break;
    }

    if (event.event_type === "ESG_VIOLATION") {
      state = "FLAGGED";
      reason = "ESG violation detected";
    }
  }

  // -------------------------
  // 3. OBLIGATIONS
  // -------------------------
  if (state !== "SUSPENDED") {
    for (const ob of obligations.rows) {
      const fulfillment = await pool.query(
        "SELECT * FROM fulfillment WHERE obligation_id = $1 AND verified = true",
        [ob.id]
      );

      if (fulfillment.rows.length === 0) {
        const now = new Date();
        const deadline = new Date(ob.deadline);

        if (now > deadline) {
          state = "FLAGGED";
          reason = "Deadline breached";
          break;
        } else {
          state = "CONDITIONAL";
          reason = "Pending obligation";
        }
      }
    }
  }

  // -------------------------
  // 4. PROPAGATION (UPSTREAM CHECK)
  // -------------------------
  const parents = await pool.query(
    "SELECT * FROM lineage WHERE child_resource_id = $1",
    [resourceId]
  );

  for (const parent of parents.rows) {
    const parentState = await pool.query(
      "SELECT state FROM recognition_state WHERE resource_id = $1 ORDER BY created_at DESC LIMIT 1",
      [parent.parent_resource_id]
    );

    if (parentState.rows.length > 0) {
      const upstream = parentState.rows[0].state;

      if (upstream === "SUSPENDED") {
        state = "SUSPENDED";
        reason = "Upstream suspended";
        break;
      }

      if (upstream === "FLAGGED" && state !== "SUSPENDED") {
        state = "FLAGGED";
        reason = "Upstream risk propagated";
      }
    }
  }

  // -------------------------
  // 5. WRITE STATE
  // -------------------------
  await pool.query(
    "INSERT INTO recognition_state (id, resource_id, state, reason, authority) VALUES ($1,$2,$3,$4,$5)",
    [uuidv4(), resourceId, state, reason, "SYSTEM"]
  );

  return { state, reason };
}

module.exports = { computeRecognition };

const express = require("express");
const pool = require("./src/db");
const crypto = require("crypto");

function uuidv4() {
  return crypto.randomUUID();
}

const {
  computeRecognition,
  simulateRecognition
} = require("./src/engine/recognitionEngine");

const app = express();

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "*");
  next();
});

app.use(express.json());

app.get("/", (req, res) => {
  res.send("ArcTopia running");
});

app.post("/resource", async (req, res) => {
  try {
    const id = uuidv4();
    const { name, origin_location = null, operator = null } = req.body;

    await pool.query(
      "INSERT INTO resource (id, name, origin_location, operator) VALUES ($1, $2, $3, $4)",
      [id, name, origin_location, operator]
    );

    res.json({ id });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create resource" });
  }
});

app.get("/resources", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM resource ORDER BY created_at ASC");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch resources" });
  }
});

app.get("/lineage", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM lineage");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch lineage" });
  }
});

app.post("/lineage", async (req, res) => {
  try {
    const id = uuidv4();
    const { parent_resource_id, child_resource_id, ratio = 1.0 } = req.body;

    await pool.query(
      "INSERT INTO lineage (id, parent_resource_id, child_resource_id, ratio) VALUES ($1, $2, $3, $4)",
      [id, parent_resource_id, child_resource_id, ratio]
    );

    res.json({ id });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create lineage link" });
  }
});

app.post("/obligation", async (req, res) => {
  try {
    const id = uuidv4();
    const { resource_id, type = null, description = null, deadline } = req.body;

    await pool.query(
      "INSERT INTO obligation (id, resource_id, type, description, deadline, status) VALUES ($1, $2, $3, $4, $5, $6)",
      [id, resource_id, type, description, deadline, "DECLARED"]
    );

    res.json({ id });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create obligation" });
  }
});

app.post("/fulfillment", async (req, res) => {
  try {
    const id = uuidv4();
    const {
      obligation_id,
      evidence = {},
      verified = true,
      verified_by = "SYSTEM"
    } = req.body;

    await pool.query(
      "INSERT INTO fulfillment (id, obligation_id, evidence, verified, verified_by, timestamp) VALUES ($1, $2, $3, $4, $5, NOW())",
      [id, obligation_id, JSON.stringify(evidence), verified, verified_by]
    );

    res.json({ id });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create fulfillment" });
  }
});

app.post("/event", async (req, res) => {
  try {
    const id = uuidv4();
    const { resource_id, event_type = "check", payload = {} } = req.body;

    await pool.query(
      "INSERT INTO governance_event (id, resource_id, event_type, payload) VALUES ($1, $2, $3, $4)",
      [id, resource_id, event_type, JSON.stringify(payload)]
    );

    const result = await computeRecognition(resource_id);

    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to process live event" });
  }
});

app.get("/state/:id", async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT * FROM recognition_state WHERE resource_id = $1 ORDER BY created_at DESC LIMIT 1",
      [req.params.id]
    );

    res.json(result.rows[0] || null);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch state" });
  }
});

app.post("/simulate", async (req, res) => {
  try {
    const { resource_id, simulated_event_type = "check" } = req.body;

    const result = await simulateRecognition(resource_id, simulated_event_type);

    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to simulate scenario" });
  }
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});

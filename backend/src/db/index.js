const { Pool } = require("pg");

const pool = new Pool({
  user: process.env.PGUSER || "arctopia",
  host: process.env.PGHOST || "localhost",
  database: process.env.PGDATABASE || "arctopia",
  password: process.env.PGPASSWORD || "arctopia",
  port: Number(process.env.PGPORT || 5432),
});

pool.on("connect", () => {
  console.log("Connected to PostgreSQL");
});

module.exports = pool;

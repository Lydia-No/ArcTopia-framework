CREATE TABLE resource (
  id UUID PRIMARY KEY,
  name TEXT,
  origin_location TEXT,
  operator TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE obligation (
  id UUID PRIMARY KEY,
  resource_id UUID,
  type TEXT,
  description TEXT,
  deadline TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  status TEXT
);

CREATE TABLE fulfillment (
  id UUID PRIMARY KEY,
  obligation_id UUID,
  evidence JSONB,
  verified BOOLEAN,
  verified_by TEXT,
  timestamp TIMESTAMP
);

CREATE TABLE recognition_state (
  id UUID PRIMARY KEY,
  resource_id UUID,
  state TEXT,
  reason TEXT,
  authority TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE governance_event (
  id UUID PRIMARY KEY,
  resource_id UUID,
  event_type TEXT,
  payload JSONB,
  timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE lineage (
  id UUID PRIMARY KEY,
  parent_resource_id UUID,
  child_resource_id UUID,
  ratio FLOAT
);

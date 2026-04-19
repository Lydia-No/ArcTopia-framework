from fastapi import FastAPI

from backend.core.runtime import Runtime

app = FastAPI(title="field-core")
runtime = Runtime()


@app.get("/")
def root():
    return {"status": "running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/state")
def state():
    return runtime.state()


@app.post("/step")
def step():
    runtime.step()
    return runtime.state()

"""FastAPI application demonstrating REST patterns."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

from example_pkg import Counter

app = FastAPI(
    title="py-fullstack-template API",
    description="Example API demonstrating REST patterns with FastAPI",
    version="0.1.0",
)


class CounterRequest(BaseModel):
    """Request model for counter operations."""

    value: int = Field(default=0, description="Starting value")
    amount: int = Field(default=1, ge=1, description="Amount to increment/decrement")


class CounterResponse(BaseModel):
    """Response model for counter operations."""

    result: int = Field(..., description="Result after operation")


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/counter/increment", response_model=CounterResponse)
def increment(request: CounterRequest) -> CounterResponse:
    """Increment a value and return the result."""
    counter = Counter(start=request.value)
    counter.increment(request.amount)
    return CounterResponse(result=counter.value)


@app.post("/counter/decrement", response_model=CounterResponse)
def decrement(request: CounterRequest) -> CounterResponse:
    """Decrement a value and return the result."""
    counter = Counter(start=request.value)
    counter.decrement(request.amount)
    return CounterResponse(result=counter.value)

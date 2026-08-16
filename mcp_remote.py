from fastmcp import FastMCP

mcp = FastMCP("Restaurant")


@mcp.tool
def menu() -> list[str]:
    """Return the food items provided by the restaurant."""
    return ["biryani", "ice cream", "pizza"]


@mcp.tool
def locations() -> list[str]:
    """Return the restaurant locations."""
    return ["Hyderabad", "Bangalore", "Mumbai", "Delhi"]


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=5001,
    )
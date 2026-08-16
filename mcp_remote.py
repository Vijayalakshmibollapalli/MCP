from fastmcp import FastMCP

mcp = FastMCP(name='Restaurent')

@mcp.tool
def menu():
    '''The food items provided by restaurant'''
    food = ['biryani', 'ice cream', 'pizza']
    return food

@mcp.tool
def locations():
    '''The location of the restaurent'''
    locations = ['Hyderabad', "Banglore", "Mumbai", "Delhi"]
    return locations

if __name__ == '__main__':
    mcp.run(transport='streamable-http', port = 5001, host = '0.0.0.0')


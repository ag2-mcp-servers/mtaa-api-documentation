# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T07:02:40+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity

app = MCPProxy(
    contact={
        'email': 'isaackeinstein@gmail.com',
        'name': 'Mtaa API',
        'url': 'https://github.com/HackEAC/mtaaAPI',
    },
    description="Mtaa A simple REST API to access Tanzania's location information,With mtaa API you can easily query and integrate all the location in tanzania from region level to streets from your programming language of your your choice",
    license={
        'name': 'MIT License',
        'url': 'https://github.com/HackEAC/mtaaAPI/blob/main/LICENSE',
    },
    title='Mtaa API Documentation',
    version='1.0',
    servers=[
        {
            'description': 'Production Server',
            'url': 'https://mtaa-api.herokuapp.com/api',
        }
    ],
)


@app.get(
    '/{country}',
    description=""" Fetches all regions present in Tanzania and then return a response as json """,
    tags=['tanzania_geographical_data'],
)
def tanzania_regions(country: str):
    """
    Returns all regions present in Tanzania
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{country}/{region}',
    description=""" Returns a post code and all districts in a specified region """,
    tags=['tanzania_geographical_data'],
)
def districts_in_a_region(country: str, region: str = ...):
    """
    Returns all districts in region
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{country}/{region}/{district}',
    description=""" Returns all wards in a  specified district and district postcode """,
    tags=['tanzania_geographical_data'],
)
def wards_in_a_district(country: str, region: str = ..., district: str = ...):
    """
    Returns all wards in a district
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{country}/{region}/{district}/{ward}',
    description=""" Returns all streets in a specified ward and ward postcode """,
    tags=['tanzania_geographical_data'],
)
def streets_in_a_ward(
    country: str, region: str = ..., district: str = ..., ward: str = ...
):
    """
    Returns all streets in a ward
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/{country}/{region}/{district}/{ward}/{street}',
    description=""" Returns all neighborhood in a specified street """,
    tags=['tanzania_geographical_data'],
)
def neighborhood_in_a_street_(
    country: str,
    region: str = ...,
    district: str = ...,
    ward: str = ...,
    street: str = ...,
):
    """
    Returns all neighborhood in a street
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)

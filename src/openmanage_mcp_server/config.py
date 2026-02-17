"""Configuration for OpenManage Enterprise MCP Server."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings loaded from environment variables (OME_ prefix)."""

    ome_host: str = ""
    ome_username: str = ""
    ome_password: str = ""
    ome_transport: str = "stdio"
    ome_log_level: str = "INFO"

    model_config = {"env_prefix": ""}

    # Map to env vars: OME_HOST, OME_USERNAME, OME_PASSWORD

"""Elasticsearch client and connection manager."""

from typing import Optional

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError as ESConnectionError

from src.utils.config import settings
from src.utils.logger import get_logger

logger = get_logger(__name__)


class ElasticsearchClient:
    """Manages Elasticsearch connection and operations."""
    
    def __init__(
        self,
        host: str = None,
        port: int = None,
        username: str = None,
        password: str = None
    ):
        """Initialize Elasticsearch client.
        
        Args:
            host: Elasticsearch host
            port: Elasticsearch port
            username: Username for authentication
            password: Password for authentication
        """
        self.host = host or settings.elasticsearch_host
        self.port = port or settings.elasticsearch_port
        self.username = username or settings.elasticsearch_user
        self.password = password or settings.elasticsearch_password
        
        if self.host.startswith('http'):
            self.url = self.host
        else:
            self.url = f"http://{self.host}:{self.port}"
            
        self._client: Optional[Elasticsearch] = None
        
    @property
    def client(self) -> Elasticsearch:
        """Get or create Elasticsearch client.
        
        Returns:
            Elasticsearch client instance
        """
        if self._client is None:
            self._connect()
        return self._client
    
    def _connect(self):
        """Establish connection to Elasticsearch."""
        try:
            logger.info(f"Connecting to Elasticsearch at {self.url}")
            
            # Determine connection parameters
            connection_params = {
                "hosts": [self.url],
                "request_timeout": 30
            }
            
            # Add authentication if provided (required for Bonsai.io)
            if self.username and self.password and self.password != "changeme":
                connection_params["basic_auth"] = (self.username, self.password)
            
            # Handle SSL for cloud hosts
            if self.url.startswith('https'):
                connection_params["verify_certs"] = True
            else:
                connection_params["verify_certs"] = False
                connection_params["ssl_show_warn"] = False

            self._client = Elasticsearch(**connection_params)
            
            # Test connection
            if self._client.ping():
                info = self._client.info()
                version = info['version']['number']
                logger.info(f"Connected to Elasticsearch {version}")
            else:
                raise ESConnectionError("Failed to ping Elasticsearch")
                
        except Exception as e:
            logger.error(f"Failed to connect to Elasticsearch: {e}", exc_info=True)
            raise
    
    def is_connected(self) -> bool:
        """Check if connected to Elasticsearch.
        
        Returns:
            True if connected, False otherwise
        """
        try:
            return self.client.ping()
        except:
            return False
    
    def close(self):
        """Close Elasticsearch connection."""
        if self._client:
            self._client.close()
            self._client = None
            logger.info("Elasticsearch connection closed")
    
    def get_cluster_health(self) -> dict:
        """Get cluster health information.
        
        Returns:
            Cluster health dictionary
        """
        return self.client.cluster.health()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

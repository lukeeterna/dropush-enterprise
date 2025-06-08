class EBayClient:
    """Minimal eBay API client stub."""
    def __init__(self, app_id, cert_id, token, sandbox=True):
        self.app_id = app_id
        self.cert_id = cert_id
        self.token = token
        self.sandbox = sandbox

    def get_trending_products(self, category_id=None, limit=100):
        """Ritorna la lista stub dei top N prodotti in una categoria."""
        # TODO: implementare chiamata reale via ebaysdk
        return []

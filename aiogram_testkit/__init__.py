"""
aiogram-testkit main module.
"""

class MockBot:
    """
    Stub for a bot mock that avoids real network requests.
    """
    def __init__(self, token: str = "123:test"):
        self.token = token
        
    async def __call__(self, method, *args, **kwargs):
        # TODO: implement request interception
        pass

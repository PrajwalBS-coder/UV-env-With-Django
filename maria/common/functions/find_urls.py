
def find_be_url(environment=None):
    """
    Returns the url based on the environment
    if environment is dev then return https://dev.myfairworx.com/api/
    if environment is stage then return https://stage.myfairworx.com/api/
    if local then return http://127.0.0.1:8000/api/
    """
    if environment == "dev":
        return "https://dev.myfairworx.com/api/"
    elif environment == "stage":
        return "https://stage.myfairworx.com/api/"
    else:
        return "http://127.0.0.1:8000/api/"
    
def find_fe_url(environment=None):
    """
    Returns the url based on the environment
    if environment is dev then return https://dev.myfairworx.com/
    if environment is stage then return https://stage.myfairworx.com/
    if local then return http://127.0.0.1:8000/
    """
    if environment == "dev":
        return "https://dev.myfairworx.com/"
    elif environment == "stage":
        return "https://stage.myfairworx.com/"
    else:
        return "http://127.0.0.1:8001/silk/"
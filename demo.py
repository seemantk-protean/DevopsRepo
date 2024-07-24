import requests


def check_nifi_connectivity(nifi_url):
    """
    Function to check connectivity to Apache NiFi.

    Args:
    - nifi_url (str): URL of the NiFi instance (e.g., http://nifi-host:8080)

    Returns:
    - bool: True if NiFi is reachable, False otherwise
    """
    try:
        response = requests.get(f"{nifi_url}/nifi-api/system-diagnostics", timeout=10,verify=False)
        if response.status_code == 200:
            print(f"Successfully connected to NiFi at {nifi_url}")
            return True
        else:
            print(f"Failed to connect to NiFi at {nifi_url}. Status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to NiFi at {nifi_url}: {e}")
        return False


# Example usage
nifi_url = "https://localhost:8443"  # Replace with your NiFi URL
is_connected = check_nifi_connectivity(nifi_url)

if is_connected:
    print("Succuess full made")
    # Perform actions if NiFi is reachable
    # Example: Trigger a NiFi flow, retrieve data, etc.
    pass
else:
    # Handle case where NiFi is not reachable
    print("check your connections")
    pass

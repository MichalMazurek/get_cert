import ssl
from urllib.parse import urlparse
import click


def get_certificate(url: str) -> str:
    """Download certificate from remote server."""
    parsed_url = urlparse(url)

    hostname = parsed_url.hostname
    port = int(parsed_url.port or 443)
    conn = ssl.create_connection((hostname, port))
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sock = context.wrap_socket(conn, server_hostname=hostname)
    return ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))


@click.command()
@click.argument("url", type=str)
def main(url: str):
    """Retrieve and print out the ssl certificate.

    Args:
        URL (str): url to be picked up
    """
    click.echo(get_certificate(url), nl=False)


if __name__ == "__main__":
    main()

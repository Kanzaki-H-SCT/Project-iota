#LICENCE :   http://www.apache.org/licenses/LICENSE-2.0
#CREATOR BY : PRANKBOT
#MOD BY ACIL
import logging
import sys
from thrift.transport.TTransport import TTransportException
logger = logging.getLogger(__name__)
def legacy_validate_callback(cert, hostname):
    if 'subject' not in cert:
        raise TTransportException(
            TTransportException.NOT_OPEN,
            'sert tidak ada di ssl dengan user name %s' % hostname)
    fields = cert['subject']
    for field in fields:
        if not isinstance(field, tuple):
            continue
        cert_pair = field[0]
        if len(cert_pair) < 2:
            continue
        cert_key, cert_value = cert_pair[0:2]
        if cert_key != 'commonName':
            continue
        certhost = cert_value
        if certhost == hostname:
            return
        else:
            raise TTransportException(
                TTransportException.UNKNOWN,
                'Hostname we connected to "%s" doesn\'t match certificate '
                'provided commonName "%s"' % (hostname, certhost))
    raise TTransportException(
        TTransportException.UNKNOWN,
        'Could not validate SSL certificate from host "%s".  Cert=%s'
        % (hostname, cert))
def _optional_dependencies():
    try:
        import ipaddress  # noqa
        logger.debug('ipaddress module is available')
        ipaddr = True
    except ImportError:
        logger.warn('ipaddress module is unavailable')
        ipaddr = False
    if sys.hexversion < 0x030500F0:
        try:
            from backports.ssl_match_hostname import match_hostname, __version__ as ver
            ver = list(map(int, ver.split('.')))
            logger.debug('backports.ssl_match_hostname module is available')
            match = match_hostname
            if ver[0] * 10 + ver[1] >= 35:
                return ipaddr, match
            else:
                logger.warn('backports.ssl_match_hostname module is too old')
                ipaddr = False
        except ImportError:
            logger.warn('backports.ssl_match_hostname is unavailable')
            ipaddr = False
    try:
        from ssl import match_hostname
        logger.debug('ssl.match_hostname is available')
        match = match_hostname
    except ImportError:
        logger.warn('using legacy validation callback')
        match = legacy_validate_callback
    return ipaddr, match
_match_has_ipaddress, _match_hostname = _optional_dependencies()
# MOD BY ACIL
"""
    ftp_utilities.py

    Provides utility classes used to crawl FTP servers.

    This code is adapted from:
        https://gearheart.io/blog/crawling-ftp-server-with-scrapy/
"""

import json
from twisted.protocols.ftp import FTPFileListProtocol
from scrapy.http import Request, Response
from scrapy.core.downloader.handlers.ftp import FTPDownloadHandler


class FtpMetaRequest(Request):
    # Add user with password to ftp meta request
    user_meta = {'ftp_user': 'username', 'ftp_password': ''}

    def init(self, args, **kwargs):
        super(FtpMetaRequest, self).init(args, **kwargs)
        self.meta.update(self.user_meta)


class FileFtpRequest(FtpMetaRequest):
    """ Placeholder class used to indicate that a URL points to a single file that can be downloaded """
    pass


class ListFtpRequest(FtpMetaRequest):
    """ Placeholder class used to indicate that a URL points to a directory listing that can be crawled """
    pass


class FtpListingHandler(FTPDownloadHandler):
    """ Custom handler for FTP directory listings which yields callbacks with the directory listing content """

    def gotClient(self, client, request, filepath):
        """ Gets files list or one file """

        # Check what class sent a request
        if not isinstance(request, ListFtpRequest):
            return super(FtpListingHandler, self).gotClient(client, request, filepath)

        protocol = FTPFileListProtocol()
        return client.list(filepath, protocol).addCallbacks(callback=self._build_response, callbackArgs=(request, protocol), errback=self._failed, errbackArgs=(request, ))

    def _build_response(self, result, request, protocol):
        """ Get files list or one file """

        # Check what class sent a request
        if not isinstance(request, ListFtpRequest):
            return super(FtpListingHandler, self)._build_response(result, request, protocol)

        self.result = result
        body = json.dumps(protocol.files)
        return Response(url=request.url, status=200, body=body)

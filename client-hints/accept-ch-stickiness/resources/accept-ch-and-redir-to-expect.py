def main(request, response):
    return 301, [('Location', 'expect-client-hint-headers.html'),('Accept-CH', 'device-memory, DPR')], ''

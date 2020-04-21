import argparse
import server
import browser

ap = argparse.ArgumentParser(
    description='CaptchaHarvester: Solve captchas yourself without having to pay for services like 2captcha for use in automated projects.',
    epilog='For help contact @MacHacker#7322 (Discord)')
ap.add_argument('type', choices=['recaptcha', 'hcaptcha'],
                help='the type of captcha you are want to solve')
ap.add_argument('-k', '--site-key', required=True,
                help='the sitekey used by the captcha on page')
ap.add_argument('-d', '--domain', required=True,
                help='the domain for which you want to solve captchas')
ap.add_argument('-H', '--host', help='defaults to 127.0.0.1',
                default='127.0.0.1')
ap.add_argument('-p', '--port', help='defaults to 5000',
                default=5000, type=int)

ap.add_argument('-b', '--browser',
                help='which browser to open on launch', choices=['chrome', 'brave'])
ap.add_argument('-r', '--restart-browser',
                help='if this flag is not passed, a new instance of the browser will'
                'be opened. this flag is most helpful when solving Googles ReCaptchas'
                'because if you restat your main profile you\'ll most likely be logged'
                'into Google and will be given an easier time on the captchas', default=False, action='store_true')
args = ap.parse_args()

print(f'server running on http://{args.host}:{args.port}')

httpd = server.setup(args.host, args.port, args.domain,
                     args.type, args.site_key)

if args.browser:
    host, port = httpd.server_address
    browser.launch(f'http://{host}:{port}/www.sneakersnstuff.com.pac',
                   browser=args.browser, restart=args.restart_browser)

server.serve(httpd)
